from flask import current_app
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os
from rq import Queue
from redis import Redis, RedisError

class EmailService:
    def __init__(self):
        self.mail = Mail()
        self.serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY', 'your_secret_key'))

        # Redis configuration
        redis_host = os.getenv('REDIS_HOST', 'localhost')  # Replace with your Redis host
        redis_port = int(os.getenv('REDIS_PORT', 6379))  # Default Redis port
        redis_password = os.getenv('REDIS_PASSWORD', None)  # Replace with your Redis password if needed

        try:
            # Connect to Redis
            self.redis_conn = Redis(host=redis_host, port=redis_port, password=redis_password)
            self.email_queue = Queue('email_queue', connection=self.redis_conn)
        except RedisError as e:
            print(f"Error connecting to Redis: {e}")
            self.email_queue = None  # Avoid using the queue if connection fails

    def init_app(self, app):
        """Initialize the app with mail configurations."""
        app.config['MAIL_SERVER'] = 'smtp.office365.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
        app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
        app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
        self.mail.init_app(app)

    def send_email(self, recipient, subject, body):
        """Send an email using Flask-Mail."""
        with current_app.app_context():  # Use app context only here
            try:
                msg = Message(subject, recipients=[recipient])
                msg.body = body
                self.mail.send(msg)
            except Exception as e:
                print(f"Error sending email: {e}")

    def create_token(self, email):
        """Create a token for email validation."""
        return self.serializer.dumps(email, "test")

    def send_validation_email(self, email):
        print("Preparing to send validation email...")
        token = self.create_token(email)
        message = {
            'recipient': email,
            'subject': "Validate Your Email",
            'body': f"Please click the link to validate your email: http://yourdomain.com/validate/{token}"
        }

        # Check if Redis queue is initialized
        if not self.email_queue:
            print("Email queue is not initialized.")
            return

        # Enqueue the email sending job
        job = self.email_queue.enqueue(self._enqueue_send_email, message['recipient'], message['subject'], message['body'])
        print(f"Job enqueued: {job.id}")

    def _enqueue_send_email(self, recipient, subject, body):
        """Wrapper function to enqueue the email sending job."""
        self.send_email(recipient, subject, body)

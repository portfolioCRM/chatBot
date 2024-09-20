from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
''' 
The `load_dotenv()` function loads environment variables from a .env file
into the environment. This is useful for managing configuration settings
such as the Flask environment mode and other secrets.
'''
load_dotenv()

# Create an instance of the Flask application
'''
Create an instance of the Flask application. This `app` object is the core 
of the Flask application and is used to register routes, handle requests, 
and run the application.
'''
app = Flask(__name__)

# Import and register the healthcare Blueprint from the routes module
'''
Import the `healthcare` function from the `routes` module and register it 
with the Flask application. The `healthcare` function sets up the routes 
defined in the health blueprint so that they can be served by the Flask 
application.
'''
from routes import healthcare
healthcare(app)

if __name__ == '__main__':
    # Read the environment mode from environment variables
    '''
    The `FLASK_ENV` environment variable determines the mode in which the 
    Flask application runs. The default value is 'development' if the 
    variable is not set.
    '''
    env_mode = os.getenv('FLASK_ENV', 'development')
    
    # Run the Flask application
    '''
    The `app.run()` method starts the Flask development server. The `debug` 
    parameter is set based on the environment mode. If the environment mode 
    is 'development', debugging is enabled to assist with development and 
    troubleshooting. In 'production' mode, debugging is disabled.
    '''
    app.run(debug=(env_mode == 'development'))

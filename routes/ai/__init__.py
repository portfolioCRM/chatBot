from .choose_algorithm import chatbot_bp

def choose_algorithm(app):
    """
    Register the FAQ Blueprint with the Flask application.
    
    This function takes a Flask application instance and registers the
    `faq_bp` Blueprint with it. Blueprints allow for better organization
    of routes related to FAQs. By registering the Blueprint, the routes
    defined in the `faq` module become part of the main Flask application.

    Args:
        app (Flask): The Flask application instance to register the Blueprint with.

    Returns:
        None
    """
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

from flask import Blueprint

# Import the health blueprint from the health module
from .health import health_bp

def healthcare(app):
    """
    Register the healthcare Blueprint with the Flask application.
    
    This function takes a Flask application instance and registers the
    `health_bp` Blueprint with it. Blueprints are used to organize routes
    and handlers in a modular way. By registering the Blueprint, the routes
    defined in the `health` module become part of the main Flask application.

    Args:
        app (Flask): The Flask application instance to register the Blueprint with.

    Returns:
        None
    """
    app.register_blueprint(health_bp)

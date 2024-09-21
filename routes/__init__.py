from flask import Blueprint

from .health import health_bp
from .faq import faq_bp

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

def faq(app):
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
    app.register_blueprint(faq_bp, url_prefix='/faq')

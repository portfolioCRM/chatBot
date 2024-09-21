from flask import Blueprint
from flask_babel import gettext as _

from config.response import success_response, server_error_response


# Create a Blueprint for health-related routes
# A Blueprint in Flask is a way to organize routes and handlers into separate modules.
# It allows you to group related routes together and register them with the main application.
health_bp = Blueprint('health', __name__)

@health_bp.route('/')
def home():
    """
    Home route for the health blueprint.
    
    This route handles requests to the root URL ('/') of the health blueprint.
    It returns a JSON response with a message indicating the health of the server.
    
    Returns:
        Response: A JSON response with a message, status code, and success status.
    """
    try:
        response_message = _("Server runs with success")
        # Attempt to generate a success response
        return success_response(response_message)
    except Exception as e:
        response_message = _("Server runs failed")
        # Handle any errors that occur and provide a failure response
        return server_error_response(response_message)
        # Optionally, log the exception e for debugging purposes
        # print(f"Error: {e}")

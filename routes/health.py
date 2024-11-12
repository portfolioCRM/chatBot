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
    Home route for the health blueprint _test_.
    ---
    tags:
      - Health
    parameters:
      - in: header
        name: Accept-Language
        type: string
        enum: ["en", "fr", "ar", "es"]
        required: true
        description: "Language preference for the response."
    responses:
      200:
        description: Server is running successfully
        schema:
          type: object
          properties:
            success:
              type: boolean
            message:
              type: string
      500:
        description: Server failed to run
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

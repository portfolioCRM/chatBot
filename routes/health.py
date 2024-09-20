from flask import Blueprint, jsonify

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
        # Attempt to generate a success response
        response = {
            'message': 'Server runs with success',
            'status': 200,
            'success': True
        }
    except Exception as e:
        # Handle any errors that occur and provide a failure response
        response = {
            'message': 'Server runs failed',
            'status': 500,
            'success': False
        }
        # Optionally, log the exception e for debugging purposes
        # print(f"Error: {e}")

    return jsonify(response)
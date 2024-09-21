from flask import jsonify
from flask_babel import gettext as _

def create_response(message, status=200, success=True, data=None):
    """
    Creates a standardized JSON response.

    Args:
        message (str): The message to include in the response.
        status (int): The HTTP status code (default is 200).
        success (bool): Whether the operation was successful (default is True).
        data (dict, optional): Additional data to include in the response.

    Returns:
        Response: A Flask JSON response object.
    """
    response = {
        'message': _(message),
        'status': status,
        'success': success
    }
    if data is not None:
        response['data'] = data
    
    return jsonify(response)

# Wrapper function for 200 OK with optional data
def success_response(message="Operation successful", data=None):
    return create_response(message, status=200, success=True, data=data)

# Wrapper function for 204 No Content
def no_content_response(message="No content", data=None):
    return create_response(message, status=204, success=True, data=data)

# Wrapper function for 201 Created with optional data
def created_response(message="Resource created successfully", data=None):
    return create_response(message, status=201, success=True, data=data)

# Wrapper function for 400 Bad Request
def bad_request_response(message="Bad request", data=None):
    return create_response(message, status=400, success=False, data=data)

# Wrapper function for 401 Unauthorized
def unauthorized_response(message="Unauthorized", data=None):
    return create_response(message, status=401, success=False, data=data)

# Wrapper function for 403 Forbidden
def forbidden_response(message="Forbidden", data=None):
    return create_response(message, status=403, success=False, data=data)

# Wrapper function for 404 Not Found
def not_found_response(message="Resource not found", data=None):
    return create_response(message, status=404, success=False, data=data)

# Wrapper function for 500 Internal Server Error
def server_error_response(message="Internal server error", data=None):
    return create_response(message, status=500, success=False, data=data)

import os
from flask import Flask, request
from flask_cors import CORS

from flask_babel import Babel, _
from flasgger import Swagger

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

# CORS Configuration
'''
Allow all origins for now. This enables cross-origin resource sharing 
(CORS) for all incoming requests. In the future, this should be updated 
to restrict access to specific origins, such as your production site 
and the mobile application.
'''
CORS(app, resources={r"/*": {"origins": "*"}})

# babel time zone and language Configuration
'''
Define the default locale and supported locales for the application.
Specify the languages your application will support here.
'''
app.config['BABEL_DEFAULT_LOCALE'] = 'fr'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr', 'ar']

'''
Initialize the Babel extension to support internationalization (i18n).
This allows the application to respond to different locales and timezones.
'''
babel = Babel(app)

def get_locale():
    '''
    Determine the best matching locale based on the client's request.
    
    Returns:
        str: The best match locale from the supported locales.
    '''
    return request.accept_languages.best_match(['en', 'fr', 'es', 'ar'])

def get_timezone():
    '''
    Define the default timezone for the application.
    
    Returns:
        str: The default timezone.
    '''
    return 'UTC'

'''
Register the locale and timezone selector functions with Babel.
'''
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)

app.config['APP_NAME'] = 'My Flask API'
app.config['APP_VERSION'] = '1.0.0'

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": app.config['APP_NAME'],
        "version": app.config['APP_VERSION'],
        "description": "API documentation for Chat boot API",
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "X-API-KEY",
            "description": "Custom header for API key-based authentication"
        },
        "JWTAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT token using the Bearer scheme. Example: 'Bearer {token}'"
        }
    },
    "parameters": {
        "Accept-Language": {
            "name": "Accept-Language",
            "in": "header",
            "type": "string",
            "enum": ["en", "fr", "ar", "es"],
            "description": "Language preference for the response. Use 'en', 'fr', or 'ar'.",
            "required": False
        }
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, template=swagger_template, config=swagger_config)
# Import and register the healthcare Blueprint from the routes module
'''
Import the `healthcare` function from the `routes` module and register it 
with the Flask application. The `healthcare` function sets up the routes 
defined in the health blueprint so that they can be served by the Flask 
application.
'''
from routes import healthcare, faq
from routes.ai import choose_algorithm
healthcare(app)
faq(app)
choose_algorithm(app)


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

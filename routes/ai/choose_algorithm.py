from flask import Blueprint, request
from data.faq.faq import get_faqs
from config.response import success_response, bad_request_response, server_error_response, not_found_response
from algorithm.simple_vectorizer_model.response_model import get_prediction as svm_model
from algorithm.content_based_filtering.response_model import get_prediction as cbf_model

from util.generate_response import translate_text
chatbot_bp = Blueprint('chatbot', __name__)

algorithm_mapping = {
    'svm_model': svm_model,
    'cbf_model': cbf_model
}

@chatbot_bp.route('/predict', methods=['POST'])
def predict_response():
    """
    Predict chatbot response.
    ---
    tags:
      - Chatbot
    description: Predict a response from the chatbot based on user input using a specified algorithm.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: "The user input for the chatbot."
        schema:
          type: object
          required:
            - message
          properties:
            message:
              type: string
              description: "The message from the user."
              example: "What is the meaning of life?"
      - in: header
        name: Algorithm
        type: string
        required: true
        description: "The algorithm to use for prediction ('svm_model' or 'cbf_model')."
        enum:
          - svm_model
          - cbf_model
      - in: header
        name: Accept-Language
        type: string
        required: true
        description: "The language of the response."
        enum:
          - en
          - fr
          - ar
          - es

    responses:
      200:
        description: Successful response prediction
        schema:
          type: object
          properties:
            message:
              type: string
              description: "The chatbot's response to the user."
      400:
        description: Bad request, message not found
      404:
        description: Model not found
      500:
        description: Internal server error
    """
    language = request.headers.get('Accept-Language', "en")
    data = request.get_json()
    message = data.get('message')
    if not message:
        return bad_request_response("message not found")
    algorithm = request.headers.get('Algorithm')

    model_function = algorithm_mapping.get(algorithm.lower())
    if not model_function:
        return not_found_response("model not created")
    try:
        dataset = get_faqs()
        response = model_function(translate_text(message, "en"), dataset)
        data = translate_text(response, language)
        return success_response("success", data=data)
    except Exception as e:
        return server_error_response()
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
    Endpoint to get a predicted response from the chatbot model based on user input.
    
    Expects a JSON body with a 'message' key. Optionally accepts a 'dataset' key 
    to provide a custom dataset for the chatbot.
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
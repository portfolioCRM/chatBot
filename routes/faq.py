from flask import Blueprint, request
from data.faq.faq import get_faqs, get_faq, add_faq, delete_faq, delete_faqs_by_question
from config.response import success_response, not_found_response, bad_request_response, server_error_response, no_content_response
from data.messages_response.faq_messages import faq_message

faq_bp = Blueprint('faq', __name__)

@faq_bp.route('', methods=['GET'])
def list_faqs():
    """Get all FAQs."""
    try:
        faqs = get_faqs()
        if len(faqs) == 0:
            return no_content_response(message=faq_message["faq"]["list"]["empty"])
        return success_response(message=faq_message["faq"]["list"]["success"], data=faqs)
    except Exception as e:
        return server_error_response(message=str(e))

@faq_bp.route('/<string:question>', methods=['GET'])
def get_faq_route(question):
    """Get a specific FAQ by question."""
    try:
        faq = get_faq(question)
        if faq:
            return success_response(message=faq_message["faq"]["list"]["success"], data=faq)
        return not_found_response(message=faq_message["faq"]["not_found"])
    except Exception as e:
        return server_error_response(message=str(e))

@faq_bp.route('', methods=['POST'])
def add_faq_route():
    """Add a new FAQ."""
    data = request.get_json()
    if 'question' in data and 'response' in data:
        try:
            faq_id = add_faq(data)
            return success_response(message=faq_message["faq"]["create"]["success"], data={'id': faq_id})
        except Exception as e:
            return server_error_response(message=str(e))
    return bad_request_response(message=faq_message["faq"]["create"]["invalid_input"])

@faq_bp.route('/<string:faq_id>', methods=['DELETE'])
def delete_faq_route(faq_id):
    """Delete a FAQ by ID."""
    try:
        deleted_count = delete_faq(faq_id)
        if deleted_count:
            return success_response(message=faq_message["faq"]["delete"]["success"])
        return not_found_response(message=faq_message["faq"]["not_found"])
    except Exception as e:
        return server_error_response(message=str(e))

@faq_bp.route('', methods=['DELETE'])
def delete_faqs_route():
    """Delete FAQs by question."""
    try:
        deleted_count = delete_faqs_by_question()
        if deleted_count > 0 :
            return success_response(message=faq_message["faq"]["delete"]["multiple_success"])
        return not_found_response(message=faq_message["faq"]["not_found"])
    except Exception as e:
        return server_error_response(message=str(e))

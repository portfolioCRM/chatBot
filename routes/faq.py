from flask import Blueprint, request
from data.faq.faq import get_faqs, get_faq, add_faq, delete_faq, delete_faqs_by_question
from config.response import success_response, not_found_response, bad_request_response, server_error_response, no_content_response, created_response
from data.messages_response.faq_messages import faq_message
from util.generate_response import translate_field_in_array, translate_text
from util.convert_input_file import import_faqs_from_csv, import_faqs_from_json
from werkzeug.utils import secure_filename
import os

faq_bp = Blueprint('faq', __name__)

@faq_bp.route('', methods=['GET'])
def get_faq_route():
    """Get a specific FAQ by question."""
    try:
        question = request.args.get("question")
        accept_language = request.headers.get('Accept-Language', 'en')
        target_language = accept_language.split(',')[0].split('-')[0]

        print(str(question))
        if not question:
            faqs = get_faqs()
        else:
            faqs = get_faq(question)
        if len(faqs) == 0:
            return no_content_response(message=faq_message["faq"]["list"]["empty"])
        faqs = translate_field_in_array(faqs, 'response', target_language)
        return success_response(message=faq_message["faq"]["list"]["success"], data=faqs)
    except Exception as e:
        return server_error_response(message=str(e))

@faq_bp.route('', methods=['POST'])
def add_faq_route():
    """Add a new FAQ."""
    data = request.get_json()
    if 'question' in data and 'response' in data:
        try:
            data['response'] = translate_text(data['response'], target_language="en")
            faq = add_faq(data)
            return created_response(message=faq_message["faq"]["create"]["success"], data=faq)
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

@faq_bp.route('/import', methods=['POST'])
def import_faq_route():
    print(str(request.files))
    """Import FAQs from a file (JSON or CSV)."""
    if 'file' not in request.files:
        return bad_request_response(message="No file part in the request.")
    
    file = request.files['file']
    if file.filename == '':
        return bad_request_response(message="No selected file.")
    
    # Secure the filename and save it temporarily
    filename = secure_filename(file.filename)
    file_path = os.path.join('/tmp', filename)
    file.save(file_path)

    try:
        if filename.endswith('.json'):
            faqs = import_faqs_from_json(file_path)
        elif filename.endswith('.csv'):
            faqs = import_faqs_from_csv(file_path)
        else:
            return bad_request_response(message="Unsupported file type. Use a JSON or CSV file.")

        # Save each FAQ to the database
        for faq in faqs:
            if 'question' in faq and 'response' in faq:
                faq['response'] = translate_text(faq['response'], target_language="en")
                add_faq(faq)

        return success_response(message="FAQs imported successfully.", data=faqs)

    except Exception as e:
        return server_error_response(message=str(e))
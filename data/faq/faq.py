from config.connect import get_db
from bson.regex import Regex

def get_faqs():
    """Retrieve all FAQs from the collection."""
    db = get_db()
    collection = db['faq']
    return list(collection.find({}, {'_id': 0}))

def get_faq(question):
    """Retrieve a single FAQ by question."""
    db = get_db()
    collection = db['faq']
    res =  list(collection.find({"question": question}, {'_id': 0}))
    return res

def add_faq(faq):
    """Insert a new FAQ into the collection."""
    db = get_db()
    collection = db['faq']
    result = collection.insert_one(faq)
    faq['_id'] = str(result.inserted_id)
    return faq

def delete_faq(faq_id):
    """Delete a FAQ by ID."""
    db = get_db()
    collection = db['faq']
    result = collection.delete_one({'_id': faq_id})
    return result.deleted_count

def delete_faqs_by_question():
    """Delete FAQs by question."""
    db = get_db()
    collection = db['faq']
    result = collection.delete_many({})
    return result.deleted_count

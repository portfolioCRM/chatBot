from .collect_model import SimpleChatbotModel

def get_prediction(message, dataset=None):
    """
    Initializes the SimpleChatbotModel and predicts the most relevant response 
    for the given message.

    :param message: A string containing the user's message.
    :param dataset: Optional list of dictionaries with 'question' and 'response' keys.
                    If not provided, the model will use the default FAQ dataset.
    :return: A string containing the predicted response.
    """
    chatbot = SimpleChatbotModel(qa_database=dataset) if dataset else SimpleChatbotModel()
    
    response = chatbot.predict(message)
    
    return response
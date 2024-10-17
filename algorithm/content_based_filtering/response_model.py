from .collect_model import ContentBasedFilteringModel

def get_prediction(message, dataset=None):
    """
    Initializes the ContentBasedFilteringModel and recommends the most relevant content 
    for the given message.

    :param message: A string containing the user's message.
    :param content_database: Optional list of strings representing the content items to recommend.
                            If not provided, the model will use a default content dataset.
    :param top_n: The number of recommendations to return.
    :return: A list of strings containing the recommended content.
    """
    model = ContentBasedFilteringModel(qa_database=dataset) if dataset else ContentBasedFilteringModel()
    response = model.recommend(message, top_n=5)
    
    return response

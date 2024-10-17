import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import spacy

nlp = spacy.load('en_core_web_sm')

from data.faq.default_values import init_faq

class SimpleChatbotModel:
    """
    A simple chatbot model that uses cosine similarity to match user queries with predefined FAQ responses.
    """

    def __init__(self, qa_database=init_faq):
        """
        Initializes the chatbot with a question-answer database, prepares vector representations of the questions,
        and sets up text preprocessing components.
        
        :param qa_database: A list of dictionaries containing questions and their corresponding responses.
                            Default is set to the initial FAQ values imported from the module.
        """
        self.qa_database = qa_database
        self.questions = [entry["question"] for entry in self.qa_database]
        self.responses = [entry["response"] for entry in self.qa_database]
        self.vectorizer = CountVectorizer(stop_words='english')
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def preprocess(self, text):
        """
        Preprocesses input text by converting it to lowercase, removing non-alphanumeric characters, splitting
        into words, removing stopwords, and stemming the words.

        :param text: The input string to preprocess.
        :return: A preprocessed string of stemmed words.
        """
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
        doc = nlp(text)
        filtered_words = [
            token.lemma_ for token in doc if not token.is_stop and token.is_alpha
        ]
        return ' '.join(filtered_words)

    def predict(self, message):
        """
        Predicts the most appropriate response for the given user message by calculating cosine similarity
        between the message and stored questions.

        :param message: The user's input message.
        :return: The response corresponding to the most similar question in the database.
        """
        preprocessed_message = self.preprocess(message)
        message_vector = self.vectorizer.transform([preprocessed_message])
        similarities = cosine_similarity(message_vector, self.question_vectors)
        best_match_index = np.argmax(similarities)
        return self.responses[best_match_index]

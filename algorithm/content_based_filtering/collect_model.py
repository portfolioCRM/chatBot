import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from googletrans import Translator
import spacy

nlp = spacy.load('en_core_web_sm')

class ContentBasedFilteringModel:
    """
    A content-based filtering model that recommends items based on user input.
    """

    def __init__(self, qa_database):
        """
        Initializes the model with a content database and prepares vector representations of the content.
        
        :param qa_database: A list of dictionaries containing questions and their corresponding responses.
        """
        self.translator = Translator()
        self.qa_database = qa_database
        self.questions = [self.translator.translate(entry['question'], src='fr', dest='en').text for entry in self.qa_database]
        self.responses = [entry["response"] for entry in qa_database]
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def preprocess(self, text):
        """
        Preprocesses input text by converting it to lowercase, removing non-alphanumeric characters, and lemmatizing.
        
        :param text: The input string to preprocess.
        :return: A preprocessed string of lemmatized words.
        """
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
        doc = nlp(text)
        filtered_words = [
            token.lemma_ for token in doc if not token.is_stop and token.is_alpha
        ]
        return ' '.join(filtered_words)

    def recommend(self, message, top_n=5):
        """
        Recommends the top N items based on the user's input message. Prioritizes exact matches.
        
        :param message: The user's input message.
        :param top_n: The number of recommendations to return.
        :return: A list of recommended items.
        """
        preprocessed_message = self.preprocess(message)
        

        for i, question in enumerate(self.questions):
            preprocessed_question = self.preprocess(question)
            if preprocessed_message == preprocessed_question:
                return [self.questions[i]] + self._get_top_similarities(preprocessed_message, top_n - 1)
        return self._get_top_similarities(preprocessed_message, top_n)

    def _get_top_similarities(self, preprocessed_message, top_n):
        """
        Calculate cosine similarities and return the top N matches.
        
        :param preprocessed_message: The preprocessed message.
        :param top_n: The number of top similar items to return.
        :return: A list of top N recommended questions.
        """
        message_vector = self.vectorizer.transform([preprocessed_message])
        similarities = cosine_similarity(message_vector, self.question_vectors)
        best_match_indices = np.argsort(similarities[0])[::-1][:top_n]
        return [self.questions[i] for i in best_match_indices]
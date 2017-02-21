from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

english_stops = set(stopwords.words('english'))
stemmer = PorterStemmer()
tokenizer = TweetTokenizer()

def preprocess(words):

    # Twitter Tokenizer
    tokens = tokenizer.tokenize(words)
    feature = []
    for token in tokens:

        # Removing stop words
        if len(token) > 2 and token not in english_stops:

            # Stemming using Porter Algorithm
            stemmer.stem(token)

            # Lowercase it
            feature.append(token.lower())

    return feature
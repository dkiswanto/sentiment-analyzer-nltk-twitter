import nltk
from nltk import NaiveBayesClassifier

from preprocessing import preprocess
from sentiment_analysis_nltk import settings
from sentiment_app.analyzer.util import file_handler


def extract_features(document):
    # document == ['love', 'this', 'car']
    document_words = set(document[1])
    features = {}
    features['topic'] = document[0]
    for word in document_words:
        # features['contains(%s)' % word] = (word in document_words)
        features[word] = (word in document_words)

    return features

tweets = file_handler.load_data(settings.BASE_DIR + '/sentiment_app/analyzer/dataset/full-corpus-lite.csv')
data_set = nltk.classify.apply_features(extract_features, tweets)
# training_set = data_set[:len(data_set)/2]
# testing_set = data_set[len(data_set)/2:]

# make classifier
classifier = NaiveBayesClassifier.train(data_set)


def anaylze(tweet):
    # tweet = ("topic", "tweet string post")

    # accuracy & informative features
    # print nltk.classify.accuracy(classifier, testing_set)
    # print classifier.show_most_informative_features(30)
    # print classifier._labels

    # Test Classify
    data = preprocess(tweet[1])
    feature = extract_features((tweet[0], data))

    # print feature
    # print classifier.classify(feature)

    return {"feature": feature, "classify": classifier.classify(feature)}


def get_informative_features():
    most_feature = classifier.show_most_informative_features(10)
    labels = classifier._labels
    print most_feature
    return {"most_feature": most_feature, "labels": labels}
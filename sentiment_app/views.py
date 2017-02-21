from django.http import HttpResponse
from django.shortcuts import render
from analyzer import sentiment

from sentiment_analysis_nltk import settings
from sentiment_app.analyzer.sentiment import get_informative_features
from sentiment_app.analyzer.util import file_handler
from sentiment_app.analyzer.util.twitter_search import get_tweet


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":

        if 'topic-live' in request.POST:
            tweets = get_tweet(request.POST['topic-live'],20)

            output = []
            for tweet in tweets:
                topic = tweet[0]
                text = tweet[1]
                output.append(sentiment.anaylze((topic, text)))

            context = {
                "type": "twitter-live",
                "data": output
            }
            return render(request, 'index.html', context)

        else:
            topic = request.POST['topic']
            tweet = request.POST['tweet']
            context = sentiment.anaylze((topic, tweet))
            return render(request, 'index.html', context)


def dataset(request):
    if 'type' in request.GET:
        if request.GET['type'] == 'raw':
            tweets = file_handler.load_data_unpreprocessed(
                settings.BASE_DIR + '/sentiment_app/analyzer/dataset/full-corpus-lite.csv'
            )
        else:
            tweets = file_handler.load_data(
                settings.BASE_DIR + '/sentiment_app/analyzer/dataset/full-corpus-lite.csv'
            )
    else :
        tweets = {}

    context = { "dataset" : tweets}
    return render(request, 'dataset.html', context)


def information(request):
    context = get_informative_features() #return (most_feature, labels)
    return render(request, 'information.html', context)

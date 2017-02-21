from TwitterSearch import *


def get_tweet(keywords, limit=10, lang='en'):
    try:
        search_order = TwitterSearchOrder()
        search_order.set_keywords(keywords) #keywords search tweet
        search_order.set_language(lang) #language search
        search_order.set_include_entities(False) # and don't give us all those entity information

        # Leaked ini gak masalah udah gak pake twitter lagi soalnya wkwkw
        twitter_search = TwitterSearch(
            consumer_key = '6TjrSq7MTFFUshRthH52R1uVU',
            consumer_secret = '7TpJDGjGvTH7ABZ2KTupWZBl9mg30AykULHHrZBAwy3Oejd2le',
            access_token = '2501651690-JfLarQjjtxGcjW0GA62j9c2sfzfl3lpH06SZGtV',
            access_token_secret = 'lSr4jtSrWMt9atxNMoRkw3lWTEbYDRT6Jy8b1PzJceucq'
         )

         # get tweet proccess
        count = 0
        tweets = []
        for tweet in twitter_search.search_tweets_iterable(search_order):

            # content tweet
            # tweet['text']

            # tweets.append('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))
            tweets.append(tweet['text'])

            # print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            if count == limit:
                break
            count += 1

        return tweets

    except TwitterSearchException as e:
        print(e)
        return None

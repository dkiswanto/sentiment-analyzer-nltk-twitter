## Simple Sentiment Analyzer with NLTK for Twitter

### Overview

### Tech Stack
* Python 2.7
* NLTK (Natural Language Processing Toolkit) 3.2.2
* TwitterSearch

### Web App Tech
* Django 1.9.11
* Semantic UI
* JQuery

### Step
#### Pre-processing : 
* Tokenization

Using : http://www.nltk.org/_modules/nltk/tokenize/casual.html#TweetTokenizer
```
Example : 
>>> from nltk.tokenize import TweetTokenizer
>>> tweet = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
>>> TwitterTokenizer.tokenize(tweet)
['This', 'is', 'a', 'cooool', '#dummysmiley', ':', ':-)', ':-P', '<3', 'and', 'some', 'arrows', '<', '>', '->', '<--']
```

* removing stop word

```
>>> from nltk.corpus import stopwords
>>> english_stops = set(stopwords.words('english'))
>>> "is" in english_stops
True
>>> "ganteng" in english_stops
False
```

* Stemming Porter Algorithm

Algorithm : http://snowball.tartarus.org/algorithms/porter/stemmer.html

Simple Explanation : 

**1.a** 

$sses -> $ss | care**sses** -> care**ss**

$ies -> $i | poni**es** -> poni

$ss -> $ss | care**ss** -> care**ss**

$s -> $ | cat**s** -> cat

**1.b**

$(verb)-ing -> $(verb) | walk**ing** -> walk

$(verb)-ed -> $(verb) | walk**ed** -> walk

**2.(for long stems)**

$ational -> $ate | rel**ational** -> relate

$izer -> $ize | digit**izer** -> digitize

**3.(for long stems)**

$al -> $ | reviv**al** -> reviv

$able -> $ | adjust**able** -> adjust


* lower_case
using python built in .lower() method

```
>>> "TwitterPostTweet".lower()
"twitterposttweet"
```

#### Extraksi Feature

- Using Binary term, mirip term frequency, cuman ngitung ada atau tidak doang.

```
>>> tweet = ["apple", "product", "best", "use", "apple", "forever"]
>>> "extraction_feature(tweet)
{"apple": True, "product": True, "best": True, "forever": True}
```

#### Classifier
- Using NaiveBayesClassifier (NLTK),


### Screenshoot
![Alt text](/readme_files/screenshot1.png?raw=true "Optional Title")
![Alt text](/readme_files/screenshot2.png?raw=true "Optional Title")

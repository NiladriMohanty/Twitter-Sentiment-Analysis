import sys
import json

# Make a dictionary from the sentiment words file. Terms are keys and sentiment scores are values.
def senti_score(sent_file):
    scores = {}
    for line in sent_file.readlines():
        term, score = line.split("\t")
        scores[term] = int(score)
    #print scores    
    return scores

# Parsing tweet file

def parse_tweet(twitter_file):
    tweets = []
    for line in twitter_file.readlines():
        tweet = json.loads(line)
        #print tweet
        if "text" in tweet.keys():
            tweets.append(tweet["text"])
    return tweets

'''def parse_tweet(tweet_file):
    twitters = []
    for line in tweet_file:
        tweet = json.loads(line)
        if 'id' in tweet.keys() and 'text' in tweet.keys():
            tweet_text = tweet['text'].encode('utf-8')
            twitters.append(tweet_text)
    return twitters'''

# Print the sentiment score of each line of tweet
def tweet_scores(tweets, scores):
    for tweet in tweets:
        tweet_score = 0
        for word in tweet.split():
            if word in scores.keys():
                tweet_score += scores[word]
        print float(tweet_score)
        '''sums = 0
        sums = sum(scores.get(w,0) for w in tweet.split())
        print sums'''

# Main body
def main():
    sent_file = open(sys.argv[1])
#    twitter_file = sys.argv[2]
    twitter_file = open(sys.argv[2])

    scores = senti_score(sent_file)
    tweets= parse_tweet(twitter_file)

    tweet_scores(tweets, scores)


if __name__ == '__main__':
	main()




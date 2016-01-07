import sys
import json

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
def tweet_scores(tweets):  
    all_terms = {}
    for tweet in tweets:
        for word in tweet.split():
            all_terms[word] = all_terms[word] + 1 if word in all_terms.keys() else 1

    all_freq = sum(all_terms.values())

    for term in all_terms:
        print '%s %f' %(term,all_terms[term]/all_freq)

        #print float(tweet_score)
        '''sums = 0
        sums = sum(scores.get(w,0) for w in tweet.split())
        print sums'''

# Main body
def main():

    twitter_file = open(sys.argv[1])

    tweets= parse_tweet(twitter_file)

    tweet_scores(tweets)


if __name__ == '__main__':
    main()




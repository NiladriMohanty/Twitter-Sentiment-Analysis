import sys
import json
import collections

def top_tags(tweet_file):
    hashtags = collections.defaultdict(lambda:0.0)
    
    for line in tweet_file:
        response = json.loads(line)
        if 'entities' in response and response['entities'] != None:
            for tag in response['entities']['hashtags']:
                hashtags[tag['text']] += 1

    top_tags = sorted(hashtags.items(),key = lambda x:x[1],reverse = True)[:10]

    for tag in top_tags:
        print '%s %.1f' %(tag[0],tag[1])

def main():
    tweet_file = open(sys.argv[1])
    top_tags(tweet_file)

if __name__ == '__main__':
    main()
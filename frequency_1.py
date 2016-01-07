
import sys
import json
import collections

def hw(tweet_file):
    term_frequency = collections.defaultdict(lambda:0.0)
    for line in tweet_file:
        response = json.loads(line)
        if 'text' in response:
            text = response['text']
            terms = text.strip().replace('\n','').split(' ')
            for term in terms:
                term_frequency[term] += 1.0
    all_frequency = sum(term_frequency.values())
    for term in term_frequency:
        print '%s %f' %(term,term_frequency[term]/all_frequency)

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
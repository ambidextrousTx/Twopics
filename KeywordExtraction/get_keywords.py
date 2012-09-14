"""
Use the winnowed surface forms and the cleaned tweets
Generate keywords for all tweets
"""
import sys

def error():
    print 'get_keywords.py: ERROR: what are the tweet and surface forms files?'
    print 'Exiting now.'
    sys.exit()

def get_surface_forms(winnowed_sf_file):
    surface_forms = {}
    with open(winnowed_sf_file, 'r') as fh:
        for line in fh:
            # Using the newly discovered setdefault()
            surface_forms.setdefault(line.strip(), 1)
    return surface_forms

def get_keywords(tweets_file, winnowed_sf_file):
    surface_forms = get_surface_forms(winnowed_sf_file)
    f_out = open('all_tweets.clean.keywords.txt', 'w')
    with open(tweets_file, 'r') as f_in:
        for line in f_in:
            line = line.strip().split()
            id = line[0]
            tweet_words = line[2:]
            tweet_keywords = [w for w in tweet_words if w in surface_forms]
            tweet = ' '.join(tweet_keywords)
            f_out.write('{0} :: {1}\n'.format(id, tweet))
    f_out.close()

def main():
    if len(sys.argv) != 3:
        error()
    get_keywords(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()

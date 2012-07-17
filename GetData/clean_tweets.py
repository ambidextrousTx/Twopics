"""
Cleaning and preprocessing the ~1300 tweets
- get text only
- assign ID to each text
"""
import re
import sys

def error():
    print 'cleanTweets.py: ERROR: Please provide the JSON files you want to clean'
    print 'Exiting now.'
    sys.exit()

def get_all_text(files):
    allTweets = []
    for f in files:
        print 'Processing %s' % f
        with open(f, 'r') as fHandle:
            # string concatenation over a loop is extremely inefficient
            # use join instead
            lines = ''.join(fHandle.read().strip())
            chunks = lines.split('created_at')
            print 'Found {0} chunks'.format(len(chunks))
            for chunk in chunks:
                try:
                    pattern = re.search(r'\"text\":\"(.*?)\"', chunk)
                    tweet = pattern.group(1)
                    allTweets.append(tweet)
                except AttributeError:
                    pass

    fHandle = open('allTweets.txt', 'w')
    counter = 0
    for tweet in allTweets:
        fHandle.write('{0} :: {1}\n'.format(counter, tweet))
        counter += 1

def main():
    if len(sys.argv) < 2:
        error()
    files = [f for f in sys.argv if 'cleanTweets' not in f]
    get_all_text(files)

if __name__ == '__main__':
    main()

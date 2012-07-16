"""
Cleaning and preprocessing the ~1300 tweets
- get text only
- assign ID to each text
- remove stop words
- part of speech tagging, keep only certain types of keywords(lexical categories)
- do pairwise active context (web query count based similarity)
- pick top 4 context words for each keyword
- produce (id, [(keyword, [context]) ...]) tuples for each tweet
"""
import sys

def error():
    print 'cleanTweets.py: ERROR: Please provide the JSON files you want to clean'
    print 'Exiting now.'
    sys.exit()

def getAllText(files):
    

def main():
    if len(sys.argv) < 2:
        error()
    

if __name__ == '__main__':
    main()

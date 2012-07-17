"""
Work on an aggregate of all collected tweets 
Remove stop words (from a separate file)
    - part of speech tagging will only take desired categories
    - but helps to remove some 
    - also helps to remove RT, MT, @, #, and hyperlinks
"""
import re
import sys

def error():
    print 'aggregate_clean.py: ERROR: please provide a comma separated stopwords file, followed by the filename containing all tweets'
    print 'Exiting now.'
    sys.exit()

def read_stop_words(stop_words_file):
    stop_words = []
    with open(stop_words_file, 'r') as fh:
        contents = fh.read().split(',')
        for c in contents:
            # Cannot use extend, append is fine
            stop_words.append(c)
    return stop_words

def clean_twitter_stop_words(line):
    twitter_stopwords = ['RT', 'MT', '@', '#']
    
    

def clean_stop_words(stop_words_file, tweets_file):
    # Just need to read from the input file once
    # and call the corresponding functions on each line
    out_file = open('all_tweets.clean.txt', 'w')
    stop_words = read_stop_words(stop_words_file)
    
    with open(tweets_file, 'r') as input_file:
        counter = 0
        for line in input_file:
            line = line.strip().split(' ')[2:]
            line = [w for w in line if w not in stop_words]
            line = ' '.join(line)
            line = clean_twitter_stop_words(line)
            out_file.write(line + '\n')

    out_file.close()

def main():
    if len(sys.argv) != 3:  
        error()
    stop_words_file, tweets_file = sys.argv[1], sys.argv[2]
    clean_stop_words(stop_words_file, tweets_file)

if __name__ == '__main__':
    main()


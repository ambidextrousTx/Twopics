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

def clean_stop_words(stop_words_file, tweets_file):
    # Just need to read from the input file once
    out_file = open('all_tweets.clean.txt', 'w')
    stop_words = read_stop_words(stop_words_file)
    twitter_stopwords = ['RT', 'MT', '@', '#']
    
    with open(tweets_file, 'r') as input_file:
        counter = 0
        for line in input_file:
            line = line.strip().split(' ')[2:]
            # Keeping the original letter cases from the tweets
            # We don't want to miss out on abbreviations if any
            line = [w for w in line if w not in stop_words and w not in twitter_stopwords]
            line = ' '.join(line)
            hyperlink = re.compile(r'\bhttp:\\/\\/.*\\/.+?\b')
            twitter_entities = re.compile(r'@|#')
            html_ent = re.compile(r'&amp;')
            punctuation = re.compile(r',|\.|"|\'|\\|/|\||!|\?|:|')
            alphanums = re.compile(r'\w+\d|\d+\w')

            # not the best or perfect, but hey
            line = re.sub(hyperlink, '', line)
            line = re.sub(twitter_entities, '', line)
            line = re.sub(punctuation, '', line)
            line = re.sub(alphanums, '', line)
            line = re.sub(html_ent, '', line)
            out_file.write('{0} :: {1}\n'.format(counter, line))
            counter += 1

    out_file.close()

def main():
    if len(sys.argv) != 3:  
        error()
    stop_words_file, tweets_file = sys.argv[1], sys.argv[2]
    clean_stop_words(stop_words_file, tweets_file)

if __name__ == '__main__':
    main()


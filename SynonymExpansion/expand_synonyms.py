"""
Use Oxford Thesaurus to get synonyms for all words (w) possible
Use UNTIndexer to get top n (4) synonyms for each w
Add the synonyms to the overall tweet
"""
import sys
from xml.dom import minidom

def error():
    print 'Usage: supply thesaurus_xml n all_tweets_file'
    print 'Quitting now'
    sys.exit()

find_words_w_syns(line, thesaurus, n):
    syns = []
    

def process(thesaurus, n, tweets_file):
    with open(tweets_file, 'r') as twf:
        for line in twf:
            line = line.strip().split(' :: ')[1]
            words_w_syns = find_words_w_syns(line, thesaurus, n)
            

def main():
    if len(sys.args) != 4:
        error()
    thesaurus = sys.argv[1]
    n = sys.argv[2]
    tweets_file = sys.argv[3]

    process(thesaurus, n, tweets_file)

if __name__ == '__main__':
    main()



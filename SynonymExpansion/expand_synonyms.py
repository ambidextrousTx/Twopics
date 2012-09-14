"""
Ambidextrous
Sep, 2012

Use Oxford Thesaurus to get synonyms for all words (w) possible
Use UNTIndexer to get top n (4) synonyms for each w
Add the synonyms to the overall tweet

Dependencies: Oxford XML, NLTK
"""
import sys
from nltk import word_tokenize, pos_tag
from xml.dom import minidom

def error():
    print 'Usage: supply thesaurus_xml n all_tweets_file'
    print 'Quitting now'
    sys.exit()

def get_sanitized_pos(penn_pos):
    sanitized = ''
    if 'NN' in penn_pos:
        sanitized = 'n'
    if 'RB' in penn_pos:
        sanitized = 'r'
    if 'JJ' in penn_pos:
        sanitized = 'a'
    if 'VB' in penn_pos:
        sanitized = 'v'
    return sanitized

def explore_thesaurus_for_lexelt(word, pos):

def find_words_w_syns(line, thesaurus, n):
    syns = []
    xml_thesaurus = minidom.parse(thesaurus)
    words = line.split()
    words_pos = pos_tag(word_tokenize(words))
    for w_p in words_pos:
        pos = get_sanitized_pos(w_p[1])
        word = w_p[0]
        syns = explore_thesaurus_for_lexelt(word, pos)

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



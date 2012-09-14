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

def explore_thesaurus_for_lexelt(word, pos, all_lexsub_elements):
    # childNodes[1] and [3] are word and pos
    # Derive one lexelt that matches the lexelt(word, pos)
    # The lexelt returned should and will be a single node
    lexelt = filter( (lambda L: L.childNodes[1].firstChild.data == word and L.childNodes[3].firstChild.data == pos), all_lexsub_elements)[0]
    syns = []
    senses = lexelt.getElementsByTagName('sense')
    for sense in senses:    
        synonyms = sense.getElementsByTagName('synonyms')
        for syn in synonyms:
            if ' ' not in syn:
                syns.append(syn.firstChild.data)
            
    return syns

def get_all_synonyms(line, xml_thesaurus):
    syns = []
    all_lexsub_elements = xml_thesaurus.getElementsByTagName('lexelt')
    words = line.split()
    words_pos = pos_tag(word_tokenize(words))
    for w_p in words_pos:
        pos = get_sanitized_pos(w_p[1])
        word = w_p[0]
        syns = explore_thesaurus_for_lexelt(word, pos, all_lexsub_elements)

def process(thesaurus, n, tweets_file):
    xml_thesaurus = minidom.parse(thesaurus)
    with open(tweets_file, 'r') as twf:
        for line in twf:
            line = line.strip().split(' :: ')[1]
            all_syns = get_all_synonyms(line, xml_thesaurus)

def main():
    if len(sys.args) != 4:
        error()
    thesaurus = sys.argv[1]
    n = sys.argv[2]
    tweets_file = sys.argv[3]

    process(thesaurus, n, tweets_file)

if __name__ == '__main__':
    main()



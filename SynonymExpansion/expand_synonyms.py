"""
Ambidextrous
Sep, 2012

Use Oxford Thesaurus to get synonyms for all words (w) possible
    (that are present in the tweets themselves)
Create - Oxford database to feed to SaLSA
Create - SaLSA input files

Dependencies: Oxford XML, NLTK
"""
import sys
import shelve
from collections import defaultdict
from nltk import data
from nltk import word_tokenize, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from xml.dom import minidom

def error():
    print 'Usage: supply thesaurus_xml all_tweets_file'
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

def weed_out_lexelts(tweets_file):
    lexelts = []
    WNL = WordNetLemmatizer()
    with open(tweets_file, 'r') as twh:
        for line in twh:    
            line = line.strip().split(' :: ')[1]
            lexelts_temp = []
            try:
                lexelts_temp = pos_tag(word_tokenize(line))
            except TypeError:
                print line

            # Get sanitized parts of speech, not the Treebank style
            # Tuples are immutable, need to make a new single-tuple list 
            for w, p in lexelts_temp:
                new_p = get_sanitized_pos(p)
                new_w = w
                try: 
                    new_w = WNL.lemmatize(w, new_p)
                except KeyError:
                    pass
                lexelts.extend([(new_w, new_p)])
    
    lexelts = list(set(lexelts))
    print lexelts
    return lexelts

def explore_thesaurus_for_lexelt(word, pos, all_lexsub_elements):
    # childNodes[1] and [3] are word and pos
    # Derive one lexelt that matches the lexelt(word, pos)
    # The lexelt returned should and will be a single node

    syns = []
    try:
        lexelt = filter( (lambda L: L.childNodes[1].firstChild.data == word and L.childNodes[3].firstChild.data == pos), all_lexsub_elements)[0]
        senses = lexelt.getElementsByTagName('sense')
        for sense in senses:    
            synonyms = sense.getElementsByTagName('synonyms')
            for syn in synonyms:
                all_syns = syn.firstChild.data
                all_syns = all_syns.replace(';', ',')
                all_syns = all_syns.strip('.') # Get rid of the trailing .
                all_syns = all_syns.split(', ')
                for each_syn in all_syns:
                    if ' ' not in each_syn:
                        syns.append(each_syn)
    except IndexError:
        pass
    return syns

def prepare_syndb(thesaurus, lexelts):
    xml_thesaurus = minidom.parse(thesaurus)
    pers_obj = shelve.open('oxf.syns.db')
    temp_obj = defaultdict(dict)
    all_lexsub_elements = xml_thesaurus.getElementsByTagName('lexelt')
    for word, pos in lexelts:
        syns = explore_thesaurus_for_lexelt(word, pos, all_lexsub_elements)
        temp_obj[word][pos] = syns

    pers_obj['1'] = temp_obj
    pers_obj.close()

def prepare_SaLSA_input_file(tweets_file):
    # IDs are assigned sequentially to the tweets
    # So they should match what we have later in the
    # aggregated tweets

    # Use the NLTK sentence segmenter to do it multiple times
    # for multiple sentences in the tweet
    sent_tokenizer = data.load('tokenizers/punkt/english.pickle')
    file_id = 0
    with open(tweets_file, 'r') as twh:
        for line in twh:
            line = line.strip().split(' :: ')[1]
            fho = open('SaLSAInputFiles/{0}'.format(file_id), 'w')
            sents = sent_tokenizer.tokenize(line)
            for sent in sents:
                sent_array = sent.split(' ')
                for i in xrange(0, len(sent_array)):
                    temp_sent = ' '.join(sent_array[:i]) + ' <head>' + sent_array[i] + '</head> ' + ' '.join(sent_array[i+1:])
                    fho.write(temp_sent + '\n')
            fho.close()
            file_id += 1

def main():
    if len(sys.argv) != 3:
        error()
    thesaurus = sys.argv[1]
    tweets_file = sys.argv[2]

    # List of tuples
    print 'Getting all tuples of the form (word, part of speech) from the tweets file'
    lexelts = weed_out_lexelts(tweets_file)
    print 'Done'
    # Persistent object from Oxford
    print 'Preparing the Oxford synonyms database'
    prepare_syndb(thesaurus, lexelts)
    print 'Done'
    # Each word is a head word - multiple files
#   print 'Preparing the SaLSA input files'
#   prepare_SaLSA_input_file(tweets_file)
#   print 'Done'

if __name__ == '__main__':
    main()

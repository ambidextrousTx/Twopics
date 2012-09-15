"""
Ambidextrous
Sep 2012

Wrapper around SaLSA to get top n 
synonyms for all words in the tweets
using the Oxford thesaurus

Input: SaLSA input files: 1400
Output from SaLSA: bla bla bla, then 
All synonyms scores = [(score, 'word'), ...] - reverse ranked
"""
import sys
import commands

def complain():
    print 'Usage: supply path_to_input_files all_tweets_file'
    print 'Quitting now'
    sys.exit()

def run_salsa(path_to_input_files): 
    

def main():
    if len(sys.argv != 3):
        complain()
    path_to_input_files = sys.argv[1]
    all_tweets_file = sys.argv[2]

    # Get a hashmap of the extensions keyed on the tweet / file ID
    extensions = run_salsa(path_to_input_files)
    merge_and_extend(all_tweets_file, extensions)

if __name__ == '__main__':
    main()



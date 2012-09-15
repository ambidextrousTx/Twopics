"""
Ambidextrous
Sep 2012

Wrapper around SaLSA to get top n 
synonyms for all words in the tweets
using the Oxford thesaurus

Input: SaLSA input files: 1400
Output from SaLSA: bla bla bla, then 
All synonyms scores = [(score, 'word'), ...] - reverse ranked

n = 4
"""
import sys
import commands
from collections import defaultdict

def complain():
    print 'Usage: supply path_to_input_files all_tweets_file'
    print 'Quitting now'
    sys.exit()

def run_salsa(path_to_input_files): 
    files = os.listdir(path_to_input_files)
    extensions = defaultdict(dict)
    for f in files:
        print 'Processing ', f
        out = commands.getstatusoutput('python salsa.py {0}/{1} > temp.out.SaLSA.txt'.format(path_to_input_files, f))
        all_lines = []
        with open('temp.out.SaLSA.txt', 'r') as fho:
            for line in fho:
                line = line.strip()
                all_lines.append(line)

        output_lines = filter( (lambda L: 'All synonym scores' in L), all_lines)
        for out_line in output_lines:
            words_of_interest = out_line.split(' = ')[1]
        

        extensions[f] = # all words found
        
        
            


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



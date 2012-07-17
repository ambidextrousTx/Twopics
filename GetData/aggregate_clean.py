"""
Aggregate all collected tweets 
Remove stop words (from a separate file)
    - part of speech tagging will only take desired categories
    - but helps to remove some 
    - also helps to remove RT, MT, @, #, and hyperlinks
"""
import sys

def error():
    print 'aggregate_clean.py: ERROR: please provide a comma separated stopwords file'
    print 'Exiting now.'
    sys.exit()

def main():
    if len(sys.argv) != 2:  
        error()
    clean_stop_words()
    
    

if __name__ == '__main__':
    main()


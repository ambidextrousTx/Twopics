"""
Twopics
Part [1]
Get 1000 tweets related to
    #olympics
    #londonolympics
    #2012olympics
using the Twitter API

Original plan: Use REST API (hangs)
Final plan: use SEARCH API with URL-encoding (%23 for # etc)
"""
import sys
import commands

BASEQUERY = "http://search.twitter.com/search.json?q="
queries = ['%23olympics', '%232012olympics', '%23londonolympics', 'olympics', 'london%20olympics']

def callTwitterAPI():
    counter = 1
    for query in queries:
        this_query = BASEQUERY + query
        commands.getstatusoutput('wget -O %d.json "%s"' % (counter, this_query))
        counter += 1

def main():
    callTwitterAPI()

if __name__ == '__main__':
    main()

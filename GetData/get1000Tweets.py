"""
Twopics
Part [1]
Get 1000 tweets related to
    #olympics
    #londonolympics
    #2012olympics
using the Twitter API

Refer to the README of Twitter.TAP by Rada
"""
import sys
import commands

def error():
    print 'get1000Tweets.py: ERROR. Please provide the script to execute and the name of the query file'
    print 'Exiting now.'
    sys.exit()

def callTwitterAPI(exec_file, query_file):
    commands.getstatusoutput('perl %s %s' % (exec_file, query_file))

def main():
    if len(sys.argv) != 3:
        error()
    callTwitterAPI(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()

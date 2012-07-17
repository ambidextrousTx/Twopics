"""
Automate tweet collection and cleaning
Start from the 5th iteration; do about 20
Provide a delay (sleep) of 30 seconds in between
"""
import time
import commands

# dynamic range; lazily compute on the fly
for i in xrange(5, 20):
    commands.getstatusoutput('python get_1000_tweets.py')
    commands.getstatusoutput('python clean_tweets.py 1.json 2.json 3.json 4.json 5.json')
    commands.getstatusoutput('mv allTweets.txt collected_tweets/allTweets_{0}.txt'.format(i))
    time.sleep(60)
    print 'Dealt with %d' % i
    

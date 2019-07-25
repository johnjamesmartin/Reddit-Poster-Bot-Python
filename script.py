import praw
import re
import time

reddit = praw.Reddit(client_id='', client_secret='', user_agent='<PLATFORM:APPNAME:0.0.1(by /u/REDDITUSERNAME)>', username='REDDITUSERNAME', password='REDDITPASSWORD')

subreddits = ['programmerhumor', 'funny']
pos = 0

title="Remember to hug a programmer"
url="http://worklad.co.uk/wp-content/uploads/2015/01/494692340292596844.jpg"

def post():
	global subreddits
	global pos

	subreddit = reddit.subreddit(subreddits[pos])
	subreddit.submit(title, url=url)

	pos = pos + 1

	if (pos >= len(subreddits) - 1):
		post()
	else:
		print "Done"
	post()

post()
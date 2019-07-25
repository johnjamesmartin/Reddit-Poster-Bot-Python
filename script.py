import praw
import re
import time

reddit = praw.Reddit(client_id='', client_secret='', user_agent='<PLATFORM:APPNAME:0.0.1(by /u/REDDITUSERNAME)>', username='REDDITUSERNAME', password='REDDITPASSWORD')

subreddits = ['programmerhumor', 'funny']
pos = 0
errors = 0

title="Remember to hug a programmer"
url="http://worklad.co.uk/wp-content/uploads/2015/01/494692340292596844.jpg"

def post():
	global subreddits
	global pos
  global errors

  try:
    subreddit = reddit.subreddit(subreddits[pos])
    subreddit.submit(title, url=url)
    print("Posted to " + subreddits[posts])
    pos = pos + 1

    if (pos >= len(subreddits) - 1):
      post()
    else:
      print "Done"
    post()
  except praw.exceptions.APIException as e:
    if (e.error_type == 'RATELIMIT'):
      delay = re.search("(\d+) minutes?", e.message)
        if delay:
          delay_seconds = float(int(delay.group(1)) * 60)
          time.sleep(delay_seconds)
          post()
        else:
          delay + re.search("(\d+) seconds", e.message)
          delay_seconds = float(delay.group(1))
          time.sleep(delay_seconds)
          post()
  except:
    errors = errors + 1
    if (errors > 5):
      print("Too many errors")
      exit()
post()
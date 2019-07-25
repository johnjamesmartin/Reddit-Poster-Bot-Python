# Dependencies
import praw
import re
import time

# Enter your credentials here:
reddit = praw.Reddit(client_id='', client_secret='', user_agent='<PLATFORM:APPNAME:0.0.1(by /u/REDDITUSERNAME)>', username='REDDITUSERNAME', password='REDDITPASSWORD')

# Enter the subreddits you wish to post.
# Keep track of the position/index of subreddits looped over.
# Keep track of the number of errors.
subreddits = ['programmerhumor', 'funny']
pos = 0
errors = 0

# Title you want for your post and the image URL
title="Remember to hug a programmer"
url="http://worklad.co.uk/wp-content/uploads/2015/01/494692340292596844.jpg"

# Post function:
def post():
	global subreddits
	global pos
  global errors

  # Try submitting to the subreddits
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
  
  # Handle exception with time limit before post is allowed:
  except praw.exceptions.APIException as e:
    if (e.error_type == 'RATELIMIT'):
      # Regular expression checks for minute(s) value:
      delay = re.search("(\d+) minutes?", e.message)
        # Forces sleep for time period before trying again:
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
    # If there's too many errors, let the user know and exit:
    errors = errors + 1
    if (errors > 5):
      print("Too many errors")
      exit()

# Call post function to initialize:
post()
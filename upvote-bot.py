import os, sys, time
import praw
from praw.objects import Redditor, Submission

__author__ = 'bzb'
__version__ = '0.1'

"""Upvotes (or downvotes) all comments and submissions by redditor target.
Change commented lines to specify user and upvote/downvote.

python upvote-bot.py target

"""

class RedditBot(object):

	def __init__(self, username, password, target):
		self.api = praw.Reddit(user_agent='BzbBot')
		self.api.login(username, password)
		self.count = 0
		self.redditor = self.api.get_redditor(target, fetch=False)

	def run(self):
		for post in self.redditor.get_comments(limit=None):
			try:
				post.upvote() # Change this to post.downvote() if you want to downvote instead
				print "Upvoted: %s" %post.__unicode__()
				self.count += 1
			except:
				exception('Cannot upvote!')
			time.sleep(2) # Following reddit's rules

		for submitted in self.redditor.get_submitted(limit=None):
			try:
				submitted.upvote() # Change this to post.downvote() if you want to downvote instead
				print "Upvoted: %s" %submitted.__unicode__()
				self.count += 1
			except:
				exception('Cannot upvote!')
			time.sleep(2) # Following reddit's rules

def main(target):
	bot = RedditBot('username', 'password', target) # Specify username and password
	try:
		bot.run()
	except:
		raise
	finally:
		print('Done!  Upvoted %d submissions/comments!') %bot.count

	return 0

if __name__ == '__main__':
	target = sys.argv[-1]
	sys.exit(main(target))
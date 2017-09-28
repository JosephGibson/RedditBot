import praw
import config
import time
import logging


# A global blank comment list
comment_list = []


# The bot login handler 

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "A test bot tests stuff v0.1")
	return r
	print ("Login = Success")




# The function of the bot

def run_bot(r):
	for comment in r.subreddit('test').comments(limit=10):
		# To do here 
		
		




logger = logging.getLogger('reddit_crawler')
hdlr = logging.FileHandler('BotLog.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

#Ensure that the bot is logged in 

r = bot_login() 			
#while True:
run_bot(r)





import praw
import config
import time



# A global blank comment list



# The bot login handler 

def bot_login():
	print("logging in to reddit...")
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
		if "dog" in comment.body and comment.id not in comment_list:
			print("Dog comment found")
			comment.reply("doggies found")
			comment_list.append(comment.id)

		
		






#Ensure that the bot is logged in 

r = bot_login() 
comment_list = []

while True:
		
	run_bot(r, comment_list)




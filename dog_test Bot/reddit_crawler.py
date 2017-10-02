import praw
import config
import time
import os


# A global blank comment list



# The bot login handler 

def bot_login():
	print("logging in to reddit...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "A test bot tests stuff v0.1")
	print ("Login = Success")
	return r



# The function of the bot

def run_bot(r, comment_list):
	for comment in r.subreddit('test').comments(limit=40):
		if "dog" in comment.body or "test" in comment.body and comment.id not in comment_list and comment.author != r.user.me:
			print("Dog comment found at : " + comment.id)
			# comment.reply("doggies found [Here] https://i.imgur.com/TUQvrsV.jpg ")
			comment_list.append(comment.id)
			print (comment_list)
			with  open("comments_replied.txt", "a") as f:
				f.write(comment_id + "\n")
		#print("sleeping for 10 seconds")
		#time.sleep(10)


def get_comments():
	if not os.path.isfile("comments_replied.txt"):
		comments_replied = []
	else:
		with open("comments_replied.txt", "r") as f:
			comments_replied = f.read()
			comments_replied = comments_replied.split("\n")
	return comments_replied 




# Ensure that the bot is logged in 

r = bot_login() 
comment_list = get_comments()

while True:
	run_bot(r, comment_list)




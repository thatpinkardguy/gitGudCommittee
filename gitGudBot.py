
import praw
import json
from pprint import pprint

def authenticate(config):

	#authenticate with Reddit
	print("Attempting to authenticate....")
	reddit = praw.Reddit(client_id=config["client_id"], client_secret=config["client_secret"], username=config["username"],password=config["password"],user_agent=config["user_agent"])

	#print out our user name
	print("Authenicated!")
	#print(reddit.user.me())

	#return the reddit object
	return reddit


def getComments(reddit):

	#Our subreddit Name
	subName = 'test'

	#number of comments to pull
	commentsLimit = 25

	print("Getting "+ str(commentsLimit) +  " comments in subReddit: " + subName)

	#get the subreddit obj
	subReddit = reddit.subreddit(subName)

	#pull the comments
	comments = subReddit.comments(limit = commentsLimit)

	#loop through them and print the author's name
	for comment in comments:
		print(comment.author)


def getConfigData():

	print('getting configuration data')

	with open('botCredentials.json') as data_file:
    		data = json.load(data_file)
	pprint(data)

	return data

#get_comments(reddit)
config = getConfigData()
reddit = authenticate(config)
getComments(reddit)


import praw
import json
from pprint import pprint
import configparser as ConfigParser
#from pydash import _

def authenticate(config):

	#authenticate with Reddit

	client_id = config.get("Credentials", "client_secret")
	client_secret = config.get("Credentials", "client_secret")
	username = config.get("Credentials", "username")
	password = config.get("Credentials", "password")
	user_agent = config.get("Credentials", "user_agent")


	print("Attempting to authenticate....")
	#reddit = praw.Reddit(client_id=config["client_id"],
			#client_secret=config["client_secret"],
			#username=config["username"],
			#password=config["password"],
			#user_agent=config["user_agent"])

	reddit = praw.Reddit(client_id=client_id,
			client_secret=client_secret,
			username=username,
			password=password,
			user_agent=user_agent)

	#trying to get pydash to work
	#need to get _.map functioning like its js counterpart
	#reddit = praw.Reddit(client_id=_.map(config,"client_id"), client_secret=_.map(config,"client_secret"), username=_.map(config,"username"),password=_.map(config,"password"),user_agent=_.map(config,"user_agent"))

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
	if comments.yielded != 0 :
		for comment in comments:
			print(comment.author)
	
	else:
		print('query resulted in no comments')

def getConfigData():

	print('getting configuration data')

	with open('botCredentials.json') as data_file:
    		data = json.load(data_file)
	#pprint(data)
	

	return data


def parseConfig():
	config = ConfigParser.RawConfigParser()
	config.read("botSettings.cfg")

	#print(config.get("Credentials", "client_id"))
	return config

config = parseConfig()

#get_comments(reddit)
#config = getConfigData()
reddit = authenticate(config)
getComments(reddit)
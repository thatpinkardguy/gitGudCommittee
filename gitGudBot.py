
import praw


def authenticate():

	print("Attempting to authenticate....")
	reddit = praw.Reddit(client_id='BfFQSyA5YBU6BQ', client_secret='qpNXjEygoorolN5IxUta0Vm9_SE', password='Apple300!', user_agent='testing connection to Reddit', username='thatpinkardguy')

	print("Authenicated as:")
	print(reddit.user.me())

	return reddit


def get_comments(reddit):

	subName = 'test'
	commentsLimit = 25

	print("Getting "+ str(commentsLimit) +  " comments in subReddit: " + subName)

	subReddit = reddit.subreddit(subName)

	comments = subReddit.comments(limit = commentsLimit)

	for comment in comments:
		print(comment.author)

#	property_names=[p for p in dir(comments) if isinstance(getattr(comments,p),property)]

#	for p in property_names :
#		print(p.name)


reddit = authenticate()
get_comments(reddit)

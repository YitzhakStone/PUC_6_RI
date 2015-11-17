import tweepy
import MySQLdb
from io import open
from time import sleep

class Tweet(object):
	
	def __init__(self, id, id_str, text):
		self.id = id
		self.id_str = id_str
		self.text = text

############################################################################################

def gravarTweet(id, id_str, text):

	server = 'localhost'
	mysql_user = 'user'
	mysql_pass = 'password'
	database = 'ri'

	conn = MySQLdb.connect(server, mysql_user, mysql_pass, database, charset='utf8')

	c = conn.cursor()

	c.execute("INSERT INTO tweet (id, id_str, text) VALUES (%s,%s,%s)", (id, id_str, text) )

	conn.commit()

############################################################################################

#consumer key, consumer secret, access token, access secret.
ckey="xxx"
csecret="xxx"
atoken="xxx"
asecret="xxx"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

concatena = ''

#for x in range(0, 2):
	
public_tweets = api.search(count='30', result_type='recent', q='dilma')
for tweet in public_tweets:
	concatena += (tweet.id_str + ': ')
	concatena += (tweet.text.replace('\n', ' (((ENTER)))'))
	concatena += ('\n')
	t = Tweet((tweet.id), (tweet.id_str), (tweet.text))
	gravarTweet(t.id, t.id_str, t.text)

#sleep(0.5)

with open("Output.txt", "w", encoding='utf-8') as text_file:
	text_file.write(concatena)

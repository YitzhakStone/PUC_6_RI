import tweepy
import MySQLdb
import math

class Tweet(object):
	
	def __init__(self, id, id_str, text):
		self.id = id
		self.id_str = id_str
		self.text = text

############################################################################################

def gravarTweets(tweets):

	server = 'localhost'
	mysql_user = 'mysqluser'
	mysql_pass = 'mysqlpass'
	database = 'ri'

	conn = MySQLdb.connect(server, mysql_user, mysql_pass, database, charset='utf8')

	c = conn.cursor()

	for t in tweets:
		c.execute("INSERT INTO tweet (id, id_str, text) VALUES (%s,%s,%s)", (t.id, t.id_str, t.text) )

	conn.commit()

############################################################################################

#consumer key, consumer secret, access token, access secret.
ckey="NPHt6sBkmvhQDJrWuqBFChw5B"
csecret="IBDSMjwbI8Y1qmzp0lQNURNeppxnC7w8c6omntPNcyDE7hw8eQ"
atoken="98141806-c8UvwlylW4GwIOXI9Qy7O1DPA77QV0AdAmU3R8VRw"
asecret="DrflxuTFMehuPQrzkJ9mX5nvVQ4df30VCyVtWNwEBL1eb"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

hashtag = ''
total = 0
result_type = 'recent'

valid = False

while valid == False:
	hashtag = raw_input('Hashtag: ')
	try:
		total = int(raw_input('Qtd de tweets: '))
		if total > 0 and hashtag != '':
			break
	except ValueError:
		print("Dados invalidos!")
	else:
		print("Dados invalidos!")


iteracoes = int( math.ceil( total / 100.0 ) )
max_id = 0
tweetlist = []

for x in range(0, iteracoes):
	print ('Iteracao: ' + str(x+1) + ' de ' + str(iteracoes))

	if max_id > 0:
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag, max_id=max_id)
	else:
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag)

	for tweet in public_tweets:
		t = Tweet((tweet.id), (tweet.id_str), (tweet.text))
		tweetlist.append(t)
		if max_id == 0 or tweet.id < max_id:
			max_id = (tweet.id - 1)

gravarTweets(tweetlist)

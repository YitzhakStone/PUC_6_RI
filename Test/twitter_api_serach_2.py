import tweepy
import MySQLdb
import sys
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
	mysql_user = 'x'
	mysql_pass = 'x'
	database = 'ri'

	conn = MySQLdb.connect(server, mysql_user, mysql_pass, database, charset='utf8')

	c = conn.cursor()

	c.execute("INSERT INTO tweet (id, id_str, text) VALUES (%s,%s,%s)", (id, id_str, text) )

	conn.commit()

############################################################################################

#consumer key, consumer secret, access token, access secret.
ckey="x"
csecret="x"
atoken="x-x"
asecret="x"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

#concatenaErros = u'Tweets que nao foram salvos, por algum tipo de erro: \n\n\n'

for x in range(0, 90): # realiza a busca 90 vezes

	print ('Iteracao: ' + str(x))
	sucesso = 0
	erro = 0

	# 100 tweets por busca
	public_tweets = api.search(count='100', result_type='recent', q='dilma')
	for tweet in public_tweets:
		t = Tweet((tweet.id), (tweet.id_str), (tweet.text))
		try: 
			gravarTweet(t.id, t.id_str, t.text)
			sucesso += 1
		except:
			print ('Erro ao tentar gravar tweet no banco. ID do tweet: ' + t.id_str)
			print "Unexpected error:", sys.exc_info()[0]
			erro += 1

	print ('Tweets salvos: ' + str(sucesso) + ' / Com erro: ' + str(erro))
	print ('Dormindo... (240x60:4minutos)')
	sleep(240) # dorme 4 minutos para não pegar tweets repetidos

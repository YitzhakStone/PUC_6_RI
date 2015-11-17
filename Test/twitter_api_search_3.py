import tweepy
import math
from io import open

#consumer key, consumer secret, access token, access secret.
ckey="x"
csecret="x"
atoken="x-x"
asecret="x"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

hashtag = 'dilma'
result_type = 'recent'
total = 350
iteracoes = int( math.ceil( total / 100.0 ) )
concatena = ''

max_id = 0

for x in range(0, iteracoes):
	print ('Iteracao: ' + str(x+1) + ' de ' + str(iteracoes))

	if max_id > 0:
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag, max_id=max_id)
		#public_tweets = api.search(count='100', result_type=result_type, q=hashtag, until='2015-08-23', max_id=max_id)
	else:
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag)

	for tweet in public_tweets:
		concatena += tweet.id_str + ': '
		concatena += tweet.text.replace('\n', '')
		concatena += '\n'

		if max_id == 0 or tweet.id < max_id:
			max_id = (tweet.id - 1)

with open("Output.txt", "w", encoding='utf-8') as text_file:
	text_file.write(concatena)

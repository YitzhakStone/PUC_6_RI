# -*- coding: utf-8 -*-

import tweepy
import math

# RetirarStopWords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#ContarPalavras
from collections import Counter

import nltk

############################################################################################

class Tweet(object):
	
	def __init__(self, id, id_str, text):
		self.id = id
		self.id_str = id_str
		self.text = text

############################################################################################

def RetirarStopWords(texto):

	texto = texto.encode('utf-8').lower()

	texto = texto.replace('\n',' ').replace('\t',' ').replace('  ', ' ')
	texto = texto.replace('rt', '').replace('http', '')

	pontos = ['.',',','!','?',';', '\'', '#', '@', ':', '/']

	for p in pontos:
		texto = texto.replace(p.encode('utf8'), '')

	acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù','ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û']
	s_acentos = ['a','e','i','o','u','a','e','i','o','u','a','e','i','o','u','a','e','i','o','u']

	for i in range(0, len(acentos)):
		texto = texto.replace(acentos[i], s_acentos[i])

	retorno = ''

	for w in word_tokenize(texto):
		if not w in stopwords.words('portuguese'):
			w = ''.join(e for e in w if e.isalnum())
			retorno += (w + ' ')

	return retorno

############################################################################################

def ContarPalavras(tweets):
	texto = ''
	for tweet in tweets:
		texto += tweet.text

	palavras = texto.replace('\n',' ').replace('\t','').split(' ')

	contador = Counter(palavras)

	palavras_mais = []

	for i in contador.items():
		if i[1] > 10:
			palavras_mais.append(i)

	palavras_ord = sorted(palavras_mais, key=lambda s: s[1], reverse=True)

	for s in palavras_ord:
		#print s
		for c in s[0]:
			print c
			print ord(c)

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
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag, lang='pt', max_id=max_id)
	else:
		public_tweets = api.search(count='100', result_type=result_type, q=hashtag, lang='pt',)

	for tweet in public_tweets:
		tweet_text = RetirarStopWords(tweet.text)
		t = Tweet((tweet.id), (tweet.id_str), (tweet_text))
		tweetlist.append(t)
		if max_id == 0 or tweet.id < max_id:
			max_id = (tweet.id - 1)

ContarPalavras(tweetlist)
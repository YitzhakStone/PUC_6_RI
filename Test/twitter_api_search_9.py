#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import math
# RetirarStopWords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
# ContarPalavras
from collections import Counter
# Pontuacao
import string
# Regex
import re
# Polarização (classificar frase como boa ou ruim)
from textblob import TextBlob

class Tweet(object):
	
	def __init__(self, id, id_str, text):
		self.id = id
		self.id_str = id_str
		self.text = text

############################################################################################

def Polaridade(text):
	tblob = TextBlob(text)
	return tblob.sentiment.polarity


############################################################################################

def RetirarLinks(text):

	pattern = r'^https?:\/\/.*[\r\n]*'
	_text = ''

	for s in text.split(' '):
		result = re.sub(pattern, '', s, flags=re.IGNORECASE)
		_text += result + ' '

	_text = _text.replace('https', '').replace('http', '')

	return _text.strip()

def FiltrarPalavras(texto):

	# seta codificacao do texto e passa tudo pra minusculas
	texto = texto.encode('utf-8').lower()

	# retira quebras de linha e tabulações
	texto = texto.replace('\n',' ').replace('\t',' ').replace('  ', ' ')

	# retira sulfixo de retweets (RT)
	texto = texto.replace('rt', '')

	# retira links (http:// ... )
	texto = RetirarLinks(texto)

	#mapeamento dos principais caracteres acentuados
	acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù','ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û','ç']
	s_acentos = ['a','e','i','o','u','a','e','i','o','u','a','e','i','o','u','a','e','i','o','u','c']

	# substitui caracteres acentuados
	for i in range(0, len(acentos)):
		texto = texto.replace(acentos[i], s_acentos[i])

	# retira pontuacao
	for c in string.punctuation:
		texto = texto.replace(c, ' ')

	# variavel de retorno
	retorno = ''

	# retira as stopwords
	for w in word_tokenize(texto):
		w = ''.join(e for e in w if e.isalnum())		# retira caracteres que não são alfanumericos
		#if not w in stopwords.words('portuguese'):		# se a palavra nao for stopword (em portugues)
		if not w in stopwords.words('english'):			# se a palavra nao for stopword (em ingles)
			retorno += (w + ' ')						# concatena a palavra na string de retorno

	# strip: retira espaços no inicio e fim da string
	return retorno.strip()

############################################################################################

def ContarPalavras(tweets, count=5):
	texto = ''
	for tweet in tweets:
		texto += tweet.text

	palavras = texto.replace('\n',' ').replace('\t','').split(' ')

	contador = Counter(palavras)

	palavras_mais = []

	for i in contador.items():
		if i[1] > count:
			palavras_mais.append(i)

	palavras_ord = sorted(palavras_mais, key=lambda s: s[1], reverse=True)

	for s in palavras_ord:
		print s

############################################################################################

# consumer key, consumer secret, access token, access secret.
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
resto = total % 100

max_id = 0
tweetlist = []
lang = 'en'

for x in range(0, iteracoes):
	print ('Iteracao: ' + str(x+1) + ' de ' + str(iteracoes))

	if max_id > 0:
		if x < (iteracoes-1) or resto == 0:
			public_tweets = api.search(count='100', result_type=result_type, q=hashtag, lang=lang, max_id=max_id)
		else:
			public_tweets = api.search(count=str(resto), result_type=result_type, q=hashtag, lang=lang, max_id=max_id)
	else:
		if x < (iteracoes-1) or resto == 0:
			public_tweets = api.search(count='100', result_type=result_type, q=hashtag, lang=lang)
		else:
			public_tweets = api.search(count=str(resto), result_type=result_type, q=hashtag, lang=lang)

	i = 0
	for tweet in public_tweets:
		if i >= total:
			break
		i += 1
		print ''
		print '=================================================='
		print tweet.text
		print str(Polaridade(tweet.text))
		print ''
		tweet_text = FiltrarPalavras(tweet.text)
		print ''
		print 'sem stop: '
		print tweet_text
		print str(Polaridade(tweet_text))
		t = Tweet((tweet.id), (tweet.id_str), (tweet_text))
		tweetlist.append(t)
		if max_id == 0 or tweet.id < max_id:
			max_id = (tweet.id - 1)

#ContarPalavras(tweetlist)

#for t in tweetlist:
#	print ''
#	print t.text
#	print ';;;;;;;;;;;;;;;; polaridade: ' + str(Polaridade(t.text))

print ('Qtd de tweets processados: ' + str(len(tweetlist)))

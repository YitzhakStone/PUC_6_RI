#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import math
# ContarPalavras
from collections import Counter

from ri import *

############################################################################################

class Tweet(object):
	
	def __init__(self, id, id_str, text):
		self.id = id
		self.id_str = id_str
		self.text = text

############################################################################################

# consumer key, consumer secret, access token, access secret.
ckey="NPHt6sBkmvhQDJrWuqBFChw5B"
csecret="IBDSMjwbI8Y1qmzp0lQNURNeppxnC7w8c6omntPNcyDE7hw8eQ"
atoken="98141806-c8UvwlylW4GwIOXI9Qy7O1DPA77QV0AdAmU3R8VRw"
asecret="DrflxuTFMehuPQrzkJ9mX5nvVQ4df30VCyVtWNwEBL1eb"

def BuscarTweets(hashtag, qtdTweets):

	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)
	result_type = 'recent'

	iteracoes = int( math.ceil( qtdTweets / 100.0 ) )
	resto = qtdTweets % 100

	max_id = 0
	tweetlist = []
	lang = 'en'

	for x in range(0, iteracoes):
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
		if i >= qtdTweets:
			break
		i += 1
		
		tweetlist.append(tweet.text)
		if max_id == 0 or tweet.id < max_id:
			max_id = (tweet.id - 1)


	return tweetlist
#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
# ContarPalavras
from collections import Counter
# RetirarStopWords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
# Pontuacao
import string
# Regex
import re
# Polarização (classificar frase como boa ou ruim)
from textblob import TextBlob

import ri_twitter
import ri_instagram

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

############################################################################################

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

def ContarPalavras(lista):
	texto = ''
	for p in lista:
		texto += p

	palavras = texto.replace('\n',' ').replace('\t','').split(' ')

	contador = Counter(palavras)

	palavras_mais = []

	for i in contador.items():
		if i[1] > 2 and i[0] != '':
			palavras_mais.append(i)

	palavras_ord = sorted(palavras_mais, key=lambda s: s[1], reverse=True)

	return palavras_ord

############################################################################################

def Buscar(tag, count):
	lista1 = ri_twitter.BuscarTweets('star', 30)
	lista2 = ri_instagram.BuscarInstagram('star', 30)
	textos = lista1 + lista2

	return textos

def PolaridadeMedia(textos):
	i = 0
	pol = 0.0
	for t in textos:
		i += 1
		pol += Polaridade(t)


	if i == 0: return 0

	mediapol = pol / i
	return mediapol
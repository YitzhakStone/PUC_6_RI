#!/usr/bin/python
# -*- coding: utf-8 -*-

import ri
import ri_twitter
import ri_instagram



hashtag = ''
total = 0
tipopol = 0
valid = False

while valid == False:
	hashtag = raw_input('Hashtag: ')
	try:
		total = int(raw_input('Qtd de resultados (em cada api): '))
		tipopol = int(raw_input('Recuperar [1] Todos, [2] Postivos, [3] Negativos ? '))

		if total > 0 and hashtag != '' and tipopol > 0 and tipopol < 4:
			break
	except ValueError:
		print("Dados invalidos!")
	else:
		print("Dados invalidos!")




# Busca nas duas redes
#textos = ri.Buscar('tag', 50)

lista1 = ri_twitter.BuscarTweets(hashtag, total)
lista2 = ri_instagram.BuscarInstagram(hashtag, total)

f = open('out_twitter.txt', 'w')

lista1f = []
for t in lista1:
	filtrado = ri.FiltrarPalavras(t)
	polt = ri.Polaridade(filtrado)
	if tipopol == 1 or (tipopol == 2 and polt > 0) or (tipopol == 3 and polt < 0):
		lista1f.append(filtrado)
		f.write('\n==================================================\n')
		f.write(t.encode('utf-8'))
		descpol = 'bom' if polt > 0 else 'ruim'
		descpol = '(0% é considerado neutro)' if polt == 0 else descpol
		polt = polt if polt >= 0 else polt * (-1)
		f.write('\nPolaridade: ' + str(polt*100) + ' % ' + descpol)


f.write('\n==================================================\n')
f.write('\n\n\nRANKING DE PALAVRAS\n')
palavrasmais = ri.ContarPalavras(lista1f)
for i in palavrasmais:
	f.write('\n' + str(i))


mediapoli = ri.PolaridadeMedia(lista1f)
descpol = 'bom' if mediapoli > 0 else 'ruim'
descpol = '(0% é considerado neutro)' if mediapoli == 0 else descpol
mediapoli = mediapoli if mediapoli >= 0 else mediapoli * (-1)
f.write('\n\n==================================================\n')
f.write('Média de polaridade: ' + str(mediapoli*100) + ' % ' + descpol)


f.close()
f = open('out_instagram.txt', 'w')



lista2f = []
for t in lista2:
	filtrado = ri.FiltrarPalavras(t)
	polt = ri.Polaridade(filtrado)
	if tipopol == 1 or (tipopol == 2 and polt > 0) or (tipopol == 3 and polt < 0):
		lista2f.append(filtrado)
		f.write('\n==================================================\n')
		f.write(t.encode('utf-8'))
		descpol = 'bom' if polt > 0 else 'ruim'
		descpol = '(0% é considerado neutro)' if polt == 0 else descpol
		polt = polt if polt >= 0 else polt * (-1)
		f.write('\nPolaridade: ' + str(polt*100) + ' % ' + descpol)


f.write('\n==================================================\n')
f.write('\nRANKING DE PALAVRAS\n')
palavrasmais = ri.ContarPalavras(lista2f)
for i in palavrasmais:
	f.write('\n' + str(i))


mediapoli = ri.PolaridadeMedia(lista2f)
descpol = 'bom' if mediapoli > 0 else 'ruim'
descpol = '(0% é considerado neutro)' if mediapoli == 0 else descpol
mediapoli = mediapoli if mediapoli >= 0 else mediapoli * (-1)
f.write('\n\n==================================================\n')
f.write('Média de polaridade: ' + str(mediapoli*100) + ' % ' + descpol)


f.close()




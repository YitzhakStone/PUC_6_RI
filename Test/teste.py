from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


texto_longo = 'o rato roeu a roupa \tdo rei de roma, \nquando ele \nestava em \'nova\' jersey.'

print texto_longo.replace('\n',' ').replace('\t',' ').replace('  ', ' ')
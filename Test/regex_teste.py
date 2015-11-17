import re

texto = 'site 1 : https://www.google.com.br/search?q=regex+link&oq=regex+link&aqs=chrome..69i57.3787j0j7&sourceid=chrome&es_sm=93&ie=UTF-8#q=regex+replace+python , site 2: http://stackoverflow.com/questions/16720541/python-string-replace-regular-expression , site 3 : https://regex101.com/#python , site 4 : https://docs.python.org/2/library/re.html'

pattern = r'^https?:\/\/.*[\r\n]*'

for s in texto.split(' '):
	print (s)	
	result = re.sub(pattern, 'aqui_tinha_um_link', s, flags=re.IGNORECASE)
	print (result)

'''
regex = re.compile(r"^.*interfaceOpDataFile.*$", re.IGNORECASE)
for line in some_file:
    line = regex.sub("interfaceOpDataFile %s" % fileIn, line)
    # do something with the updated line
'''
# -*- coding: utf-8 -*-

import os
import sys
import httplib2
import json
import apiclient.discovery
import couchdb
from bs4 import BeautifulStoneSoup
from nltk import clean_html

API_KEY="coloque sua key"
USER_ID=sys.argv[0]

MAX_RESULTS =  200

def cleanHtml(html):
	if html == "": 
		return ""

	return BeautifulStoneSoup(clean_html(html), convertEntities=BeautifulStoneSoup.HTML_ENTITIES).contents[0]

service = apiclient.discovery.build('plus', 'v1', http=httplib2.Http(), developerKey=API_KEY)

activities_resource = service.activities()
request = activities_resource.list(
	userId=USER_ID,
	collection='public',
	maxResults='100') #Máximo permitido pela API

activities = []

while request != None and len(activities) < MAX_RESULTS:
	activities_document = request.execute()

	if 'items' in activities_document:
		for activity in activities_document['items']:
			if activity['object']['objectType'] == 'note' and activity['object']['content'] != '':
				activity['title'] = cleanHtml(activity['title'])
				activity['object']['content'] = cleanHtml(activity['object']['content'])
				activities.append(activity)

	request = service.activities().list_next(request, activities_document)

# Store out to a local file as json data if you prefer

if not os.path.isdir('out'):
	os.mkdir('out')


filename = os.path.join('out',  USER_ID + 'plus')
f = open(filename, 'w')
f.write(json.dumps(activities, indent=2))
f.close()

print >> sys.stderr, str(len(activities)), "activities written to", f.name

# Or store it somewhere like CouchDB like so..

 # server = couchdb.Server('http://localhost:8080')
 # DB = 'plus-' + USER_ID
 # db = server.create(DB)
 # db.update(activities, all_or_nothing=TRUE)



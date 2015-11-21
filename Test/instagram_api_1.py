#!/usr/bin/python
# -*- coding: utf-8 -*-

from instagram.client import InstagramAPI


access_token = "975448585.61ec9f0.3686d8aa7c0049389e9d9fb0f877092e"
client_secret = "efdf139d8a094fe7b26fa0cf40b7b2d3"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

results = api.tag_recent_media(tag_name="exodus", count=10)

for media in results[0]:
	print media.caption.text
	print '\n=====================================\n'
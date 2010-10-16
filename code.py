#!/usr/bin/env python

import json

import web

import itour

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def POST(self):
        data = web.input()
        
        location = data.location
        artists = data.artists
        
        artists = [artist.strip() for artist in artists.split(",")]
        
        events = itour.get_concerts(artists, location)
        
        concerts = []
        [concerts.append(event.json_data) for event in events]
        
        web.header('Content-Type', 'application/json')
        return json.dumps(concerts)
        
if __name__ == "__main__": app.run()
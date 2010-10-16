#!/usr/bin/env python

import json

import web

import itour

urls = (
  '/([0-9\-]+/[0-9\-]+)?/?$', 'index'
)

app = web.application(urls, globals())

class index:
    def POST(self, dates):
        data = web.input()
        
        location = data.location
        artists = data.artists
        
        artists = [artist.strip() for artist in artists.split(",")]
        
        if dates:
            dates = dates.split("/")
            start_date = dates[0]
            end_date = dates[1]
            events = itour.get_concerts(artists, location, start_date, end_date)
        else:
            events = itour.get_concerts(artists, location)
        
        concerts = []
        [concerts.append(event.json_data) for event in events]
        
        web.header('Content-Type', 'application/json')
        return json.dumps(concerts)
        
if __name__ == "__main__": app.run()

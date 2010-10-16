import json

from django.http import HttpResponse

import itour

def index(request, dates=None):
    if request.method == 'POST':
        data = request.POST
        
        location = data['location']
        artists = data['artists']
        
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
        
        return HttpResponse(json.dumps(concerts), mimetype='application/json')
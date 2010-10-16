import json

from django.http import HttpResponse

import itour

def index(request):
    if request.method == 'POST':
        data = request.POST
        
        location = data['location']
        artists = data['artists']
        
        artists = [artist.strip() for artist in artists.split(",")]
        
        events = itour.get_concerts(artists, location)
        
        concerts = []
        [concerts.append(event.json_data) for event in events]
        
        return HttpResponse(json.dumps(concerts), mimetype='application/json')
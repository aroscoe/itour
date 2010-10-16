import sys
import plistlib
from datetime import datetime

from bandsintown import bandsintown

bandsintown.app_id = 'itour'

def get_artists(file):
    '''Reads itunes xml file and extracs artists'''
    
    itunes = plistlib.readPlist(file)
    tracks = itunes["Tracks"]
    
    # Get all artists
    artists = []
    for track in tracks.values():
        artist = track.get("Artist")
        if artist:
            artist = artist.encode("utf8")
            artists.append(artist)
    
    # Remove duplicates
    artists = sorted(set(artists))
    
    return artists

def get_concerts(artists, location='Brooklyn, NY', start_date=None, end_date=None):
    search_args = {
        'radius': 10,
        'per_page': 10,
        'location': location
    }
    
    if start_date:
        date = start_date
        if end_date: date += ",%s" % end_date
        search_args['date'] = date
    
    concerts = []
    for i in range(0, len(artists), 50):
        search_args['artists'] = artists[i:i+50]
        new_concerts = bandsintown.Event.search(**search_args)
        if new_concerts:
            concerts += new_concerts
    
    # order concerts by date
    concerts = sorted(concerts, key=lambda x: datetime.strptime(x.datetime,'%Y-%m-%dT%H:%M:%S'))
    
    return concerts
import sys
import os.path
import plistlib

import bandsintown

from settings import APP_ID

bandsintown.app_id = APP_ID

def main(file):
    if os.path.exists(file):
        artists = get_artists(file)
        
        concerts = get_concerts(artists)
        
        if concerts:
            print concerts
        else:
            print "::: NO CONCERTS :::"
        
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

def get_concerts(artists, start_date=None, end_date=None):
    concerts = []
    for i in range(0, len(artists), 50):
        new_concerts = bandsintown.Event.search(artists=artists[i:i+50],
            radius=10, per_page=10, location="Brooklyn, NY")
        if new_concerts:
            concerts += new_concerts
    return concerts

if __name__ == "__main__":
    main(sys.argv[1])

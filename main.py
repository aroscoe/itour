import sys
import os.path
import plistlib

import bandsintown

from settings import APP_ID

bandsintown.app_id = APP_ID

def main(file):
    if os.path.exists(file):
        artists = get_artists(file)
        
        concerts = []
        for i in range(0, len(artists), 50):
            new_concerts = bandsintown.Event.search(artists=artists[i:i+50],
                radius=10, per_page=10, location="Brooklyn, NY")
            if new_concerts:
                concerts += new_concerts
        print concerts

def get_artists(file):
    '''Reads itunes xml file and extracs artists'''
    
    itunes = plistlib.readPlist(file)
    tracks = itunes["Tracks"]
    
    # Get all artists
    all_artists = []
    for track in tracks.values():
        artist = track.get("Artist")
        if artist:
            artist = artist.encode("utf8")
            all_artists.append(artist)
    
    # Remove duplicates
    artists = []
    # TODO: use a Set
    for artist in sorted(all_artists):
        if (artists == [] or artist != artists[-1]) and artist != None:
            artists.append(artist)
    
    return artists

if __name__ == "__main__":
    main(sys.argv[1])

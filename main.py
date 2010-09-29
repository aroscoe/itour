import sys
import os.path
import plistlib

def main(file):
    if os.path.exists(file):
        print get_artists(file)

def get_artists(file):
    '''Reads itunes xml file and extracs artists'''
    
    itunes = plistlib.readPlist(file)
    tracks = itunes["Tracks"]
    
    # Get all artists
    all_artists = []
    for track in tracks.values():
        all_artists.append(track.get("Artist"))
    
    # Remove duplicates
    artists = []
    for artist in sorted(all_artists):
        if (artists == [] or artist != artists[-1]) and artist != None:
            artists.append(artist)
    
    return artists

if __name__ == "__main__":
    main(sys.argv[1])

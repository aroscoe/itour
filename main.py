import plistlib

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

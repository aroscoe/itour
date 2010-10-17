#!/usr/bin/env python

import sys
import os.path
from optparse import OptionParser

# Put root dir on the PYTHONPATH
current_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(current_dir)))

import itour
import test

def main():
    parser = OptionParser()
    parser.add_option("-a", "--artists", dest="artists", help="comma separated list of artists")
    parser.add_option("-f", "--file", dest="filename", help="read data from FILENAME")
    parser.add_option("-t", "--test",
                      action="store_true", dest="test_mode",
                      help="Use test data set instead of parsing iTunes XML file")
    (options, args) = parser.parse_args()
    if len(args) > 0:
        parser.error("incorrect number of arguments")
    
    if options.test_mode:
        artists = test.artists
    elif options.artists:
        artists = [artist.strip() for artist in options.artists.split(",")]
    elif options.filename:
        if os.path.exists(options.filename):
            artists = itour.get_artists(options.filename)
        else:
            error = "File: %s does not exist" % options.filename
            parser.error(error)
    else:
        parser.error("You must specify iTunes XML file (-f)")
    
    if artists:
        print "\n%d Artists\n" % len(artists)
        
        concerts = itour.get_concerts(artists)
        
        if concerts:
            print concerts
            print "\n\n %d Concerts" % len(concerts)
        else:
            print "::: NO CONCERTS :::"

if __name__ == "__main__":
    main()

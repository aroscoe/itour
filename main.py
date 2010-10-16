#!/usr/bin/env python

import sys
import os.path

import itour

def main(file):
    if os.path.exists(file):
        artists = itour.get_artists(file)
        
        print "\n%d Artists" % len(artists)
        
        concerts = itour.get_concerts(artists)
        
        if concerts:
            print concerts
            print "\n\n %d Concerts" % len(concerts)
        else:
            print "::: NO CONCERTS :::"

if __name__ == "__main__":
    main(sys.argv[1])

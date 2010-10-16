#!/usr/bin/env python

import sys
import os.path
from optparse import OptionParser

import itour

def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="read data from FILENAME")
    (options, args) = parser.parse_args()
    if len(args) > 0:
        parser.error("incorrect number of arguments")
    
    if options.filename:
        if os.path.exists(options.filename):
            artists = itour.get_artists(options.filename)
            
            print "\n%d Artists\n" % len(artists)
            
            artists = artists[:50]
            
            print "\n\n\n\n"
            
            print artists[:50]
            
            print "\n\n\n\n"
            
            concerts = itour.get_concerts(artists)
            
            if concerts:
                print concerts
                print "\n\n %d Concerts" % len(concerts)
            else:
                print "::: NO CONCERTS :::"
        else:
            error = "File: %s does not exist." % options.filename
            parser.error(error)
    else:
        parser.error("You must specify iTunes XML file (-f).")

if __name__ == "__main__":
    main()

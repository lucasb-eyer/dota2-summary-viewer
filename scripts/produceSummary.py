#! /usr/bin/python
"""
Processes a given .dem file and puts the results in the data folder 
structure, so it can be easily visualized with the viewer (and no 
file mess is created)

should be called from the parent directory of 'scripts'
"""

import sh
import logging
import argparse

import os
import os.path as path

if __name__ == "__main__":
    #check if called from correct relative path
    currentDir = os.getcwd()
    #assumes the parent directory is called Dotascience
    assert(path.split(currentDir)[1] == "Dotascience")

    p = argparse.ArgumentParser(description="Dota 2 demo processor")
    p.add_argument('demo', help="The .dem file to parse")
    args = p.parse_args()

    demoFilePath = args.demo
    demoFile = path.basename(demoFilePath)
    demoFileName, demoFileExt = path.splitext(demoFile)
    
    destinationDirectory = path.join("data",demoFileName)
    if path.exists(destinationDirectory):
        if not path.isdir(destinationDirectory):
            log.error("Destination is not a directory:'%s'"%(destinationDirectory,))
            exit(1)
    else:
        log.error("Creating new directory:'%s'"%(destinationDirectory,))
        os.mkdir(destinationDirectory)

    #TODO: call dota2py to process the .dem, then produce the fun stuff - summary.json etc

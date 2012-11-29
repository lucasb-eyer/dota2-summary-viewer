#! /usr/bin/python
"""
Processes a given .dem file and puts the results in the data folder 
structure, so it can be easily visualized with the viewer (and no 
file mess is created)

usage: [script] path/to/replay.dem
"""

import logging
import argparse

import os
import os.path as path

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Dota 2 demo processor")
    p.add_argument('demo', help="The .dem file to parse")
    args = p.parse_args()

    demoFilePath = args.demo
    demoFile = path.basename(demoFilePath)
    demoFileName, demoFileExt = path.splitext(demoFile)
    
    #make sure the output goes to the right place yadda yadda files
    scriptDir = os.path.realpath(__file__)
    destinationDirectory = path.normpath(
        path.join(scriptDir,"..","..","data","output",demoFileName))

    if path.exists(destinationDirectory):
        if not path.isdir(destinationDirectory):
            log.error("Destination is not a directory:'%s'"%(destinationDirectory,))
            exit(1)
    else:
        logging.error("Creating new directory:'%s'"%(destinationDirectory,))
        os.mkdir(destinationDirectory)

    #preprocess .dem file (to demson)
    demoDemsonPath = path.join(destinationDirectory,"extract.demson")
    os.system("demoinfo2 %s > %s"%(
        demoFilePath,demoDemsonPath))

    #call dota2info summary script to process the .demson to the fun stuff - summary.json etc
    demoSummaryPath = path.join(destinationDirectory,"summary.json")
    os.system("dota2info_summary --out %s %s"%(
        demoSummaryPath, demoDemsonPath))

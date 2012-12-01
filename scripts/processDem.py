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

import json
import jinja2

class Renderer():
    def __init__(self,templateDir, staticDir):
        self.templateDir = templateDir
        self.staticDir = staticDir #absolute path to static files
        loader = jinja2.FileSystemLoader(self.templateDir)
        self.env = jinja2.Environment(loader=loader)

    def render(self, templateName, data):
        template = self.getTemplateFile(templateName)
        return template.render(data=data, staticDir=self.staticDir)

    def getTemplateFile(self, templateName):
        return self.env.get_template(templateName)

    def renderToAndFromFile(self, outFilePath, templateName, inJsonFilePath):
        dataFile = open(inJsonFilePath,"r")
        data = json.loads(dataFile.read())

        outFile = open(outFilePath, "w")
        outFile.write(self.render(templateName, data))

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Dota 2 demo processor")
    p.add_argument('demo', help="The .dem file to parse")
    args = p.parse_args()

    demoFilePath = args.demo
    demoFile = path.basename(demoFilePath)
    demoFileName, demoFileExt = path.splitext(demoFile)

    #make sure the output goes to the right place yadda yadda files
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    destinationDir = path.normpath(
        path.join(scriptDir,"..","data","output",demoFileName))

    #init renderer
    templateDir = path.normpath(path.join(scriptDir,"..","templates"))
    staticDir = path.normpath(path.join(scriptDir,"..","static"))
    renderer = Renderer(templateDir,staticDir)

    if path.exists(destinationDir):
        if not path.isdir(destinationDir):
            log.error("Destination is not a directory:'%s'"%(destinationDir,))
            exit(1)
    else:
        logging.error("Creating new directory:'%s'"%(destinationDir,))
        os.mkdir(destinationDir)

    print ("Producing .demson from .dem")
    demsonPath = path.join(destinationDir,"extract.demson")
    os.system("demoinfo2 %s > %s"%(
        demoFilePath,demsonPath))

    print ("Producing translated combatlog")
    combatlogPath = path.join(destinationDir,"combatlog.demson")
    os.system("dota2info_combatlog < %s > %s"%(
        demsonPath,combatlogPath))

    print ("Producing faction conflict data")
    factionConflictPath = path.join(destinationDir,"factionConflict.json")
    os.system("dota2info_factionConflict < %s > %s"%(
        demsonPath,factionConflictPath))

    #render a html file from the json data in factionConflictPath
    outPath = path.join(destinationDir,"viewFactionConflict.html")
    renderer.renderToAndFromFile(outPath,"factionConflict.html",factionConflictPath)

    #TODO: once it actually works
    #call dota2info summary script to process the .demson to the fun stuff - summary.json etc
    #demoSummaryPath = path.join(destinationDir,"summary.json")
    #os.system("dota2info_summary --out %s %s"%(
    #    demoSummaryPath, demoDemsonPath))


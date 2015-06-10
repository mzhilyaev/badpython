#!/usr/bin/python -u
import sys
import os
import Logger
import Config

def readFileContent(file):
  try:
    f = open(file, "r")
    content = f.read()
    f.close()
    return content
  except:
    print file + " ><><>"
    Logger.warning(file + " file failed open/read syscall")
    return None

def getSourceHarvestDirectory(sourceFormat):
  harvestDir = os.path.join(Cofig.get("dir.harvest"), sourceFormat)
  if (not os.path.exists(harvestDir)):
    ### make one
    os.mkdir(harvestDir)
  return harvestDir

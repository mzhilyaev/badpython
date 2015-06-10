#!/usr/bin/python -u

##### built in and python lib modules
import sys
import re
import random
import math
import os
import glob, sys, os.path
from optparse import OptionParser

startDirectory = os.getcwd()

### chnage to root of the tree and update the python path
def onStartup():
  absPath = os.path.abspath(sys.argv[0])
  dirName = re.sub(r"badpython.*$", "badpython", os.path.dirname(absPath))
  os.chdir(dirName)
  sys.path.append(dirName + "/python")

### run startup setter
onStartup();

#### import local modules here
import Config
import Logger
import SysUtils
import DocCranker
import NLP
import Consumer

#### run modules setup
Config.setup()
Logger.setup()

## change directory back to where it started
os.chdir(startDirectory)

def read_args():
  parser = OptionParser()
  parser.add_option("--format", dest="format", default="json", help="source format")
  parser.add_option("--scorer", dest="scorer", default="test", help="nlp scorer")
  parser.add_option("--consumer", dest="consumer", default="json", help="consumer of scored records")
  parser.add_option("--config", dest="config", default=None, help="config file")
  return parser.parse_args()

def processFiles(options, args):
  if options.config:
    Config.refresh(options.config)
  scorer = NLP.getScorer(options.scorer, Config.get("nlp"))
  consumer = Consumer.getConsumer(options.consumer, options.format)
  if len(args):
    for file in args:
      DocCranker.processFile(file, options.format, scorer, consumer)
  else:
    for file in sys.stdin:
      DocCranker.processFile(file, options.format, scorer, consumer)
  print consumer
    
if __name__ == '__main__':
  (options, args) = read_args()
  #print options
  #print args
  processFiles(options, args)


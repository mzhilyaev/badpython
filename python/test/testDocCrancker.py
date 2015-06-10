#!/usr/bin/python -u

##### built in and python lib modules
import sys
import os
import re
import json
import unittest

### chnage to root of the tree and update the python path
def onStartup():
  global absPath
  absPath = os.path.abspath(sys.argv[0])
  dirName = re.sub(r"badpython.*$", "badpython", os.path.dirname(absPath))
  os.chdir(dirName)
  sys.path.append(dirName + "/python")

### run startup setter
onStartup();

#### import local modules here
import Logger
import SysUtils
import DocCranker
import NLP
import Consumer

#### change directory back to script directory
os.chdir(os.path.dirname(absPath))

#### run modules setup
Logger.setup("debug")

class TestDocCranker(unittest.TestCase):
  def testOnePass(self):
    scorer = NLP.getScorer("test", {"ruleAFile": "adic.json", "ruleBFile": "bdic.json", "ruleCFile": "cdic.json"})
    consumer = Consumer.getConsumer("json")
    DocCranker.processFile("jsonDocs.json", "json", scorer, consumer)
    self.assertEquals(consumer.records, 
      [
        {
          "A": 1, 
          "publisher": "p1", 
          "C": 0, 
          "B": 1, 
          "docID": "d1", 
          "title": "t1", 
          "checkSum": "LW/VLuKAIQk9Me2tZmdCHQ==", 
          "published": "2014-01-01T12:00:00.000Z"
        }, 
        {
          "A": 1, 
          "publisher": "p2", 
          "C": 0, 
          "B": 1, 
          "docID": "d2", 
          "title": "t2", 
          "checkSum": "sMJQOHQ89pNw6gn27kpSxQ==", 
          "published": "2014-01-01T12:00:00.000Z"
        }
      ])

if __name__ == '__main__':
  unittest.main()


  
  




  


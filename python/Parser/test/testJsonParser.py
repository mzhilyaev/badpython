#!/usr/bin/python -u

##### built in and python lib modules
import sys
import os
import re
import glob
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
import Config
import Logger
import Parser.Factory
import SysUtils

#### run modules setup
Logger.setup("debug")
Config.setup()

#### change directory back to script directory
os.chdir(os.path.dirname(absPath))


class TestJsonParser(unittest.TestCase):
    def testJsonParser(self):
      fileData = json.loads(SysUtils.readFileContent("testJson.json"))
      parser = Parser.Factory.getParser("json")
      parser.parseFile("testJson.json")
      self.assertSequenceEqual(parser.docs(), fileData["docs"])
      self.assertEqual(parser.getFileMetaData("metaData"), "some data")


if __name__ == '__main__':
  unittest.main()


  
  




  


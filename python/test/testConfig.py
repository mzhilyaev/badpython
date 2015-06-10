#!/usr/bin/python -u

##### built in and python lib modules
import sys
import os
import re
import glob
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

#### change directory back to script directory
os.chdir(os.path.dirname(absPath))

#### run modules setup
Config.setup("conf.json")
Logger.setup("debug")

class TestConfig(unittest.TestCase):
    def testConfig(self):
      self.assertEqual(Config.get("v1"), "ooo")
      self.assertEqual(Config.get("v2"), 1)
      self.assertFalse(Config.get("v4"))
      self.assertEqual(Config.get("foo.bar"), 1)
      self.assertEqual(Config.get("foo.baz.boo"), "hello")

if __name__ == '__main__':
  unittest.main()


  
  




  


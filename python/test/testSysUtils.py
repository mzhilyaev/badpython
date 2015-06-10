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
import Logger
import SysUtils

#### change directory back to script directory
os.chdir(os.path.dirname(absPath))

#### run modules setup
Logger.setup("debug")

class TestSysUtils(unittest.TestCase):
    def testFileRead(self):
      ## test existing file
      cont = SysUtils.readFileContent("content.txt")
      self.assertEqual(cont, "hello")
      ## test non-existing file
      cont = SysUtils.readFileContent("nosuchfile.txt")
      self.assertIsNone(cont)


if __name__ == '__main__':
  unittest.main()


  
  




  


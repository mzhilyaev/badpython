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
from Exceptions import DatabaseException
from DB.Connection import Connection
from DB.Table import Table

#### run modules setup
Config.setup()
Logger.setup("debug")

class TestDb(unittest.TestCase):
    Config.get("database.host")
    global connection
    testDb = Config.get("database.testDb")
    connection = Connection(Config.get("database.host"),
                            Config.get("database.port"),
                            Config.get("database.user"),
                            Config.get("database.passwd"),
                            None)
    connection.execute("drop database IF EXISTS " + testDb, [])
    connection.execute("create database " + testDb, [])
    connection.execute("use " + testDb)
    connection.execute("create table test (a INT NOT NULL PRIMARY KEY, b VARCHAR(20))",[])

    def testInsert(self):
      table = Table("test", connection)
      table.consume({"a": 1, "b": "hi"})
      table.consume({"a": 2, "b": "bi"})
      ### make sure we catch failed insertions
      exceptionSeen = False
      try:
        table.consume({"c": 2, "b": "bi"})
        ### we should never reach it
        self.assertTrue(False)
      except DatabaseException as inst:
        exceptionSeen = True
      self.assertTrue(exceptionSeen)

      results = table.selectAll()
      self.assertSequenceEqual(results, [{u'a': 1, u'b': u'hi'}, {u'a': 2, u'b': u'bi'}])

      table.consume({"a": 2, "b": "hello"}, ignore="ignore")
      table.consume({"a": 1, "b": "hello"}, ignore="replace")
      results = table.selectAll()
      self.assertSequenceEqual(results, [{u'a': 1, u'b': u'hello'}, {u'a': 2, u'b': u'bi'}])

if __name__ == '__main__':
  unittest.main()


  
  




  


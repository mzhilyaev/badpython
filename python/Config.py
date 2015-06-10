#!/usr/bin/python -u
import sys
import re
import random
import os
import json
import SysUtils
from Exceptions import *

class Config:
  def __init__(self, cfgFile):
    self.load(cfgFile)

  def load(self, inFile):
    ## load configuration from argument or ./config.cfg.json or config/config.cfg.json
    cfgFile = inFile or ("config.cfg.json" if os.path.isfile("config.cfg.json") else os.path.join("config", "config.cfg.json"))
    if (not os.path.isfile(cfgFile)):
      raise ConfigException("unable to find config file")
    self.cfgFile = cfgFile
    content = SysUtils.readFileContent(cfgFile)
    self.json = json.loads(content)

  def get(self, param):
    items = param.split(".")
    obj = self.json
    for item in items:
      if (item not in obj):
        raise ConfigException("no config param: " + param)
      obj = obj[item]
    return obj
  
  def configFile(self):
    return self.cfgFile

_config = None

def get(param=None):
  if (param):
    return _config.get(param)
  else:
    return _config.json

def setup(configFile=None):
  global _config 
  _config = Config(configFile)

def refresh(configFile):
  _config.load(configFile)

def getConfigFile():
  return _config.configFile()
  
if __name__ == '__main__':
  pass


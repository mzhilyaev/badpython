#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import json
import SysUtils

class JsonParser:
  def __init__(self):
    pass

  def parseFile(self, fileName):
    self.json = json.loads(SysUtils.readFileContent(fileName))

  def docs(self):
    return self.json["docs"]
    
  def getFileMetaData(self, key):
    return self.json[key] if key in self.json else None

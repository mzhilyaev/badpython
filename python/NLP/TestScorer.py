#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import json
import hashlib
import base64
import Logger
import SysUtils
import Config

class TestScorer:
  def __init__(self, nlpConfig):
    self.Aterms = self.loadTermFile(nlpConfig["ruleAFile"])
    self.Bterms = self.loadTermFile(nlpConfig["ruleBFile"])
    self.Cterms = self.loadTermFile(nlpConfig["ruleCFile"])

  def loadTermFile(self, ruleFile):
    if not os.path.exists(ruleFile):
      cfgDirecotry = os.path.dirname(os.path.abspath(Config.getConfigFile()))
      ## pick at config directory
      ruleFile = os.path.join(cfgDirecotry, ruleFile)
    if not os.path.exists(ruleFile):
      raise NLPException("Unable to load rule file " + os.path.basename(ruleFile))
    return json.loads(SysUtils.readFileContent(ruleFile))
    
  def score(self, doc, sourceFormat):
    aScore = 0
    bScore = 0
    cScore = 0
    text = ""
    if ("title" in doc):
      text += doc["title"] + " "
    if ("summary" in doc):
      text += doc["summary"]
    ### compute matching words
    for word in text.split(" "):
      if (word in self.Aterms):
        aScore += 1
      if (word in self.Bterms):
        bScore += 1
      if (word in self.Cterms):
        bScore += 1
    ### compute checksum
    m = hashlib.md5()
    m.update(text)
    checkSum = base64.b64encode(m.digest())
    return {"A": aScore, "B": bScore, "C": cScore, "checkSum": checkSum}


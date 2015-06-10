#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import Exceptions
import Logger
import TestScorer

def getScorer(name, nlpConfig):
  if (name == "json" or name=="test"):
    return TestScorer.TestScorer(nlpConfig)
  else:
    Logger.alert("Unknown scorer type " + name);
    raise NLPException("Unknown scorer type " + name)


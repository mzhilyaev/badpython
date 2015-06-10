#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import Exceptions
import Logger
import JsonParser

def getParser(name):
  if (name == "json"):
    return JsonParser.JsonParser()
  else:
    Logger.alert("Unknown parser type " + name);
    raise ParserException("Unknown parser type " + name)


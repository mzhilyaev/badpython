#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import Exceptions
import Logger
import JsonConsumer

def getConsumer(name, sourceFormat = None):
  if (name == "json" or name=="test"):
    return JsonConsumer.JsonConsumer()
  else:
    Logger.alert("Unknown consumer type " + name);
    raise ConsumerException("Unknown consumer type " + name)


#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import json
import Logger
import SysUtils
import Parser.Factory

def processFile(fileName, sourceFormat, scorer, consumer):
  Logger.info("Processing " + sourceFormat + " file " + fileName)
  parser = Parser.Factory.getParser(sourceFormat)
  try:
    parser.parseFile(fileName)
  except Exception as e:
    Logger.error("Failed to parse " + sourceFormat + " file", e)
    return
  
  ### read documents
  for doc in parser.docs():
    record = {}
    ### score the doc
    try:
      results = scorer.score(doc, sourceFormat)
    except Exception as e:
      Logger.warning("Failed to score document " + doc["docID"], e)
      continue
      
    record["docID"] = doc["docID"]
    record["title"] = doc["title"]
    record["publisher"] = doc["publisher"]
    record["published"] = doc["published"]
    for key in results:
      record[key] = results[key]
  
    ### give record to consumer
    try:
      consumer.consume(record)
    except Exception as e:
      Logger.warning("Failed to consume document " + doc["docID"], e)


#!/usr/bin/python -u
import sys
import re
import logging
import os
import Config
import Exceptions

_scriptName = os.path.basename(sys.argv[0])
_logLevelsMap = {
 "debug": 0,
 "info": 1,
 "notice": 2,
 "warning": 3,
 "error": 4,
 "alert": 5,
}
_logLevelString = "debug"
_logLevel = _logLevelsMap[_logLevelString]

def _log(level, msg, e):
 if (_logLevelsMap[level] >= _logLevel):
   if e:
     msg += " [" + str(type(e)) + "=" + str(e) + "]"
   print "[%s] %s %s" % (_scriptName, level, msg)

def debug(msg,e=None):
  _log("debug",msg,e)

def info(msg,e=None):
  _log("info",msg,e)
  
def notice(msg,e=None):
  _log("notice",msg,e)
  
def warning(msg,e=None):
  _log("warning",msg,e)
  
def error(msg,e=None):
  _log("error",msg,e)
  
def critical(msg,e=None):
  _log("alert",msg,e)

def setLogLevel(levelString):
  global _logLevel
  if (levelString in _logLevelsMap):
    _logLevel = _logLevelsMap[levelString]
  else:
    raise Exceptions.ConfigException("Bad log level " + levelString)
    
def setup(level=None):
  if (level): 
    setLogLevel(level)
  else:
    setLogLevel(Config.get("log.level"))
  

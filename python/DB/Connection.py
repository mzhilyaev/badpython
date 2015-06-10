#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import pymysql.cursors
import Logger
from Exceptions import DatabaseException

class Connection:
  def __init__(self, host, port, user, passwd, db):
    self.host = host
    self.port = port
    self.user = user
    self.passwd = passwd
    self.db = db
    self.connect()

  def connect(self):
    self.connection = pymysql.connect(host=self.host,
                             user=self.user,
                             port=self.port,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

  def execute(self, sql, args = [], commit=True):
    cursor = self.connection.cursor()
    try:
      cursor.execute(sql, args)
      if (commit):
        self.connection.commit()
      return cursor
    except Exception as inst:
      Logger.warning("failed: " + sql + ";" +  ",".join(str(i) for i in args), inst)
      ###m re-throw
      raise DatabaseException(str(inst))



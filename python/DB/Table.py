#!/usr/bin/python -u
import sys
import re
import logging
import random
import math
import os
import pymysql.cursors
import Logger

class Table:
  def __init__(self, tableName, connection):
    self.tableName = tableName
    self.connection = connection

  def consume(self, record, ignore=""):
    self._insert(record, ignore)

  def _insert(self, record, ignore):
    columns = []
    values = []
    args = []
    for column in record:
      columns.append(column)
      values.append("%s")
      args.append(record[column])
    
    sql = "INSERT " + ignore
    if (ignore == "replace"):
      sql = "REPLACE"

    sql += " into " + self.tableName + " " + \
          " ( " + ",".join(columns) + " ) " +\
          " VALUES ( " + ",".join(values) + " ) "
    cursor = self.connection.execute(sql, args)
    cursor.close()

  def selectAll(self):
    try:
      cursor = self.connection.execute("select * from " + self.tableName, commit=False)
      return cursor.fetchall()
    finally:
      if ('cursor' in locals()):
        cursor.close()
    

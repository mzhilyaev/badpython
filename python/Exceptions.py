class Error(Exception):
  def __str__(self):
    return self.message

class ConfigException(Error):
  def __init__(self, message):
    self.message = message

class DatabaseException(Error):
  def __init__(self, message):
    self.message = message

class ParserException(Error):
  def __init__(self, message):
    self.message = message

class NLPException(Error):
  def __init__(self, message):
    self.message = message

class ConsumerException(Error):
  def __init__(self, message):
    self.message = message


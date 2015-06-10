import json

class JsonConsumer:
  def __init__(self):
    self.records = []

  def consume(self, record):
    self.records.append(record)

  def records(self):
    return self.records
 
  def __str__(self):
    return json.dumps(self.records, indent=2)

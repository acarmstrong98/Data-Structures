class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(self.size, item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
      self.size -= 1
      return self.storage.pop(0)

  def len(self):
    return self.size 

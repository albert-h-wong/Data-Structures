class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    x = self
    while True:
      if value == self.value:
        break
      elif value < x.value:
        if not x.left:
          x.left = BinarySearchTree(value)
          break
        else:
          x = x.left
      else:
        if not x.right:
          x.right = BinarySearchTree(value)
          break
        else:
          x = x.right


  def contains(self, target):
    y = self
    while True:
      if y.value == target:
        return True
      elif target < y.value and y.left:
        y = y.left
      elif target > y.value and y.right:
        y = y.right
      else:
        return False
  

  def get_max(self):
    max_value = self.value
    if not self.right:
      return max_value
    return self.right.get_max()


  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)
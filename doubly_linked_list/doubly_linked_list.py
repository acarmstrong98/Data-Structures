"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value):

    if self.length > 0:
      current_head = self.head
      new_head = ListNode(value, None, current_head)
      self.head = new_head
      self.length += 1
      current_head.prev = self.head

    else:
      node = ListNode(value, None, None)
      self.head = node
      self.tail = node
      self.length += 1
  
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    if self.length > 0:
      current_head = self.head

      if current_head.next is not None:
        self.head = current_head.next
        self.head.prev = None

      else:
        self.head = None
      self.length -= 1

      if self.length == 0:
        self.tail = None
      return current_head.value

   """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    if self.length > 0:
      current_tail = self.tail
      new_tail = ListNode(value, current_tail, None)
      self.tail = new_tail
      self.length += 1
      current_tail.next = self.tail

    else:
      node = ListNode(value, None, None)
      self.head = node
      self.tail = node
      self.length = 1

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    if self.length > 0:
      current_tail = self.tail

      if self.head.next is not None:
        self.tail.next = None
        self.tail = current_tail.prev

      else:
        self.tail = None
      self.length -= 1

      if self.length == 0:
        self.head = None
      return current_tail.value

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    
    self.add_to_head(node.value)
    self.length -= 1
    node.delete()

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    if node == self.head:
      self.head = node.next
    original_tail = self.tail
    self.tail = node

    if node.prev is not None:
      node.prev.next = node.next

    if node.next is not None:
      node.next.prev = node.prev
    self.tail.prev = original_tail
    original_tail.next = self.tail

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    if node == self.head and node == self.tail:
      node.delete()
      self.head = None
      self.tail = None
      self.length = 0
      return

    if node == self.head:
      self.remove_from_head()
      return

    if node == self.tail:
      self.remove_from_tail()
      return
    node.delete() 
    
  """Returns the highest value currently in the list"""
  def get_max(self):

    max = self.head.value
    node = self.head

    while node is not None:
      if node.value > max:
        max = node.value
      node = node.next
    return max

from Node import Node

class LinkedList:
  def __init__(self): 

    self.head = None
    self.tail = None
    return

  def add_list_item(self, item):
    node = Node(item)
    if self.head is None:
      self.head = node
    else:
      self.tail.next = node
    self.tail = node
    return
    
  def list_length(self):
    count = 0
    cur = self.head

    while cur is not None:
      count = count + 1
      cur = cur.next 
    return count

  def print_list(self):
    cur = self.head
    res = []

    while cur is not None:
      res.append(cur.data)
      cur = cur.next 

    print(res)
    return

  def search(self, value):
    cur = self.head
    node_id = 0
    res = []

    while cur is not None:
      if cur.data == value:
        res.append(node_id)
      
      node_id = node_id + 1
      cur = cur.next

    return res

  def remove_list_item_by_id(self, id):
    current_id = 0
    cur = self.head
    pre = None

    while cur is not None:
      if current_id == id:
        if pre is not None:
          pre.next = cur.next
        else:
          self.head = cur.next
      pre = cur
      cur = cur.next
      current_id = current_id + 1
    return
  
  def remove_value(self, value):

    pre = None
    cur = self.head

    while cur is not None:
      if cur.data == value:
        pre.next = cur.next
        return

      pre = cur
      cur = cur.next

    return

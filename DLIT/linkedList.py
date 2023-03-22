#double linked list using dequeue

class node:
    def __init__(self,version,timestamp,chunk):
        self.version = version
        self.timestamp = timestamp
        self.chunk = chunk
        self.next = None
        self.prev = None
class doubly_list:
    def __init__(self):
        self.head = None
        self.curr = None
    def append(self,version,timestamp,chunk):
        if self.head is None:
            self.head = node(version,timestamp,chunk)
            self.curr = self.head
        else:
            new_node = node(version,timestamp,chunk)
            new_node.next = None
            new_node.prev = self.curr
            self.curr.next = new_node
            self.curr = new_node
    
    def make_list(self,version,timestamp,chunks):
        #create double linked list
        size = len(chunks)
        for i in range(size):
            self.append(version,timestamp[i],chunks[i])
import time
class node:
    def __init__(self,version,timestamp,chunk):
        self.version = version
        self.timestamp = timestamp
        self.data = chunk
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def makelist(self,block):
        timestamp = time.time()
        temp = node(1,timestamp,block)
        if self.head is None:
            self.head = temp
        else:
            ptr = self.head
            while(ptr):
                if ptr.next is None:
                    ptr.next = temp
                    break
                ptr = ptr.next
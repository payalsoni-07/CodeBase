class node:
    def __init__(self,version,timestamp,chunk):
        self.version = version
        self.timestamp = timestamp
        self.chunk = chunk
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
    def append(self,version,timestamp,chunk):
        if self.head is None:
            self.head = node(version,timestamp,chunk)
        else:
            new_node = node(version,timestamp,chunk)
            ptr = self.head
            while(ptr):
                if ptr.next is None:
                    ptr.next = new_node
                    break
                ptr = ptr.next
    def make_list(self,version,timestamp,chunks):
        #create linked list
        size = len(chunks)
        for i in range(size):
            self.append(version,timestamp[i],chunks[i])
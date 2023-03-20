#double linked list using dequeue
import collections

class doubly_list:
    def __init__(self):
        self.double_linked_list = collections.deque()
    def make_list(self,version,timestamp,chunks):
        #create double linked list
        size = len(chunks)
        row = []
        for i in range(size):
            self.double_linked_list.append({'version':version,'timestamp':timestamp[i],'chunk':chunks[i]})
            row.append({'version':version,'timestamp':timestamp[i]})
    
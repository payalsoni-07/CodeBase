#double linked list using dequeue
import collections
import time

class doubly_list:
    def __init__(self):
        self.double_linked_list = collections.deque()
    def make_list(self,version,timestamp,chunks):
        #create double linked list
        size = len(chunks)
        for i in range(size):
            self.double_linked_list.append({'version':version,'timestamp':timestamp[i],'chunk':chunks[i]})
    def modify_data(self,pos,data,block_no):
        #modify data
        current_data = self.double_linked_list[block_no]['chunk']
        updated_data = current_data[:pos] + data + current_data[pos+len(data):]
        self.double_linked_list[block_no]['chunk'] = updated_data
        self.double_linked_list[block_no]['version'] += 1
        self.double_linked_list[block_no]['timestamp'] = time.time()
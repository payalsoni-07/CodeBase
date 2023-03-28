import time
import linkedlist
class DCHL:
    def __init__(self):
        self.DCHL = []
        self.length = 1000
        self.block_size = 0
        self.fb = []
    def insert(self,block):
        self.DCHL.append([self.length,block])

    def getindex(self,filename,current_block,pos):
        prev_blocks = 0
        for i in range(len(self.fb)):
            if self.fb[i][0] == filename:
                break
            else:
                prev_blocks += self.fb[i][1]
        total_blocks = prev_blocks + current_block
        blocks = 0
        for i in range(len(self.DCHL)):
            blocks += self.DCHL[i][0]
            if blocks > total_blocks:
                index = i
                break
        block_no = self.DCHL[index][0] - (blocks - total_blocks)
        return index,block_no
    
    def remove(self,filename,first_block,last_block,spos,epos):
        first_index,first_block_no = self.getindex(filename,first_block,spos)
        last_index,last_block_no = self.getindex(filename,last_block,epos)
        if first_index == last_index:
            if first_block_no == last_block_no:
                j,ptr = self.DCHL[first_index]
                for i in range(first_block_no):
                    ptr = ptr.next
                    current_data = ptr.data
                    updated_data = current_data[:spos] + current_data[epos:]
                    ptr.data = updated_data
                    ptr.version += 1
                    ptr.timestamp = time.time()
            else:
                j,ptr = self.DCHL[first_index]
                for i in range(first_block_no):
                    ptr = ptr.next
                    current_data = ptr.data
                    updated_data = current_data[:spos]
                    ptr.data = updated_data
                    ptr.version += 1
                    ptr.timestamp = time.time()
                    fptr = ptr
                    ptr = ptr.next
                    for i in range(first_block_no+1,last_block_no):
                        ptr = ptr.next
                        self.DCHL[first_index][0]-=1
                    current_data = ptr.data
                    updated_data = current_data[epos:]
                    ptr.data = updated_data
                    ptr.version += 1
                    ptr.timestamp = time.time()
                    fptr.next = ptr
        else:
                j,ptr = self.DCHL[first_index]
                for i in range(first_block_no):
                    ptr = ptr.next
                current_data = ptr.data
                updated_data = current_data[:spos]
                ptr.data = updated_data
                ptr.version += 1
                ptr.timestamp = time.time()
                fptr = ptr
                ptr = ptr.next
                for i in range(first_block_no+1,j):
                    delptr = ptr
                    ptr = ptr.next
                    del delptr
                    self.DCHL[first_index][0]-=1
                j,ptr = self.DCHL[last_index]
                for i in range(last_block_no):
                    ptr = ptr.next
                current_data = ptr.data
                updated_data = current_data[epos:]
                ptr.data = updated_data
                ptr.version += 1
                ptr.timestamp = time.time()
                self.DCHL[last_index][1] = ptr
                self.DCHL[last_index][0]=0
                while(ptr):
                    self.DCHL[last_index][0]+=1
                    ptr = ptr.next
                total_to_remove = last_index - first_index - 1
                for i in range(total_to_remove):
                    self.DCHL.pop(first_index+1)
                fptr.next = ptr
        return "Deleted"

    def update(self,pos, data,filename,current_block):
            index,block_no = self.getindex(filename,current_block,pos)
            j,ptr = self.DCHL[index]
            for i in range(block_no):
                ptr = ptr.next
            current_data = ptr.data
            updated_data = current_data[:pos] + data + current_data[pos:]
            if len(updated_data) > self.block_size:
                rem_data = updated_data[self.block_size:]
                ptr.data = updated_data[:self.block_size]
                ptr.version += 1
                ptr.timestamp = time.time()
                new_block = linkedlist.node(1,time.time(),rem_data)
                ptr_next = ptr.next
                ptr.next = new_block
                new_block.next = ptr_next
                self.DCHL[index][0]+=1
            else: 
                ptr.data = updated_data
                ptr.version += 1
                ptr.timestamp = time.time()
                rem_data = None
            
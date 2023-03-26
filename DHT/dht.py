import time
class DHT:
    
    def __init__(self):
        self.DHT = []
        self.chunk_size = 100
    def make_list_block(self,fileid,list_head,chunk_size):
        self.chunk_size = chunk_size
        self.DHT.append({'fileid':fileid,'list':list_head})

    def modify_data(self,pos,data,block_no,file_index):
        ptr = self.DHT[file_index]['list']
        i = 1
        while(i<block_no):
            ptr = ptr.next
            i += 1
        current_data = ptr.chunk
        modified_data = current_data[:pos-1] + data + current_data[pos-1:]
        ptr.chunk = modified_data
        ptr.version += 1
        ptr.timestamp = time.time()

        
    def remove_data(self,spos,epos,first_block_no,last_block_no,file_index):
        ptr = self.DHT[file_index]['list']
        spos %= self.chunk_size
        epos %= self.chunk_size
            
        if first_block_no == last_block_no:
            i = 1
            while i!= first_block_no:
                ptr = ptr.next
                i += 1
            current_data = ptr.chunk
            modified_data = current_data[:spos-1] + current_data[epos:]
            ptr.chunk = modified_data
            ptr.version += 1
            ptr.timestamp = time.time()
        else:
            i = 1
            while i!= first_block_no:
                ptr = ptr.next
                i += 1
            current_data = ptr.chunk
            modified_data = current_data[:spos-1]
            ptr.chunk = modified_data
            ptr.version += 1
            ptr.timestamp = time.time()
            fptr = ptr
            while i!= last_block_no:
                del_ptr = ptr
                ptr = ptr.next
                i += 1
                del del_ptr
            current_data = ptr.chunk
            modified_data = current_data[epos:]
            ptr.chunk = modified_data
            ptr.version += 1
            ptr.timestamp = time.time()
            fptr.next = ptr

import random
import string
import time
import os
#public and secret using 
class get_public_secret:
    
    def __init__(self,filename):
        #generate public key
        self.filename = filename
        self.timestamp = []
        self.version = 1
        self.autheticator = None
        self.tag = None
        self.no_of_blocks = 0
        self.file = open(os.path.join(os.pardir,"Cloud",filename), 'r')
        self.data = self.file.read()
        self.file.close()
        self.chunk_size = int(100)
        self.chunks = list(self.divide_chunks(self.data, self.chunk_size))
        #generate fileid
        self.fileid =  filename
        self.divide_chunks(self.chunks,self.chunk_size)
        
    def divide_chunks(self,l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]
            self.timestamp.append(time.time())
            self.no_of_blocks += 1
    
    def get_block_no(self,pos):
        return (pos//self.chunk_size)+1


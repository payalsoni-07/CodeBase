import random
import string
import time
import os
import sys
#public and secret using 
class get_public_secret:
    
    def __init__(self,filename):
        #generate public key
        self.filename = filename
        self.timestamp = []
        self.version = 1
        self.autheticator = None
        self.tag = None
        self.file = open(os.path.join(sys.path[-1],"Cloud",filename), 'r')
        self.data = self.file.read()
        self.file.close()
        self.chunk_size = int(100)
        self.chunks = list(self.divide_chunks(self.data, self.chunk_size))
        #generate fileid
        self.fileid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        #generate userid
        self.userid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        self.divide_chunks(self.chunks,self.chunk_size)
        
    def divide_chunks(self,l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]
            self.timestamp.append(time.time())


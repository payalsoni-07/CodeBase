import os
import sys

class split:
    def __init__(self):
        self.split = None
        self.block_size = 100
        self.total_blocks = 0
        self.blocks = []


    def split_file(self,filename):
        with open(os.path.join(os.pardir,"Cloud",filename), 'r') as f:
            while True:
                block = f.read(self.block_size)
                if not block:
                    break
                self.blocks.append(block)
                self.total_blocks += 1
    def blocknumber(self,pos):
        return pos//self.block_size

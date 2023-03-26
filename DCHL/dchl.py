class DCHL:
    def __init__(self):
        self.DCHL = []
        self.length = 100
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
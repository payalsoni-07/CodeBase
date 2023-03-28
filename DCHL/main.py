import dchl
import split
import linkedlist
import time

if __name__ == '__main__':
    DCHL = dchl.DCHL()
    while True:
        print("enter 1: for Insertion of data blocks")
        print("enter 2: for Modification of data")
        print("enter 3: for Removing some data")
        print("enter 4: for exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            filename = input("Enter the file name: ")
            t1 = time.time()
            sp = split.split()  
            sp.split_file(filename)
            t2 = time.time()
            print("Time taken for setup file: ",t2-t1)
            iter = 0
            remaining_blocks = sp.total_blocks
        
            DCHL.fb.append((filename,sp.total_blocks))
            DCHL.block_size = sp.block_size
            t1 = time.time()
            while(remaining_blocks > 0):
                if remaining_blocks > DCHL.length:
                    ll = linkedlist.linkedlist()
                    for i in range(0,DCHL.length):
                        ll.makelist(sp.blocks[iter+i])
                    DCHL.insert(ll.head)
                    remaining_blocks -= DCHL.length
                    iter+=1
                else:
                    ll = linkedlist.linkedlist()
                    for i in range(0,remaining_blocks):
                        ll.makelist(sp.blocks[iter+i])
                    DCHL.insert(ll.head)
                    DCHL.DCHL[-1][0] = remaining_blocks
                    remaining_blocks = 0
                    iter+=1
            t2 = time.time()
            print("Time taken for inserrt into DCHL: ",t2-t1)
        elif ch == 2:
            filename = input("Enter the file name: ")
            pos = int(input("Enter the position from where to be inserted: "))
            data = input("Enter the data to be inserted: ")
            current_block = sp.blocknumber(pos)
            pos = pos%sp.block_size
            t1 = time.time()
            for i in range(1,1000):
                DCHL.update(pos,data,filename,current_block)
            t2 = time.time()
            print("Time taken for modification: ",t2-t1)
        elif ch == 3:
            filename = input("Enter the file name: ")
            spos = int(input("Enter the position from where to be removed: "))
            epos = int(input("Enter the position till where to be removed: "))
            dt1 = time.time()
            first_block = sp.blocknumber(spos)
            last_block = sp.blocknumber(epos)
            spos = spos%sp.block_size
            epos = epos%sp.block_size
            DCHL.remove(filename,first_block,last_block,spos,epos)
            dt2 = time.time()
            print(dt1,dt2)
            print("Time taken for deletion: ",dt2-dt1)
        else:
            break
        
        count = 0
        for i in range(len(DCHL.DCHL)):
            #print("Block number: ",i)
            j,ptr = DCHL.DCHL[i]
            #print(j,ptr)
            for k in range(j):
                #print(ptr.data)
                count+= 1
                ptr = ptr.next
        print("verify list nodes ",count)
        

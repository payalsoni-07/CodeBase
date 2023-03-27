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
            index,block_no = DCHL.getindex(filename,current_block,pos)
            j,ptr = DCHL.DCHL[index]
            for i in range(block_no):
                ptr = ptr.next
            current_data = ptr.data
            updated_data = current_data[:pos] + data + current_data[pos:]
            if len(updated_data) > DCHL.block_size:
                rem_data = updated_data[DCHL.block_size:]
                ptr.data = updated_data[:DCHL.block_size]
                ptr.version += 1
                ptr.timestamp = time.time()
                new_block = linkedlist.node(1,time.time(),rem_data)
                ptr_next = ptr.next
                ptr.next = new_block
                new_block.next = ptr_next
                DCHL.DCHL[index][0]+=1
            else: 
                ptr.data = updated_data
                ptr.version += 1
                ptr.timestamp = time.time()
                rem_data = None
            t2 = time.time()
            print("Time taken for modification: ",t2-t1)
        elif ch == 3:
            filename = input("Enter the file name: ")
            spos = int(input("Enter the position from where to be removed: "))
            epos = int(input("Enter the position till where to be removed: "))
            t1 = time.time()
            first_block = sp.blocknumber(spos)
            last_block = sp.blocknumber(epos)
            spos = spos%sp.block_size
            epos = epos%sp.block_size
            first_index,first_block_no = DCHL.getindex(filename,first_block,spos)
            last_index,last_block_no = DCHL.getindex(filename,last_block,epos)
            if first_index == last_index:
                if first_block_no == last_block_no:
                    j,ptr = DCHL.DCHL[first_index]
                    for i in range(first_block_no):
                        ptr = ptr.next
                    current_data = ptr.data
                    updated_data = current_data[:spos] + current_data[epos:]
                    ptr.data = updated_data
                    ptr.version += 1
                    ptr.timestamp = time.time()
                else:
                    j,ptr = DCHL.DCHL[first_index]
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
                        delptr = ptr
                        ptr = ptr.next
                        del delptr
                        DCHL.DCHL[first_index][0]-=1
                    current_data = ptr.data
                    updated_data = current_data[epos:]
                    ptr.data = updated_data
                    ptr.version += 1
                    ptr.timestamp = time.time()
                    fptr.next = ptr
            else:
                j,ptr = DCHL.DCHL[first_index]
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
                    DCHL.DCHL[first_index][0]-=1
                j,ptr = DCHL.DCHL[last_index]
                for i in range(last_block_no):
                    ptr = ptr.next
                current_data = ptr.data
                updated_data = current_data[epos:]
                ptr.data = updated_data
                ptr.version += 1
                ptr.timestamp = time.time()
                DCHL.DCHL[last_index][1] = ptr
                DCHL.DCHL[last_index][0]=0
                while(ptr):
                    DCHL.DCHL[last_index][0]+=1
                    ptr = ptr.next
                total_to_remove = last_index - first_index - 1
                for i in range(total_to_remove):
                    DCHL.DCHL.pop(first_index+1)
            t2 = time.time()
            print("Time taken for deletion: ",float(t2-t1))
        else:
            break
        for i in range(len(DCHL.DCHL)):
            j,ptr = DCHL.DCHL[i]
            print(j,ptr)
            k = 0
            while ptr != None:
                k+=1
                ptr = ptr.next
            print("verify list nodes ",k)
        

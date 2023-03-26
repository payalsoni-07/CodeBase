import setup
import linkedList
import os
import sys
import dht
import time
#main function

if __name__ == '__main__':
 #2-D doubly linked list
    DHT = dht.DHT()
    while True:
        print("enter 1: for Insertion of data blocks")
        print("enter 2: for Modification of data")
        print("enter 3: for Removing some data")
        print("enter 4: for exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            name = input("Enter the file name: ")
            t1 = time.time()
            param = setup.get_public_secret(name)
            t2 = time.time()
            print("Time taken to setup file: ",t2-t1)
            t1 = time.time()
            ll = linkedList.linked_list()
            ll.make_list(param.version,param.timestamp,param.chunks)
            DHT.make_list_block(param.fileid,ll.head,param.chunk_size)
            t2 = time.time()
            print("Time taken to insert: ",t2-t1)
            
        elif ch == 2:
            name = input("Enter the file name: ")
            pos = int(input("Enter the position of data block to be modified: "))
            data = input("Enter the data to be modified: ")
            t1 = time.time()
            for i in range(len(DHT.DHT)):
                if DHT.DHT[i]['fileid'] == name:
                    file_index = i
                    break            
            block_no = param.get_block_no(pos)
            DHT.modify_data(pos,data,block_no,file_index)
            t2 = time.time()
            print("Time taken to modify: ",t2-t1)
        elif ch == 3:
            name = input("Enter the file name: ")
            spos = int(input("Enter the start position of data block to be removed: "))
            epos = int(input("Enter the end position of data block to be removed: "))
            t1 = time.time()
            for i in range(len(DHT.DHT)):
                if DHT.DHT[i]['fileid'] == name:
                    file_index = i
                    break
            first_block_no = param.get_block_no(spos)
            last_block_no = param.get_block_no(epos)
            DHT.remove_data(spos,epos,first_block_no,last_block_no,file_index)
            t2 = time.time()
            print("Time taken to remove: ",t2-t1)

        else:
            sys.exit(0)
        for i in range(len(DHT.DHT)):
            print(DHT.DHT[i]['fileid'])
            head = DHT.DHT[i]['list']
            print(head)
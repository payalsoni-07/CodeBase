import setup
import linkedList
import os
import sys
import dlit
#main function

if __name__ == '__main__':
 #2-D doubly linked list
    DLIT = dlit.DLIT()
    while True:
        print("enter 1: for Insertion of data blocks")
        print("enter 2: for Modification of data")
        print("enter 3: for Removing some data")
        print("enter 4: for exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            name = input("Enter the file name: ")
            param = setup.get_public_secret(name)
            ll = linkedList.doubly_list()
            ll.make_list(param.version,param.timestamp,param.chunks)
            DLIT.make_list_block(param.fileid,param.userid,ll.head,param.chunk_size)
            
        elif ch == 2:
            name = input("Enter the file name: ")
            for i in range(len(DLIT.DLIT)):
                if DLIT.DLIT[i]['fileid'] == name:
                    file_index = i
                    break
            pos = int(input("Enter the position of data block to be modified: "))
            data = input("Enter the data to be modified: ")
            block_no = param.get_block_no(pos)
            DLIT.modify_data(pos,data,block_no,file_index)
        elif ch == 3:
            name = input("Enter the file name: ")
            for i in range(len(DLIT.DLIT)):
                if DLIT.DLIT[i]['fileid'] == name:
                    file_index = i
                    break
            spos = int(input("Enter the start position of data block to be removed: "))
            epos = int(input("Enter the end position of data block to be removed: "))
            first_block_no = param.get_block_no(spos)
            last_block_no = param.get_block_no(epos)
            DLIT.remove_data(spos,epos,first_block_no,last_block_no,file_index)

        else:
            sys.exit(0)
        for i in range(len(DLIT.DLIT)):
            print(DLIT.DLIT[i]['fileid'])
            head = DLIT.DLIT[i]['list']
            print(head)
import setup
import linkedList
import os
import sys


DLIT =[]
def make_list_block(fileid,userid,list_doubly):
    DLIT.append({'fileid':fileid,'userid':userid,'list':list_doubly})

#main function

if __name__ == '__main__':
 #2-D doubly linked list
    while True:
        print("enter 1: for Insertion of data blocks")
        print("enter 2: for Modification of data")
        print("enter 3: for Removing some data")
        print("enter 4: for exit")
        ch = int(input("Enter your choice"))
        if ch == 1:
            name = input("Enter the file name: ")
            param = setup.get_public_secret(name)
            linkedList.make_list(param.version,param.timestamp,param.chunks)
            make_list_block(name,setup.get_user_id(),linkedList.double_linked_list)
            print("File inserted successfully")
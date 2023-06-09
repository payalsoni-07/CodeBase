import os
import sys
import exhash as exh
import time

#block information
fb = []
from cryptography.fernet import Fernet
#split file into blocks
def split_file(filename, block_size):
    with open(os.path.join(sys.path[0],"Cloud",filename), 'r') as f:
        while True:
            block = f.read(block_size)
            if block:
                yield block
            else:
                break

def get_block_data(filename,blockno):
    with open(os.path.join(sys.path[0],"Cloud",filename), 'r') as f:
        block = ""
        for i  in range(blockno):
            block = f.read(100)
    return block
def no_of_blocks(name):
    index = 0
    for i in range(len(fb)):
        if fb[i][0] == name:
            index = i
            break
    return fb[index][1]

def total_blocks():
    blocks = 0
    for i in range(len(fb)):
        blocks += fb[i][1]
    return blocks
def find_block_range(name):
    for i in range(len(fb)):
        if fb[i][0] == name:
            index = i
            break
    if index>0:
        blocks = 0
        for i in range(index):
            blocks += fb[i][1]
        return blocks
    else:
        return 0
#generate random secret key
def generate_secret_key():
    key  = Fernet.generate_key()
    return key


def get_block_no(spos,epos,name):
    last_block = 0
    first_block = 0
    n = no_of_blocks(name)
    for i in range(1,n):
        if spos <= i*100: 
            first_block = i
            break
    for i in range(first_block,n):
        if epos <= i*100:
            last_block = i
            break
    print("First Block no. is ", first_block)
    print("Last Block no. is ", last_block)
    return first_block,last_block
#encrypt block using key
def encrypt(block,key):
    Fer = Fernet(key)
    encrypted = Fer.encrypt(block.encode())
    return encrypted
def decrypt(encrypted,key):
    Fer = Fernet(key)
    decrypted = Fer.decrypt(encrypted)
    return decrypted

if __name__ =="__main__":
    #get file size
    size = int(input("Enter the size of the bucket: "))
    e = exh.ExtendibleHash(size)
    block_size = 100
    key  = generate_secret_key()
        
    print("Enter 1 for  inserting an element")
    print("Enter 2 for searching an element")
    print("Enter 3 for deleting an element")
    print("Enter 4 for updating an element")
    print("Enter 5 for exit")

    while(1):
        ch = int(input("Enter your choice: "))
        if ch == 1:
            filename = input("Enter the file name to perform operations: ")
            filesize = os.path.getsize(os.path.join(sys.path[0],"Cloud",filename))
            i = 1
            bl = total_blocks()
            t = 0
            print(bl)
            for block in split_file(filename, block_size):
                encrypted = encrypt(block,key)
                t1 = time.time()
                e.insert(bl+i, encrypted)
                t2 = time.time()
                t+=t2-t1
                i+=1
            fb.append((filename,i-1))
            print("Time taken for insertion is ", t)
            print("No. of blocks in the file: ", i-1)
        if ch == 2:
            name = input("Enter the file name: ")
            bl = find_block_range(name)
            print(bl)
            id = int(input("Enter the block no.: "))
            t1 = time.time()
            print(e.search(bl+id))
            t2 = time.time()
            print("Time taken for search is ", t2-t1)
        
        if ch == 3:
            name = input("Enter the file name: ")
            bl = find_block_range(name)
            spos = int(input("Enter the start position from where to delete data: "))
            epos = int(input("Enter the end position till where to delete data: "))
            t1 = time.time()
            first_block,last_block = get_block_no(spos,epos,name)
            if first_block == last_block:
                block_data = get_block_data(name,first_block)
                modified_data = block_data[:spos%100]
                modified_data += block_data[epos%100:]
                value = encrypt(modified_data,key)
                e.delete(bl+first_block)
                e.insert(bl+first_block,value)
            else:
                first_block_data = get_block_data(name,first_block)
                last_block_data = get_block_data(name,last_block)
                modified_data = first_block_data[:spos%100]
                modified_data += last_block_data[epos%100:]
                value = encrypt(modified_data,key)
                for i in range(first_block,last_block+1):
                    id = bl+i
                    e.delete(id)
                e.insert(bl+first_block,value)
            t2= time.time()
            print("Time in Deletion",t2-t1)

        if ch == 4:
            name = input("Enter the file name: ")
            bl = find_block_range(name)
            pos = int(input("Enter the position from where to update data: "))
            data = input("Enter the data to be added: ")
            blockno = pos//100
            block_data = get_block_data(name,blockno)
            updated_data = block_data+data
            encrypted = encrypt(updated_data,key)
            t1 = time.time()
            id = bl+blockno
            for i in range(1,1000):
                e.update(id,encrypted )
            t2 = time.time()
            print("Time taken for updation is ", t2-t1)

        if ch == 5:
            break   
        
        print("Global depth: ", e.global_depth)
        print("Bucket_count: ", e.bucket_count())
        print("No. of Split: ", e.split_count)
        
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
def find_block_range(name):
    index = 0
    for i in range(len(fb)):
        if fb[i][0] == name:
            index = i
            break
    return fb[index-1][1]
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
            t = 0
            total =0 
            t1 = time.time()
            for block in split_file(filename, block_size):
                #t1 = time.time()
                encrypted = encrypt(block,key)
                value = encrypted
                e.insert(i, value)
                #t2 = time.time()
                i+=1
                #t = max(t, t2-t1)
            fb.append((filename,i))
            t2 = time.time()
            print("Time taken for insertion is ", t2-t1)
            print("No. of blocks in the file: ", i-1)
            #print("Maximum time in insertion is ", t)
        if ch == 2:
            name = input("Enter the file name: ")
            bl = find_block_range(name)
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
            first_block,last_block = get_block_no(spos,epos,name)
            if first_block == last_block:
                block_data = get_block_data(name,first_block)
                modified_data = block_data[:spos%100]
                modified_data += block_data[epos%100:]
                value = encrypt(modified_data,key)
                t1 = time.time()
                print(e.delete(bl+first_block))
                t2 = time.time()
                print("Time taken for deletion is ", t2-t1)
                e.insert(bl+first_block,value)
            else:
                first_block_data = get_block_data(name,first_block)
                last_block_data = get_block_data(name,last_block)
                modified_data = first_block_data[:spos%100]
                modified_data += last_block_data[epos%100:]
                value = encrypt(modified_data,key)
                t1 = time.time()
                for i in range(first_block,last_block+1):
                    id = bl+i
                    print(e.delete(id))
                t2 = time.time()
                print("Time taken for deletion is ", t2-t1)
                e.insert(bl+first_block,value)

        if ch == 4:
            name = input("Enter the file name: ")
            bl = find_block_range(name)
            pos = int(input("Enter the position from where to update data: "))
            data = input("Enter the data to be added: ")
            blockno = pos//100
            block_data = get_block_data(name,blockno)
            updated_data = block_data+data
            t1 = time.time()
            encrypted = encrypt(updated_data,key)
            id = bl+blockno
            print(e.update(id,encrypted ))
            t2 = time.time()
            print("Time taken for updation is ", t2-t1)

        if ch == 5:
            break   
        
        # print("Global depth: ", e.global_depth)
        # print("Bucket_count: ", e.bucket_count())
        # print("No. of Split: ", e.split_count)

    
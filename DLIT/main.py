import setup
import linkedList
import os
import sys
n = int(input("Enter the number of files: "))
f =[]


for i in range(n):
    
    name = input("Enter the file name: ")
    f.append(setup.get_public_secret(name))


list_block =[] #2-D doubly linked list

def make_list_block(fileid,userid,list_doubly):
    list_block.append({'fileid':fileid,'userid':userid,'list':list_doubly})

d = []
for i in range(n):
    d.append(linkedList.doubly_list())
    d[i].make_list(f[i].version,f[i].timestamp,f[i].chunks)
    make_list_block(f[i].fileid,f[i].userid,d[i].double_linked_list)

#verification
while True:
    
        name = input("Enter the file name: ")
        i = int(input("Enter the file index: "))
        #update the name file
        print("enter 1: for Insertion of new data")
        print("enter 2: for Modification of data")
        print("enter 3: for Removing some data")
        ch = int(input("Enter your choice"))
        if ch == 1:
            file = open(os.path.join(sys.path[0],"Cloud",name), 'a')
            file.write(input("Enter the data: "))
            file.close()
        elif ch == 2:
            #modify some data
            file = open(os.path.join(sys.path[0],"Cloud",name), 'r')
            data = file.read()
            file.close()
            print(data)
            pos = int(input("Enter the position: "))
            data = data[:pos] + input("Enter the data: ") + data[pos:]
            file = open(os.path.join(sys.path[0],"Cloud",name), 'w')
            file.write(data)
            print(data)
            file.close()
        elif ch == 3:
            #delete some data
            file = open(os.path.join(sys.path[0],"Cloud",name), 'r')
            data = file.read()
            file.close()
            print(data)
            start = int(input("Enter the starting position: "))
            end = int(input("Enter the ending position: "))
            data = data[:start] + data[end:]
            file = open(os.path.join(sys.path[0],"Cloud",name), 'w')
            file.write(data)
            print(data)
            file.close()
        else:
            print("Invalid choice")
            continue
        
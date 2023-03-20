import os
import sys


#open a file from cloud folder
def open_file(filename):
    file = open(os.path.join(os.pardir,"Cloud",filename), 'r')
    print(file.read())

#main function
if __name__ == '__main__':
    open_file("t1.txt")
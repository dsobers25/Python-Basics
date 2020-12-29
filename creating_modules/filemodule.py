# create a module
# named file handling
# within file handling module
# create 2 fuctions
# function 1. takes the file name and check if the file exist or not 
# if it doesn't exist it will return a message, if it does it will tell 
# the number of lines
# function 2. take a file name and one integers in the params 
# and check if it exist or not
# if it doesn't exist return failure message, if it does then return
# the first n bytes
import os.path

# f = open(r"D:\Drive\workspace\Python-Learning-Materials\Python_Github_Projects\Python-Basics\file1.txt", 'r')
def num_lines(f_path):
    if os.path.isfile(f_path):
        f = open(f_path,'r')
        print(len(f.readlines()))
    else:
        print("File %s does not exist" % f_path)

# this works
# num_lines("../file1.txt")

# this does not work
# num_lines("../file1000.txt")

def read_bytes(f_path, bytesToRead):
    if os.path.isfile(f_path):
        f = open(f_path,'r')
        print(f.read(bytesToRead))
    else:
        print("File %s does not exist" % f_path)


# read_bytes("../file1.txt", 5)
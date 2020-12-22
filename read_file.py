# Read files using file("location/file_name", "mode") method
#mode could be
# 'r' -> read, 'w' -> write = create/overwrite, 'a' -> append/create

# methods for file
# read() -> returns a single variable with the entire content of file
# readlines() -> returns a list which each element will be one line of the file

# prints out the each element of the returned list
# Good for one line of file content
f = open("file1.txt",'r')
for x in f.readline():
    print(x)

# this will print out the entire content of the file line by line
x = f.readline()
while(x != ""):
    print(x)
    x = f.readline()
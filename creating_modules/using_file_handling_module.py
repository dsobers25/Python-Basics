from filemodule import read_bytes, num_lines

filepath="../file2.txt"

read_bytes(filepath, 9)

num_lines(filepath)

read_bytes("don't know", 19)
num_lines("don't know")
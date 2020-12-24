"""

Read a file and give the word count
for each word in the file

"""

# f = open(r"D:\Drive\workspace\Python-Learning-Materials\Python_Github_Projects\Python-Basics\file1.txt", 'r')
f = open("file2.txt", 'r')
word_frequency = {}
lines = f.readlines()
for x in lines:
    word_list = x.strip().split(" ")
    for word in word_list:
        freq = 1
        try:
            freq = word_frequency[word] + 1
        except KeyError:
            pass
        word_frequency[word] = freq

print("Word Frequency = %s" % word_frequency)
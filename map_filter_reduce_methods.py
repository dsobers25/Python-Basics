# Created a function named square that accepts one param k and returns k^2
def square(k):
    return k ** 2

print(square(5))


# map() methon allows me to pass a function in the 1st param
# and the sequece in the 2nd param to invoke the fuction on each 
# element of the sequence such a s a list
x = [1,2,3,4,5]
result = map(square, x)
# print map elements
for i in result:
    print(i)


# lambda fuction is an anonymous fuction
# does not have a name
myList = [1,3,6,9]
result_4 = map(lambda k: k ** 2, myList)
# print results of map
for i in result_4:
    print(i)


# filter will accept a function as its first parameter and a sequence for 
# the 2nd param. If the result of the fuction invocaction is true the it will be 
# returned
even_numbers = filter(lambda k : k % 2 == 0, range(1, 101))
# print out elements of even_numbers sequence
for i in even_numbers:
    print(i)


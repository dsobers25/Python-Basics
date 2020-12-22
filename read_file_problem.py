"""
1. Read file (id, name, product)
2. Print
    1. who are unique users
    2. for every user, how many products bought
    3. for every user, which distinct products have
    been purchased
    4. for every product, how many times is has been bought?
"""

# 1. who are unique users
print("\n#1. who are unique users?")
f = open("file1.txt", 'r')
unique_users = set()
x = f.readline()
while(x != ""):
    temp_list = x.split(",")
    id = temp_list[0]
    unique_users.add(id)
    x = f.readline()

print("Unique Users = %s" % unique_users)

# 2. for every user, how many products bought
print("\n#2. for every user, how many products bought?")
f2 = open("file1.txt", 'r')
productCount = [0,0,0,0]
x2 = f2.readline()

while(x2 != ""):
    temp_list = x2.split(",")
    if(temp_list[0] == '1'):
        productCount[0] +=1
    elif(temp_list[0] == '2'):
        productCount[1] +=1
    elif(temp_list[0] == '3'):
        productCount[2] +=1
    elif(temp_list[0] == '4'):
        productCount[3] +=1
    x2 = f2.readline()

print(" User 1 purchased %d products, User 2 purchased %d products, User 3 purchased %d products, User 4 purchased %d products" % (productCount[0], productCount[1], productCount[2], productCount[3]))

# 3. for every user, which distinct products have been purchased
print("\n#3. for every user, which distinct products have been purchased?")
distinctProductA = set()
distinctProductB = set()
distinctProductC = set()
distinctProductD = set()
f3 = open("file1.txt", 'r')
x3 = f3.readline()

while(x3 != ""):
    temp_list = x3.split(",")
    if(temp_list[0] == '1'):
        distinctProductA.add(temp_list[2].strip("\n"))
    elif(temp_list[0] == '2'):
        distinctProductB.add(temp_list[2].strip("\n"))
    elif(temp_list[0] == '3'):
        distinctProductC.add(temp_list[2].strip("\n"))
    elif(temp_list[0] == '4'):
        distinctProductD.add(temp_list[2].strip("\n"))
    x3 = f3.readline()

print("User 1 Purchased Products %s, User 2 Purchased Products %s, User 3 Purchased Products %s, User 4 Purchased Products %s" % (distinctProductA, distinctProductB, distinctProductC, distinctProductD))

# 4. for every product, how many times is has been bought?
print("\n#4. for every product, how many times is has been bought?")
f4 = open("file1.txt",'r')
x4 = f4.readline()
productPurchaseCount = [0,0,0,0]

while(x4 != ""):
    temp_list = x4.split(',')
    # print(temp_list)
    if(temp_list[2].strip("\n") == 'P1'):
        productPurchaseCount[0] += 1
    elif(temp_list[2].strip("\n") == 'P2'):
        productPurchaseCount[1] += 1
    elif(temp_list[2].strip("\n") == 'P3'):
        productPurchaseCount[2] += 1
    elif(temp_list[2].strip("\n") == 'P4'):
        productPurchaseCount[3] += 1
    x4 = f4.readline()

print("Product P1 was Purcashed %d times, Product P2 was Purcashed %d times, Product P3 was Purcashed %d times, Product P4 was Purcashed %d times" % (productPurchaseCount[0], productPurchaseCount[1], productPurchaseCount[2], productPurchaseCount[3]))

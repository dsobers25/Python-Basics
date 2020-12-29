# currently works only for odd numbers

"""
 Exercise​ ​1:   Create​ ​a​ ​function​ ​that​ ​accepts​ ​a​ ​single​ ​array​ ​as​ ​an​ ​argument.​ ​
 Given​ ​an​ ​array​ ​of​ ​integers,​ ​x,​ ​sort x​ ​and​ ​split​ ​the​ ​integers​ ​into​ ​three​ ​smaller​ ​
 arrays​ ​of​ ​equal​ ​length.​ ​If​ ​the​ ​length​ ​of​ ​x​ ​is​ ​not​ ​evenly divisible​ ​by​ ​three,​ ​
 increase​ ​the​ ​size​ ​of​ ​the​ ​smaller​ ​arrays​ ​by​ ​one​ ​starting​ ​from​ ​the​ ​first​ ​array.​ 
 ​The function​ ​should​ ​return​ ​an​ ​array​ ​of​ ​arrays.   
 Example:   Input​ ​=​ ​[2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14] 
            Output​ ​=​ ​[​ ​[0,​ ​1,​ ​2,​ ​3,​ ​4,​ ​5],​ ​[6,​ ​7,​ ​8,​ ​9,​ ​10,​ ​11],​ ​[12,​ ​13,​ ​14,​ ​15,​ ​16]​ ​]  
"""

input = [2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14]

input2 = [2,3,4,44,9,53,1,34,11,3,91,12]

def func1(list):
    list.sort()
    size = len(list)
    print("Size = %d" %size)
    subList = size/3
    print("subList = %d" %subList)
    extra = size%3
    print("extra is %d" % extra)
    start = 0
    yup = False
    stop = int(subList)
    newList = []
    for _ in range(3):
        # print("extra is %d" % extra)
        # print("Start value is %d" % start)
        if extra > 0:
            yup = True
            stop+=1
            # print("Stop value is %d" % stop)
            extra-=1
            # print("extra is now %d" % extra)
        temp1 = list[start:stop]
        print("Temp1** is %s" % temp1)
        newList.append(temp1)
        start = stop
        if yup == True:
            stop-=1
        stop+=stop+1
    return newList

print(func1(input))
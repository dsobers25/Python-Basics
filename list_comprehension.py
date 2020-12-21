# list comprehension Example 1
x = [1,2,3,4,5]
result = [] 
for i in x:
    result.append(i*i)
    
print(result)

# Short hand list comprehension
# Examle 2
result2 = [i*i for i in x]

print(result2)
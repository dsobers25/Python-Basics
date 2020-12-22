# Accept input by using input()

lower = input("Enter lower number: ")
higher = input("Enter higher number: ")
even_list = filter(lambda x: x%2 == 0, range(int(lower), int(higher) + 1))

for i in even_list:
    print(i)
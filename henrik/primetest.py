import math
print("")
number = 300
for num in range(2,number):
    for i in range(2,num):
        if (num % i ==0):
            break
    else:
        print(num)
imp

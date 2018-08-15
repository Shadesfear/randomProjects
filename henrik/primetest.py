number = 300

for num in range(2,number):
    prime = False

    for i in range(2,num):
       if (num % i == 0):
           prime = False
           break
       else:
           prime = True
    if (prime == True):
        print(num)

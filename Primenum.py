from math import sqrt
num=int(input(" Enter a number "))
if num>1:
    for i in range(2,int(sqrt(num))+1):
        if(num%i==0):
            print(num, " Is not a prime number ")
            break
    else:
        print(num, " Is a prime number ")
else:
    print(num, " Is not a prime number ")


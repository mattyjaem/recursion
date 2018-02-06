import math

def sumEven(n):
    #finds all evens up to given num and adds them up
    if int(n) > 0:
        if int(n) % 2 == 0:
            n = int(n) + sumEven(int(n) - 2)
            return(n)
        else:
            print(n)
            n = int(n) - 1
            n = int(n) + sumEven(int(n) - 2)
            return(n)
    else:
        return(n)

#Main program
while 1 == 1:
    number = input("Enter Number:")
    sum = sumEven(number)
    print ("The Sum of the evens up to that number is: %s" %sum)


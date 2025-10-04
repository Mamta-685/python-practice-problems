#FIZZBUZZ Problem
# Write a function fizzbuzz(n) that:
# Prints numbers from 1 to n.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz".



def fizzbuzz(n):
    # n = int(input("enter number upto which you want to be printed : "))--- If you want user input, you don’t need n as a parameter. If you want it as a function parameter, then don’t ask input inside.
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
                print("fuzz")
        elif i % 5 == 0:
                print("buzz")
        else:
            print(i)

num = int(input("enter number here: "))
fizzbuzz(num)
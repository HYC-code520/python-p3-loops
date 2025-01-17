#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1

    print("Happy New Year!")

        
    

def square_integers(int_list):
    # code goes here!
    # num_square = num * num
    #loop through [1,2,3,4,5]
    squared_list = []
    for integer in int_list:
        squared = integer * integer
        squared_list.append(squared)
    return squared_list

def fizzbuzz():
    # code goes here!
    #fizz = num % 3
    #buzz = num % 5
    #fizzbuzz = num % 3 and 5
    
    for num in range(1, 101):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)



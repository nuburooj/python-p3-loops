#!/usr/bin/env python3

def happy_new_year():
 
 counter = 10
 while counter > 0:
    print(counter)
    counter -= 1
    print("Happy New Year!")

    

def square_integers(int_list):
    return [num ** 2 for num in int_list]
    

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

fizzbuzz()
   
    # counter = 100
    # while counter < 100:
    #     print(fizzbuzz(num))
    #     counter += 1
    #     print(num)





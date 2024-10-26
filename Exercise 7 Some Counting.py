# -*- coding: utf-8 -*-
"""
Exercise 7: Some Counting
***************
Shan Marky Isidro
"""

# It Count up from 0 to 50 in increments of 1
print("Counting up from 0 to 50:")
for numbers in range(51):  # range of 51 counts from 0 to 50 
    print(numbers)

# It count down from 50 to 0 in decrements of 1
print("Counting down from 50 to 0:")
for numbers in range(50, -1, -1):  # It will start at 50, end at 0, decrement by 1
    print(numbers)

# It count up from 30 to 50 in increments of 1
print("Counting up from 30 to 50:")
for numbers in range(30, 51):  # It will start at 30, end at 50
    print(numbers)

# It count down from 50 to 10 in decrements of 2
print("Counting down from 50 to 10 in decrements of 2:")
for numbers in range(50, 9, -2):  # It will start at 50, end at 10, decrement by 2
    print(numbers)

# It count up from 100 to 200 in increments of 5
print("Counting up from 100 to 200 in increments of 5:")
for numbers in range(100, 201, 5):  # It will start at 100, end at 200, increment by 5
    print(numbers)
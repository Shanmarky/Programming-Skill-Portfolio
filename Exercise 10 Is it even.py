# -*- coding: utf-8 -*-
"""
Exercise 10: Is it even?
*********
Shan Marky Isidro
"""
#This function will check if even or odd number
def check_number(number):
    if number%2== 0:
        return "even number"
    else:
        return "odd number"
#The function is to get the user input and print the result
def main():
    print("Welcome to Even or Odd Checker!")#It will ask for a number
    number = int(input("Please enter a number: ")) #The function will check even or add
    result = check_number(number)
    print(result) # It will print the result

main()

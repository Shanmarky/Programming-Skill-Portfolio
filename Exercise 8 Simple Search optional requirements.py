# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search optional requirements
**************
Shan Marky Isidro
"""
#I add the names
names=["Jake","Zac","Ian","Ron","Sam","Dave"]
#It will allow the user input the search
search_for=input("Enter the name of you're searching for:")
#It will check if the search for is in th list
if search_for in names:
    print(f"{search_for} was found in the list!")
else:
    print(f"{search_for} was not found in the list")

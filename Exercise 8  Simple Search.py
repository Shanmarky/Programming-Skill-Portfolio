# -*- coding: utf-8 -*-
"""
Exercise 8: Simple Search
"""
names=["Jake","Zac","Ian","Ron","Sam","Dave"]
#It will define the search
search_for="Sam"
#It will check if the search for is in th list
if search_for in names:
    print(f"{search_for} was found!")
else:
    print(f"{search_for} was not found in the list")

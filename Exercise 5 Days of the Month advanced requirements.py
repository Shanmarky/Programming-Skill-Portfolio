# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month advanced requirements
*********
Shan Marky isidro
"""
# First i add dictionary mapping month numbers to days in each month
days_in_month={
    1: 31,   # January
    2: 28,   # February (it will adjust if leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}
# I will ask the person to input the month number
month_number = int(input("Enter the month number (1-12): "))
# it Check if the input month is valid
if month_number==2:  # If the month is February
    leap_year_input=input("Is this year a leap year? (yes/no): ").strip().lower()
    days=29 if leap_year_input=="yes" else 28
else:
    days=days_in_month.get(month_number,"Invalid month number.")
# I print the result
if days !="Invalid month number.":
    print(f"There are {days} days in month {month_number}.")
else:
    print(days)  # it show the invalid month message

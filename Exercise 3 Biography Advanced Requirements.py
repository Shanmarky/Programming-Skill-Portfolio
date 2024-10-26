"""
Exercise 3: Biography Advanced Requirements
***********************
Shan Marky Isidro
"""
# I add two string variables and one integer variable to store information and i print it
name=input("Enter you full name:")
hometown=input("Enter your hometown:")
age=int(input("Enter you age:"))
print(name,hometown,age)

if age is not None: # If the age is not valid
  print(name,hometown,age)
else: # It will show that your answer is not valid
    print("Your answer is not valid")

"""
Exercise 3: Biography
********
Shan Marky Isidro
"""
# I add two string variables and one integer variable to store information 
name=input("Enter your name: ")
hometown=input("Enter your hometown: ")
age=input("Enter your age: ")
# I store information in a dictionary
my_info = {
    "name":name,
    "hometown":hometown,
    "age":age
}
# I print each value on separate line
print("\nName:",my_info["name"])
print("Hometown:",my_info["hometown"])
print("Age:",my_info["age"])
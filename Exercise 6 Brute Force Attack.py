"""
Exercise 6: Brute Force Attack 
***********
Shan Marky Isidro
"""
#First i will define the password
correct_password="12345"
user_password=""
while True: #I use a while Loop to repeat the ask for the password
    user_password=input("Enter you password")
    if user_password==correct_password:#It check if the password is correct
        print("Your password is correct!")
        break #it will exit the Loop when the password is incorrect
    else:
        print("Your password is incorrect. Please try again")
    
    
    

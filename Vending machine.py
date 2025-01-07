# -*- coding: utf-8 -*-
"""
Vending Machine ShanMarkyIsidro
"""
#Import pyttzx3 for text to speech conversion
import pyttsx3
#This function display and announce the welcome message
def welcome_message():
    print("Hello! Welcome to Shan's Vending Machine")
    voice = pyttsx3.init()
    voice.say("Hello! Welcome to Shan's Vending Machine")
    voice.runAndWait()
#This function display the collection of the items, The names,prices, and stocks
def display_items(items):
    for key, item in items.items():
        print(f"{key}. {item['name']} - AED{item['Price']} (Stock: {item['Stock']})")
#this function display the add ons suggestion before you proceed to the payment method
def add_ons(selected_item, items):
    add_ons_selected = [] # this one to determine the empty list for the add ons
    if selected_item['Add_ons']:#this use if statement and for loops
        print("You might also like:")
        for addon in selected_item['Add_ons']: #To repeat through add ons and match to item dictionary
            for key, item in items.items():
                if item['name'] == addon:
                    print(f"{key}. {addon} (AED{item['Price']})") #This details the key, name and the price
       #this loop is for user input
        while True:
            add_on_choice = input("Enter the item number of the add-on you want to add (Type 'next' to finish): ")
            if add_on_choice.lower() == 'next':
                break #This break the loop if the user finishes
            elif add_on_choice in items and items[add_on_choice]['name'] in selected_item['Add_ons']:
                add_ons_selected.append(items[add_on_choice])
                print(f"Added {items[add_on_choice]['name']} to your purchase.")
            else:#This will hold or handle the invalid input from the user
                print("Invalid choice. Please select a valid add-on item.")
    return add_ons_selected #This return the list of the add ons
#This function display the payment method and calculate the change
def payment_method(selected_item, add_ons):
    total_due = selected_item['Price'] + sum(add_on['Price'] for add_on in add_ons)
    while total_due > 0: #This loop for the payment untill the asked amount gets paid
        try:
            payment = float(input(f"Insert AED{total_due:.2f}: "))
            if payment >= total_due:
                change = payment - total_due #It will calculate the change
                selected_item['Stock'] -= 1 #This will update the stocks of items in the machine
                for add_on in add_ons:
                    add_on['Stock'] -= 1
                print(f"Thank you for your purchase! Your change is AED{change:.2f}.")
                return change
            #If the payment is insufficient
            else:
                total_due -= payment #Subtract the payment from the total due
                print(f"Insufficient amount. AED{total_due:.2f} remaining.") #The user will inform of the remaining balance
        except ValueError: #This will manage the invalid payment or invalid input
            print("Invalid input. Please enter a valid amount.") #This message will show that your payment is invalid
#This function will display or print the receipt of the purchase
def print_receipt(selected_item, add_ons, change):
    print("\n***** Receipt *****")#The header
    print(f"Item: {selected_item['name']} - AED{selected_item['Price']}") #This will display the all item details
    if add_ons:
        print("Add-ons:")
        for add_on in add_ons:
            print(f"  {add_on['name']} - AED{add_on['Price']}")
    #This print will display the change of amount 
    print(f"Total Change: AED{change:.2f}")
    print("Thank you for using Shan's Vending Machine!")
    print("*********************")
    voice = pyttsx3.init() #The ending of the text to conversion of the receipt
    voice.say(f"Thank you for your purchase! Your change is {change:.2f} dirhams.")
    voice.runAndWait()#This will run  the text to speech output

# The Vending machine items and prices
items = {
    "1": {"name": "Popcorn", "Price": 4.50, "Stock": 15, "Add_ons": ["Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "2": {"name": "Lays chips", "Price": 5, "Stock": 20, "Add_ons": ["Popcorn", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "3": {"name": "Toblerone", "Price": 5.50, "Stock": 13, "Add_ons": ["Popcorn","Lays chips","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "4": {"name": "Dairy Milk", "Price": 3.50, "Stock": 10, "Add_ons": ["Popcorn","Lays chips","Toblerone","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "5": {"name": "Ritz biscuit", "Price": 2.25, "Stock": 15, "Add_ons": ["Popcorn","Lays chips","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "6": {"name": "Mai Dubai", "Price": 1.15, "Stock": 30, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "7": {"name": "Pepsi", "Price": 2.50, "Stock": 20, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pineapple juice","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "8": {"name": "Pineapple juice", "Price": 2.75, "Stock": 20, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Redbull","PRIME","C2 Juice","Minute maid Juice",]},
    "9": {"name": "Redbull", "Price": 10, "Stock": 20, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","PRIME","C2 Juice","Minute maid Juice",]},
    "10": {"name": "PRIME", "Price": 15, "Stock": 15, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","C2 Juice","Minute maid Juice",]},
    "11": {"name": "C2 Juice", "Price": 2.75, "Stock": 16, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","Minute maid Juice",]},
    "12": {"name": "Minute maid Juice", "Price": 1.75, "Stock": 16, "Add_ons": ["Popcorn","Lays chips", "Toblerone","Dairy Milk","Ritz biscuit","Mai Dubai","Pepsi","Pineapple juice","Redbull","PRIME","C2 Juice",]},
}

# Main message and item display of the machine
if __name__ == "__main__":
    welcome_message()
    display_items(items)#This shows the available stocks and prices of the items
    while True: #THis while loop for the item selection
        display_items(items)
        select = input("Enter the item number you want to purchase: ") #This will print print for the user to select an item
        if select in items: 
            selected_item = items[select]
            if selected_item['Stock'] > 0: #This will check if the item have available stock
                print(f"You have selected {selected_item['name']}. Price: AED{selected_item['Price']}") #This print will confirm the selection
                add_ons = add_ons(selected_item, items)#Display the user for the add ons
                change = payment_method(selected_item, add_ons) #It will Handle the payment method and to update the stocks
                print_receipt(selected_item, add_ons, change) #This will print the receipt
                break #This break will stop or exit the loop  after the successful purchase item
            else: #Else will manage the out of stock part when it happens
                print("Sorry, the selected item is out of stock.") #display to show to user
        else:#This will manage the invalid input from the user
            print("Invalid selection. Please try again.") #It will show the  message if the selection item number is invalid and try again


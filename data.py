#Helper functions to use in main.py

from datetime import datetime

#Variables
date_format = "%m-%d-%Y"   
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:      #If user just hit enter return today's date
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)        
        return valid_date.strftime(date_format)                       #converting back into month/day/year
    except ValueError:
        print("Invalid date input. Please enter the date in the dd-mm-yyyy format.")        #If the user gives an invalid input
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative, non zero value.") #If an invalid amount is given
        return amount
    except ValueError as e:
        print(e) #Error
        return get_amount() #Repeat until valid amount is given

def get_category():
    category = input("Enter the category: 'I' for Income and 'E' for Expense): ")
    category = category.upper() #Convert to uppercase
    if category in CATEGORIES:  #if user category is in the category options
        return CATEGORIES[category]
    
    print("Invalid category. Please enter 'I' for Income or 'E' for Expenses.")      #Repeat until a valid category is given
    return get_category()

def get_description():
    return input("Enter a description (optional): ")

#'Smart Financial Tracker' - Leonardo Chavarry

"""
This is a financial tracker built using pands and csv.
1. Run main.py and fill out the information.
2. Check your data in the csv file
3. Track all your expenses!
"""

from datetime import datetime

#Import the libraries we will use 
import pandas as pd
import csv


#Import the "data" file into this one to use the helper functions
from data import get_amount, get_category, get_date, get_description


class CSV: 
    CSV_FILE = "tracker.csv"  # CSV file that will store our incomes/expenses
    COLUMNS = ["date", "amount", "category", "description"]  # The column headers for the CSV file
#Variables
    FORMAT = "%m-%d-%Y"     # The format for dates in the CSV file

#Initialize the CSV file
    @classmethod
    def initialize_csv(cls):
        """
        Initialize the CSV file
        If the file already exists, skip.
        """
        try:
            pd.read_csv(cls.CSV_FILE) # Try reading the CSV file
        
        except FileNotFoundError: # If the file doesn't exist, create a new DF with the same column headers
            df = pd.DataFrame(columns=cls.COLUMNS)  
            df.to_csv(cls.CSV_FILE, index=False)  # Write the DF in the CSV file

# Add an entry to the CSV file
    @classmethod  
    def add_entry(cls, date, amount, category, description):
        """
        Add a new entry to the CSV file.
        Parameters:
        date: Date of the transaction
        amount: Amount of the transaction
        category: Category of the transaction
        description: Description of the transaction
        """
        # Dictionary to represent the entry
        new_entry = {"date": date, "amount": amount, "category": category, "description": description}

        # Open the CSV file
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            # Create a DictWriter
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            # Write the entry
            writer.writerow(new_entry)
        print("Entry added successfully")

# Get all the transactions within a date range
    @classmethod  
    def get_transactions(cls, start_date, end_date):    
        """
        Get the transactions from a start date to an end date (inclusive).
        Parameters:
        start_date: The start date
        end_date: The end date 
        """
        # Read the CSV file
        df = pd.read_csv(cls.CSV_FILE)      
        
        # Convert to the datetime format
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        
        # Convert start_date and end_date to the datetime format
        start_date = datetime.strptime(start_date, CSV.FORMAT)      
        end_date = datetime.strptime(end_date, CSV.FORMAT)
        
        # Mask to filter the DataFrame
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        #If it's empty, print a message
        if filtered_df.empty:
            print('No transactions found')
        else: # Print the transactions found
            print(
                f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
                )
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

def add():
    """
    Function to add a new transaction
    """
    # Initialize the CSV file
    CSV.initialize_csv()
    # Get the date of the transaction
    date = get_date(
        "Enter the date of the transaction (mm-dd-yyyy) or press 'Enter' for today's date: ", 
        allow_default=True,
        )
    # Amount of the transaction
    amount = get_amount ()
    # Category of the transaction
    category = get_category()
    # Description of the transaction
    description = get_description()
    # Add this transaction to the CSV file
    CSV.add_entry(date, amount, category, description)

# Initialize the CSV file
CSV.initialize_csv()    

# main function
add()
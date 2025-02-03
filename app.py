import sqlite3
from database import get_all_transactions
import pandas as pd

def add_expenseincome():
    print("Welcome to simple financial recorder App! \n Choose an option")
    print(" 1. Add Expenses \n 2. Add Income \n 3. View Transactions \n 4. Exit")

    choice = int(input("Enter your choice "))

    if choice == 1:

    elif choice == 2:

    elif choice == 3:

    elif choice == 4:

    else:
        return("Invalid choice, please try again")    

add_expenseincome()
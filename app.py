import sqlite3
from database import add_transactions, get_all_transactions
import pandas as pd

def add_expenseincome():
    print("Welcome to simple financial recorder App! \n Choose an option")
    print(" 1. Add Expenses \n 2. Add Income \n 3. View Transactions \n 4. Exit")

    choice = int(input("Enter your choice "))

    if choice == 1:
        description = input("Enter expense description: ")
        amount = float(input("Enter amount: "))
        add_transactions(description, amount, 'expense')
        print("Expense succesfully added")
        
    elif choice == 2:
        description = input("Enter income description: ")
        amount = float(input("Enter amount: "))
        add_transactions(description, amount, 'income')
        print("Income succesfully added")

    elif choice == 3:
        print("\nAll Transactions:")
        transactions = get_all_transactions()
        df = pd.DataFrame(transactions, columns=["ID", "Description", "Amount", "Type"])
        print(df)

    elif choice == 4:
        print("Exiting Application")
        exit()

    else:
        return("Invalid choice, please try again")    

if __name__ == "__main__":
    add_expenseincome()
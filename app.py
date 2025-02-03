import sqlite3
from database import get_all_transactions
import pandas as pd

def add_expenseincome():
    print("Welcome to simple financial recorder App! \n Choose an option")
    print(" 1. Add Expenses \n 2. Add Income \n 3. View Transactions \n 4. Exit")

    choice = int(input("Enter your choice "))

add_expenseincome()
import sqlite3 

def connect_db():
    conn = sqlite3.connect('transactions.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTO INCREMENT,
        description TEXT,
        amount REAL,
        type TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def add_transactions(description, amount, type):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (description, amount, type) VALUES (?, ?, ?)",
                   (description, amount, type))
    conn.commit()
    conn.close()

def get_all_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

if __name__ == "__main__":
    connect_db()
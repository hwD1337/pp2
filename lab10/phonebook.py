import sqlite3
import csv

conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE
);
""")
conn.commit()

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

def insert_from_csv(filepath):
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cursor.execute("INSERT OR IGNORE INTO PhoneBook (name, phone) VALUES (?, ?)", (row[0], row[1]))
        conn.commit()

def update_phonebook(name=None, phone=None, new_name=None, new_phone=None):
    if name:
        cursor.execute("UPDATE PhoneBook SET name = ?, phone = ? WHERE name = ?", (new_name or name, new_phone or phone, name))
    elif phone:
        cursor.execute("UPDATE PhoneBook SET name = ?, phone = ? WHERE phone = ?", (new_name or name, new_phone or phone, phone))
    conn.commit()

def query_phonebook(filter_key, filter_value):
    cursor.execute(f"SELECT * FROM PhoneBook WHERE {filter_key} LIKE ?", (f"%{filter_value}%",))
    return cursor.fetchall()

def delete_from_phonebook(identifier):
    cursor.execute("DELETE FROM PhoneBook WHERE name = ? OR phone = ?", (identifier, identifier))
    conn.commit()

if __name__ == "__main__":
    print("1. Add user from console\n2. Upload from CSV\n3. Update\n4. Query\n5. Delete")
    choice = input("Choose action: ")
    if choice == "1":
        insert_from_console()
    elif choice == "2":
        filepath = input("Enter CSV file path: ")
        insert_from_csv(filepath)
    elif choice == "3":
        name = input("Current name: ")
        new_name = input("New name: ")
        new_phone = input("New phone: ")
        update_phonebook(name=name, new_name=new_name, new_phone=new_phone)
    elif choice == "4":
        key = input("Search by (name/phone): ")
        value = input("Search value: ")
        results = query_phonebook(key, value)
        for r in results:
            print(r)
    elif choice == "5":
        identifier = input("Enter name or phone to delete: ")
        delete_from_phonebook(identifier)


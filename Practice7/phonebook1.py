import csv
from connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()


def add_contact(name, phone):
    cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()


def load_from_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        for name, phone in reader:
            add_contact(name, phone)


def show_contacts():
    cur.execute("SELECT * FROM contacts")
    for row in cur.fetchall():
        print(row)


def update_contact(name, new_phone):
    cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))
    conn.commit()

def update_contact_name(old_name, new_name):
    cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, old_name))
    conn.commit()


def find_contact(name):
    cur.execute("SELECT * FROM contacts WHERE name=%s", (name,))
    print(cur.fetchall())


def delete_contact(name):
    cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    conn.commit()


while True:
    print("\n1 - Add")
    print("2 - Show")
    print("3 - Update by num")
    print("4 - Find")
    print("5 - Delete")
    print("6 - Load CSV")
    print("7 - Update by name")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        add_contact(name, phone)

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        name = input("Name: ")
        phone = input("New phone: ")
        update_contact(name, phone)

    elif choice == "4":
        name = input("Name: ")
        find_contact(name)

    elif choice == "5":
        name = input("Name: ")
        delete_contact(name)

    elif choice == "6":
        load_from_csv()

    elif choice == "7":
        old_name = input("Old name: ")
        new_name = input("New name: ")
        update_contact_name(old_name, new_name)

    elif choice == "0":
        break

cur.close()
conn.close()
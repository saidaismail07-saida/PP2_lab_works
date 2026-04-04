from connect import get_connection

conn = get_connection()
cur = conn.cursor()

def search(pattern):
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matches found")

def paginate(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)

def upsert(name, phone):
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print(f"Saved {name} with phone {phone}")

def delete(value):
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    print(f"Deleted contact matching '{value}'")

def insert_many():
    cur.execute("CALL insert_many(%s, %s)",
                (['Ali','Bob','Eve'], ['123','abc','999']))
    conn.commit()
    print("Inserted multiple contacts")


# === MENU LOOP ===
while True:
    print("\n1 - Search")
    print("2 - Add/Update")
    print("3 - Delete")
    print("4 - Paginate")
    print("5 - Insert Many (Test)")
    print("0 - Exit")

    ch = input("Choose: ")

    if ch == "1":
        search(input("Enter pattern: "))
    elif ch == "2":
        upsert(input("Name: "), input("Phone: "))
    elif ch == "3":
        delete(input("Name or phone: "))
    elif ch == "4":
        limit = int(input("Limit: "))
        offset = int(input("Offset: "))
        paginate(limit, offset)
    elif ch == "5":
        insert_many()
    elif ch == "0":
        break
    else:
        print("Invalid choice")

cur.close()
conn.close()
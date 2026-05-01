from connect import get_connection
import json

conn = get_connection()
cur = conn.cursor()


def search():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    for row in cur.fetchall():
        print(row)


def filter_by_group():
    g = input("Group: ")
    cur.execute("""
        SELECT c.name, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (g,))
    print(cur.fetchall())


def search_email():
    e = input("Email: ")
    cur.execute("SELECT * FROM contacts WHERE email ILIKE %s", ('%' + e + '%',))
    print(cur.fetchall())


def paginate():
    limit = 3
    offset = 0

    while True:
        cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        for row in cur.fetchall():
            print(row)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev" and offset >= limit:
            offset -= limit
        else:
            break


def export_json():
    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    rows = cur.fetchall()

    data = []

    for row in rows:
        data.append([
            row[0],
            row[1],
            str(row[2]) if row[2] else None,   # 👈 ВАЖНО
            row[3],
            row[4]
        ])

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)


def import_json():
    with open("contacts.json") as f:
        data = json.load(f)

    for row in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (row[0],))
        if cur.fetchone():
            if input("skip? (yes/no): ") == "yes":
                continue

        cur.execute("INSERT INTO contacts(name,email) VALUES(%s,%s)",
                    (row[0], row[1]))

    conn.commit()


def add_phone():
    name = input("Name: ")
    phone = input("Phone: ")
    t = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, t))
    conn.commit()


def move_group():
    name = input("Name: ")
    g = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, g))
    conn.commit()


while True:
    print("""
1 Search
2 Filter by group
3 Search email
4 Pagination
5 Export JSON
6 Import JSON
7 Add phone
8 Move group
0 Exit
""")

    c = input("Choose: ")

    if c == "1":
        search()
    elif c == "2":
        filter_by_group()
    elif c == "3":
        search_email()
    elif c == "4":
        paginate()
    elif c == "5":
        export_json()
    elif c == "6":
        import_json()
    elif c == "7":
        add_phone()
    elif c == "8":
        move_group()
    elif c == "0":
        break
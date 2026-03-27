import psycopg2

conn =psycopg2.connect(
    host="localhost",
    dbname="pp2_db",
    user="pp2",
    password="pp2_password"
)

cur=conn.cursor()
cur.execute("select version();")
print(cur.fetchone())
cur.close()
conn.close()
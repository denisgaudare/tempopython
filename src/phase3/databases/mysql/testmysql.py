import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='finance'
)
cursor = conn.cursor()

cursor.execute("SELECT * FROM trades")
results = cursor.fetchall()
for row in results:
    print(row)

# https://dev.mysql.com/doc/connector-python/en/
# https://www.psycopg.org/docs/
# https://python-oracledb.readthedocs.io/en/latest/
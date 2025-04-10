import sqlite3

first = True

if first:
    connection = sqlite3.connect("tutorial.db")
    curseur = connection.cursor()
    curseur.execute("CREATE TABLE movie(title, year, score)")
    curseur.execute("""
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5)
    """)
    connection.commit()
    connection.close()


# ------------------------------

new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
c = new_cur.execute("SELECT year, title FROM movie ORDER BY year")
data = c.fetchall()
for row in data:
    print(row)
new_con.close()
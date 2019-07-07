import sqlite3
#import _mysql

conn = sqlite3.connect('sql.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS bans (
            id INTEGER,
            banned INTEGER(1)
)""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS chatfilter (
            id INTEGER,
            filtered TEXT,
            active INTEGER(1)
)""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS sugban (
            id INTEGER,
            banned INTEGER(1)
)""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS version (
            ver TEXT
)""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS Warnings (
            id INTEGER,
            memid INTEGER,
            amount BIGINT,
            reasons TEXT
)""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS cmds (
            sid INTEGER,
            cmdid TEXT,
            rid TEXT,
            mid TEXT,
            erid TEXT,
            emid TEXT,
            ffa INTEGER(1),
            active INTEGER(1)
)""")
c.execute("""CREATE TABLE IF NOT EXISTS v (
            count INTEGER
)""")
conn.commit()
c.execute("INSERT INTO v VALUES ('0')")
c.execute("SELECT * FROM v")
row = c.fetchone()
print("Version: ", end='')
print(row[0])

v2 = row[0] + 1

c.execute("UPDATE version SET ver = 'b 0.3.0.%s Stable'" % (v2))
c.execute("UPDATE v SET count = %s" % (v2))

c.execute("INSERT INTO version VALUES ('0.3.0 Stable')")

row = c.fetchall()
print(row)
conn.commit()

conn.close()
def ex():
    pass

print("Init done.")

con = None

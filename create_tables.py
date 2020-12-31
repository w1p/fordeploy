import sqlite3

conn = sqlite3.connect("mydata.db")
cs = conn.cursor()

create_table = "create table if not exists users (id integer primary key, username text, password text)"
cs.execute(create_table)

create_table = (
    "create table if not exists items (id integer primary key, name text, price real)"
)
cs.execute(create_table)

# cs.execute("insert into items(name, price) values ('piano', 100000) ")
conn.commit()
conn.close()
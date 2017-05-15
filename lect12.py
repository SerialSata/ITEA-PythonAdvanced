# PEP 249
import sqlite3

db = sqlite3.connect('db.sqlite3')
print(db)

cursor = db.cursor()
print(cursor)

c1 = cursor.execute('select * from students')

for row in c1:
    print(row)

# cursor.execute('insert into students (name, subj, mark) values (?, ?, ?);', ('Bob', 'math', 4))

print(row)
fields = ('id', 'name', 'subj', 'mark')

print(list(zip(fields, row)))

r = dict(zip(fields, row))
print(r)
print(r['name'])

db.commit()
cursor.close()
db.close()

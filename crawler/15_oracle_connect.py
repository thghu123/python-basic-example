import cx_Oracle

conn = cx_Oracle.connect("class11/class11@localhost:1521:orcl")
cursor = conn.cursor()
sql = "select * from bbs"

cursor.execute(sql)
for row in cursor:
    for i in range(len(row)):
        if i==3:
            description = row[3].read()
        print(row[i], end = " ")
    print()

cursor.close()
conn.close()


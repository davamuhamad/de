import mysql.connector as mysql 

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()

str = '''Insert into pegawai(nip,nama,seks,gaji)
        values(%s,%s,%s,%s)'''
values = [
    ("008","RINA","W",2100000),
    ("009","TONO","P",1700000),
    ("010","MIRA","W",2100000)
]

for val in values:
    cursor.execute(str,val)
    conn.commit()

cursor.close()
conn.close()
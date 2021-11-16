import mysql.connector as mysql 

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()

str = '''Insert into pegawai(nip,nama,seks,gaji)
        values(%s,%s,%s,%s)'''
val = ("006","DANIK","W",2100000)

cursor.execute(str,val)
conn.commit()

print("Sebanyak {} data telah ditambahkan ".format(cursor.rowcount))

cursor.close()
conn.close()
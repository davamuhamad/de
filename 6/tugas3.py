import mysql.connector as mysql 

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()

str = '''Insert into departemen(kodedept,namadept)
        values(%s,%s)'''
val = ("08","FASHION")

cursor.execute(str,val)
conn.commit()

print("Sebanyak {} data telah ditambahkan ".format(cursor.rowcount))

cursor.close()
conn.close()
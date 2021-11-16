import mysql.connector as mysql 
import pandas as pd 

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()
str = '''select seks , count(*) as jumlah 
        from pegawai 
        group by seks '''
cursor.execute(str)
datas = cursor.fetchall()

df = pd.DataFrame(datas)
print("Ditemukan {} data".format(cursor.rowcount))
print(df)

cursor.close()
conn.close()
import mysql.connector as mysql 
import pandas as pd 

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()
str = '''select d.namadept, count(b.kodebrg) as Total_barang , sum(b.stok) as jumlah_stok from kelompok k 
join departemen d on k.kodedept = d.kodedept 
join barang b on k.kodeklmpk = b.kodeklmpk 
group by d.namadept 
'''
cursor.execute(str)
datas = cursor.fetchall()

df = pd.DataFrame(datas)
print("Ditemukan {} data".format(cursor.rowcount))
print(df)

cursor.close()
conn.close()
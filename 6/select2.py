import mysql.connector as mysql 
conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

cursor = conn.cursor()
cursor.execute("SELECT * FROM pegawai")
datas = cursor.fetchall()
for data in datas:
    print("NIP : ",data[0]," Nama : ",data[1]," Sex : ",data[2]," Gaji : ",data[3])
cursor.close()
conn.close()
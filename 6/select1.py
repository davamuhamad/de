import mysql.connector as mysql

conn = mysql.connect(host='localhost',user = 'root',password = '',database = 'kantor')

if conn.is_connected():
    print("Berhasil Koneksi")
    conn.close()
else:
    print("Gagal Konek")
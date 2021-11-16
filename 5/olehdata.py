#import lib operating system untuk fungsi bersihkan layar
import os
#buat variabel global
data = []
ke = 0

def tambahdata():
    bersihkanlayar()
    global ke 
    jawab = 'y'
    while (jawab.lower() == 'y'):
        ke+=1
        print("Data Ke-",str(ke))
        nama = input("Nama : ")
        nilai = int(input("Nilai : "))
        #memasukan nama dan nilai ke dalam list dengan bentuk dictionary
        data.append({"nama":nama,"nilai":nilai})
        #meminta masukan lanjut atau tidak
        jawab = input("isi lagi (y/t) ? : ")

def tampildata():
    bersihkanlayar()
    no = 0 
    for dt in data:
        no+=1
        print(no,"%s \t %d"%(dt['nama'], dt['nilai']))
    tunggu()

def hapusdata():
    global data
    namadihapus = input("Isikan Nama yang akan dihapus : ")
    #metode khusus untuk menghapus data dictionary dalam list
    data = [i for i in data if not(i['nama'] == namadihapus)]
    print("Data "+namadihapus+" Sudah dihapus...")
    tunggu()

def bersihkanlayar():
    os.system("clear")

def tunggu():
    a = input("Tekan ENTER untuk lanjut...")

#program utama
pilih = 1 
while(pilih  != 0 ):
    bersihkanlayar()
    print("==MENU==")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Hapus Data")
    print("0. Keluar")
    print("")

    pilih = int(input("Pilihan Anda : "))
    if (pilih == 1):
        tambahdata()
    elif(pilih == 2):
        tampildata()
    elif(pilih == 3):
        hapusdata()
    else:
        print("Selesai")
def cekbilangan(bilangan):
    if (bilangan % 2 == 0 ):
        hasil = "GENAP"
    else:
        hasil = "GANJIL"
    return hasil

angka = int(input("Masukan Sembarang Nilai : "))
hasilcek = cekbilangan(angka)
print("Hasil pengecekan %d adalah bilangan %s "%(angka, hasilcek))
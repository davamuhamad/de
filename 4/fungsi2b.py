def cekbilangan(bilangan):
    if bilangan < 0:
        hasil = "Negatif"
    elif bilangan > 0:
        hasil = "Positif"
    elif bilangan == 0:
        hasil = "NOL"
    return hasil

angka = int(input("Masukan Sembarang Nilai : "))
hasilcek = cekbilangan(angka)
print("Hasil pengecekan %d adalah bilangan %s "%(angka, hasilcek))
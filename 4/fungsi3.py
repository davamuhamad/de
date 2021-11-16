def pembagian(pembilang,penyebut):
    if penyebut == 0 :
        hasil = "Penyebut dalam pembagian tidak boleh NOL"
    else:
        hasil = pembilang / penyebut
    return hasil

x = 75
y = 0
result = pembagian(x,y)
print("Hasil Bagi = ",result)
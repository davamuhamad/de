tp = int(input("Masukan nilai total belanja anda : "))
if tp > 100000:
    print("Selamat anda mendapat potongan 15000")
    print("Total harga yang harus dibayar = ",tp-15000)
else:
    print("Total Pembelian = ",tp)
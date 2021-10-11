usia = int(input("Masukan Usia Anda : "))
tb = float(input("Masukan data tinggi badan anda : "))
if usia > 40:
    print("Anda terlalu tua untuk mendaftar")
elif usia < 17:
    print("Anda belum boleh mendaftar")
else:
    if tb < 160:
        print("Tinggi badan anda tidak memnuhi syarat untuk menjadi pebasket ")
    else:
        print("Oke, Silahkan anda lanjutkan untuk ikut test Fisik ya")
#DOC PDE 195611102

#Deklarasi List 
list_nilai = [1,2,3,4,5,6,7,8,9,10]
#Tampilkan List
print("List Nilai : \n",list_nilai)
#menggunakan len 
print("\nBanyak item list nilai (len) : ",len(list_nilai))
#menggunakan append
print("\nMenambah Element 12 dan 5 dalam list (append) : ")
list_nilai.append(12)
list_nilai.append(5)
print("List Nilai Baru : \n",list_nilai)
#menggunakan count 
print("\nBanyak Nilai dalam 5 dalam list (count) : \n",list_nilai.count(5))
#menggunakan INdex
print("\nAngka 8 ada di posisi index ke : \n", list_nilai.index(8))
#Mengguanakan Insert
list_nilai.insert(1,22)
print("\nTambah Nilai List (insert) : \n",list_nilai)
#Menggunakan pop
list_nilai.pop()
list_nilai.pop()
print("\nList Nilai (pop) : \n",list_nilai)
#menggunakan remove
list_nilai.remove(2)
list_nilai.remove(1)
print("\nList Nilai (remove) : \n",list_nilai)
#menggunakan extend
list_nilai2 = [4,3,8,7]
list_nilai.extend(list_nilai2)
print("\nList Nilai (extend) : \n",list_nilai)
#menggunakan reverse
list_nilai.reverse()
print("\nList Nilai (reverse) : \n",list_nilai)
#menggunakan Sort
list_nilai.sort()
print("\nList Nilai (sort) : \n",list_nilai)
#menggunakan Max
print("\nList Nilai (max) : \n",max(list_nilai))
#menggunakan Min
print("\nList Nilai (min) : \n",min(list_nilai))
#menggunakan Sum
print("\nTOtal Penjumlahan nilai dari list nilai (sum) : \n",sum(list_nilai))
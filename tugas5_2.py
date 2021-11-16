kesenian = {'adi','siti','rudi','doni'}
mapala = {'rudi','sigit','doni','andi'}

print("Mahasiswa yang tidak ikut mapala adalah : ",kesenian - mapala)
print("Mahasiswa yang ikut di kedua UKM adalah : ",kesenian & mapala)
print("Semua data mahasiswa ukm : ",kesenian | mapala)
print("Anggota mapala yang tidak ikut kesenian : ",mapala - kesenian)
print("Mahasiswa yang hanya mengikut 1 ukm saja : ",kesenian ^ mapala)

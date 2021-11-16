
def convert(uts,uas,ta):
    na = (uts*30/100) + (uas*30/100) + (ta*40/100)
    print("Nilai akhir anda : ",na)
    if (na <= 100 and na >= 81):
        nilai = "A"
    elif (na <= 80 and na >= 61):
        nilai = "B"
    elif (na <= 60 and na >= 41):
        nilai = "C"
    elif (na <= 40 and na >= 21):
        nilai = "D"
    elif na <= 20:
        nilai = "E"
    return nilai

uts = int(input("Nilai UTS : "))
uas = int(input("Nilai UAS : "))
ta = int(input("Nilai Tugas : "))
nilai_akhir = convert(uts,uas,ta)
print("Anda mendapa nilai : ",nilai_akhir)
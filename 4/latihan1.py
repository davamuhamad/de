def bingkai(str):
    pjg = len(str)
    garis(pjg)
    cetak(str)
    garis(pjg)

def cetak(str):
    print("| ",str," |")

def garis(pjg):
    print("+",end='')
    for i in range(pjg+2):
        print("-",end='')
    print("+")

bingkai("Halo Pa Kabar")
bingkai("Ini adalah tulisan yang otomatis ada didalm kotak")
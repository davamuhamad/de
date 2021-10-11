ips = float(input("IP Semester Anda : "))
if ips > 3 :
    print("Anda boleh mengambil maksimal 24 SKS")
elif ips > 2.75:
    print("Anda boleh mengambil maksimal 21 SKS")
elif ips >= 2.00:
    print("Anda boleh mengambil maksimal 18 SKS")
else:
    print("Anda boleh mengambil maksimal 12 SKS")
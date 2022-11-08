

import os
os.system('clear')
name = input("Masukkan nama :")
os.system('clear')

minum = int(input("Jumlah minuman :"))
tBayar = 5 * int(minum)

print("Total bayar :",tBayar, "Dollar")
os.system('clear')

jUang = 0
x = 0
data = []
while jUang < tBayar:
    temp = int(input("Masukkan uang : "))
    if temp == 2 or temp == 5 or temp == 10:
        data.append(temp)
        jUang += data[x]
        x = x + 1
    else:
        print("Bukan 2 / 5 / 10 Dollar")

print()
kembalian = int(jUang) - int(tBayar)
print("Nama pembeli   :",name)
print("Jumlah Minuman :",minum, "buah")
print("Total bayar    :",tBayar, "Dollar")
print("Bayar          :",jUang, "Dollar")
print("Kembalian      :",kembalian, "Dollar")
print()
print("Terima kasih",name,", Uang kembalian :",kembalian,"Dollar")
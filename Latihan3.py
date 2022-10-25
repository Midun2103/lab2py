"""
Nama    = Midun Hakiki
Nim     = 312210583
"""


# input nilai variable
a=input("Masukan nilai a:")
b=input("Masukan nilai b:")

# cetak nilai variable
print("variable a=",a)
print("variable b=",b)

# cetak hasil operasi kedua variabel dengan string
print("hasil penggabung {1} & {0} = ".format(a,b) + (8    a + b))

# konversi nilai
a=int(a)
b=int(b)
print("hasil penjumlahan {1} + {0} = %d". format(a,b) % (a+b))
print("hasil pembagian {1} / {0} = %d". format(a,b) % (a/b))
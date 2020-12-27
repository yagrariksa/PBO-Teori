print("==================BISMILLAH====================")
print()
print("Nama = M.Segaf Isa A.")
print("NIM  = 082011633047")
print()
print("=========MASIHBELAJARJADISANTUYSAJA========")
print()
a = int(input('bilangan a = '))
b = int(input('bilangan b = '))
def removekembar(a,b):
    arra = []
    arrb = []
    akandihapus = []
    while a>=1 :
        simpan = a%10
        a = ((a-simpan)//10)
        arra.append(simpan)
    while b>=1 :
        simpan = b%10
        b = ((b-simpan)//10)
        arrb.append(simpan)
    na = len(arra)
    nb = len(arrb)
    for i in range (na):
        for j in range (nb):
            c=arra[i]
            b=arrb[j]
            if c == b :
                akandihapus.append(i)
            print ("array a awal = ",c)
    for k in akandihapus:
        arra.pop(k)
        print ("akan dihapus = ",k)
    for l in arra:
        print ("hasil = ",l)
        
removekembar(a,b)





print()
print()
print("==========NEVERGIVEUP==========")
print()
print()
print()

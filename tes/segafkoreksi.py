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
    # na = len(arra)
    # nb = len(arrb)
    for i in range (len(arra)): #berubah
        for j in range (len(arrb)): #berubah
    #         c=arra[i]
    #         d=arrb[j]
            if arra[i] == arrb[j] :
                akandihapus.append([i,j])
            # print ("array a awal = ",c)
    print(akandihapus)
    for k in akandihapus:
        arra.pop(k[0])
        arrb.pop(k[1])
        print("k -> ", k[0])
        # print ("akan dihapus = ",k)
    # for l in arra:
        # print ("hasil = ",l)
    # print("sisa array =", arra )
    print(arra,arrb)
        
removekembar(a,b)





print()
print()
print("==========NEVERGIVEUP==========")
print()
print()
print()

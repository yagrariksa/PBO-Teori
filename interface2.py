class Aklas():
    NILAI_A = 0
    def __init__(self,a):
        self.NILAI_A = a

    def hitungKali(self,a,b):
        hasil = a*b
        return hasil

class Bklas():
    NILAI_B = 0
    def __init__(self,b):
        self.NILAI_B = b

    def getB(self):
        return self.NILAI_B

    def hitungKurang(self,a,b):
        hasil = a-b
        return hasil

class Cklas(Bklas):
    NILAI_C = 0
    def __init__(self,c):
        self.NILAI_C = c

    def hitungKali(self,a,b):
        hasil = a*b
        return hasil

    def tampilBC(self,obj):
        print("B :",obj.getB(), "& C :",self.NILAI_C)

    def tamiplKonstanta(self,obja,objb):
        print(obja.NILAI_A,"&",objb.NILAI_B)


aklas = Aklas(2)
bklas = Bklas(3)
cklas = Cklas(4)

print("2*2 =",aklas.hitungKali(2,2))
print("B : ", bklas.getB())
print("4-2 =", bklas.hitungKurang(4,2))
cklas.tampilBC(bklas)
cklas.tamiplKonstanta(aklas,bklas)

    
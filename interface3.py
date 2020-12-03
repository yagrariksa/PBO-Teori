class Aklas():
    NILAI_A = 0

    def hitungkali(self,a,b):
        hasil  = a*b
        return hasil

class Bklas():
    NILAI_B = 0
        
    def hitungkurang(self,a,b):
        hasil = a-b
        return hasil

class Cklas(Aklas,Bklas):
    NILAI_C = 0

    def __init__ (self,a,b,c):
        self.NILAI_A = a
        self.NILAI_B = b
        self.NILAI_C = c

    def hitungjumlah(self,a,b):
        hasil = a+b
        return hasil

class Dklas():

    def __init__(self,a):
        self.d = a

    def tampilD(self):
        return self.d

    def tampilkonstanta(self,obj):
        print("A", obj.NILAI_A,"B", obj.NILAI_B,"C", obj.NILAI_C)

    def hitungkurang(self,a,b):
        hasil = a-b
        return hasil

    def hitungkali(self,a,b):
        hasil  = a*b
        return hasil

    def hitungjumlah(self,a,b):
        hasil = a+b
        return hasil

cklas = Cklas(3,4,5)
dklas = Dklas(2)

dklas.tampilkonstanta(cklas)
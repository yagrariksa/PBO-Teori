# Buatlah program yang di dalamnya ada class vektor dengan beberapa member function untuk menghitung cosinus sudut antara dua vektor dengan ketentuan sebagai berikut :
class Vektor():

    def __init__(self, arg=False):
        self.vek = []
        if (arg):
            for i in range(3):
                string = 'masukan ke-' + str(i) + ' : '
                x = input(string)
                self.vek.append(int(x))

    def tampil(self):
        print(self.vek)

    def panjangkuadrat(self, b):
        v2 = Vektor()
        for i in range(len(self.vek)):
            x = self.vek[i]-b.vek[i]
            x = x**2
            v2.vek.append(int(x))
        total = 0
        for i in v2.vek:
            total += i
        return total

    def panjang(self, b):
        v2 = Vektor()
        for i in range(len(self.vek)):
            x = self.vek[i]-b.vek[i]
            v2.vek.append(int(x))
        total = 0
        for i in v2.vek:
            total += i
        return total

    def input(self, vektor):
        self.vek = vektor

    def print(self):
        print(self.vek)


A = Vektor()
A.vek = [4, 4, 4]
B = Vektor()
B.vek = [2, 2, 2]
C = Vektor()
C.vek = [1, 1, 1]

print("method print :")
A.print()
B.print()
C.print()

cos = (A.panjangkuadrat(B)+A.panjangkuadrat(C) -
       B.panjangkuadrat(C))/(2*A.panjang(B)*A.panjang(C))
print(cos)

# a)     Vektor A=(a1, a2, a3) , B=(b1, b2, b3) dan B=(c1, c2, c3)

# b)    Panjang  vektor AB dinotasikan |AB|2 = (a1-b1)2 + ( a2-b2)2 + ( a3-b3)2

# c)     Panjang  vektor AC dinotasikan |AC|2 = (a1-c1)2 + ( a2-c2)2 + ( a3-c3)2

# d)    Panjang  vektor BC dinotasikan |BC|2 =  (b1-c1)2 + ( b2-c2)2 + ( b3-c3)2

# e)     cos alfa = (|AB|2 + |AC|2 -  |BC|2)/(2* |AB| * |AC| )

# f)     Tampilkan data dalam format :  (..., ..., ..., ...)

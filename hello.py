#!/usr/bin/env python3

class Vektor:

    def __init__(self, n=0):
        self.vek = []
        for i in range(n):
            string = 'input ' + str(i) + ' : '
            x = input(string)
            print(x)
            self.vek.append(int(x))

    def tampil(self):
        print(self.vek)

    def jumlah(self, a, b=None):
        if b is None:
            v2 = Vektor(0)
            for i in range(len(self.vek)):
                x = self.vek[i]+a.vek[i]
                v2.vek.append(int(x))
            return v2
        else:
            v2 = Vektor(0)
            for i in range(len(a.vek)):
                x = a.vek[i]+b.vek[i]
                v2.vek.append(int(x))
            return v2

    def kurang(self, a, b=None):
        if b is None:
            v2 = Vektor()
            for i in range(len(self.vek)):
                x = self.vek[i]-a.vek[i]
                v2.vek.append(int(x))
            return v2
        else:
            v2 = Vektor()
            for i in range(len(a.vek)):
                x = a.vek[i]-b.vek[i]
                v2.vek.append(int(x))
            return v2


print("############# nomor 1 >>>>>>>>>>")
pet = Vektor(3)
pot = Vektor(3)
pet.tampil()
print(pot.vek)
p3 = pot.jumlah(pet)
p3.tampil()
p4 = p3.kurang(pet, pot)
p4.tampil()


class Matriks:
    def __init__(self, x, y):
        self.matriks = []
        for i in range(x):
            aa = []
            for j in range(y):
                string = 'masukkan ', i, '-', j, ' : '
                aa.append(int(input(string)))
            self.matriks.append(aa)

    def tampil(self):
        for i in self.matriks:
            print(i)


print("############# nomor 2 >>>>>>>>>>")
m1 = Matriks(3, 4)
m1.tampil()


class Array2DimBedaElemen:
    def __init__(self, a):
        self.arr = []
        for i in range(3):
            aa = []
            for j in range(a[i]):
                aa.append(int(input('input: ')))
            self.arr.append(aa)

    def tampil(self):
        for i in self.arr:
            print(i)


print("############# nomor 3 >>>>>>>>>>")
t3 = Array2DimBedaElemen([3, 2, 4])
t3.tampil()


class Array3DimSama:
    def __init__(self, a, b, c):
        self.arr = []
        for i in range(a):
            barr = []
            for j in range(b):
                carr = []
                for k in range(c):
                    carr.append(int(input('input: ')))
                barr.append(carr)
            self.arr.append(barr)

    def tampil(self):
        for i in self.arr:
            for j in i:
                print(j)
            print('-')


print("############### nomor 4 >>>>>>>>>")
t4 = Array3DimSama(3, 2, 3)
t4.tampil()

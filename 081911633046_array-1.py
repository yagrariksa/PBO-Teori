
class Vektor:

    def __init__(self, n=0):
        self.vek = []
        for i in range(n):
            str = 'masukan ke-', i, ' : '
            x = input(str)
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

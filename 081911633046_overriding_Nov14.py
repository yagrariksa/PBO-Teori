class Vehicle:
    def start(self):
        print("Vehicle start code")

    def stop(self):
        print("Vehicle stop code")


class Car(Vehicle):
    def __init__(self, nbOfSeats):
        self.nbOfSeats = nbOfSeats

    def getNbOfSeats(self):
        return self.nbOfSeats


class BendaBulat():
    def __init__(self, radius, warna):
        self.radius = radius
        self.warna = warna

    def getRadius(self):
        return self.radius

    def getWarna(self):
        return self.warna

    def display(self):
        print("\nradius : ", self.getRadius())
        print("warna : ", self.getWarna())


class Tabung(BendaBulat):
    def __init__(self, radius, warna, tinggi):
        super().__init__(radius, warna)
        self.tinggi = tinggi

    def getTinggi(self):
        return self.tinggi

    def display(self):
        super().display()
        print("tinggi : ", self.getTinggi())


class BendaPersegi():
    def __init__(self, panjang, lebar, warna='merah'):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def getPanjang(self):
        return self.panjang

    def getLebar(self):
        return self.lebar

    def getWarna(self):
        return self.warna

    def display(self):
        print("\nPanjang : ", self.getPanjang())
        print("Lebar : ", self.getLebar())
        print("Warna : ", self.getWarna())


class Balok(BendaPersegi):
    def __init__(self, panjang, lebar, tinggi, warna='merah'):
        super().__init__(panjang, lebar, warna)
        self.tinggi = tinggi

    def getTinggi(self):
        return self.tinggi

    def display(self):
        super().display()
        print("Tinggi : ", self.getTinggi())
        print("Volume : ", self.volume())

    def volume(self):
        return self.getTinggi()*self.getPanjang()*self.getLebar()


print("Daffa Yagrariksa Ramadhan")
print("081911633046")

car1 = Car(2)
vehicle1 = Vehicle()
car2 = Car(4)

print("\nCAR 1 -> car")
car1.start()
print("number of seats : ",  car1.getNbOfSeats())
car1.stop()

print("\nVEHICLE 1 -> Vehicle")
vehicle1.start()
vehicle1.stop()

print("\nCAR 2 -> car")
car2.start()
print("number of seats : ", car2.getNbOfSeats())
car2.stop()

tb1 = Tabung(5, 'coklat', 3)
bb1 = BendaBulat(7, 'ungu')
tb2 = Tabung(4, 'merah', 8)
tb1.display()
bb1.display()
tb2.display()

tb1 = Balok(1, 2, 3)
bb1 = BendaPersegi(1, 2, 'hijau')
tb2 = Balok(4, 5, 6, 'kuning')
tb1.display()
bb1.display()
tb2.display()

print("\nHello world")

print("Daffa Yagrariksa Ramadhan")
print("081911633046")

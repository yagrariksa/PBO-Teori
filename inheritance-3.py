class Shape():
    def __init__(self, n):
        self._name = n

    def getName(self):
        return self._name

    def calculateArea(self):
        pass

    def displayName(self):
        print("Name : ", self.getName())

    def display(self):
        self.displayName()
        print("luas area : ", self.calculateArea(), "\n")


class Circle(Shape):
    def __init__(self, n, r):
        super().__init__(n)
        self._r = float(r)

    def getR(self):
        return self._r

    def calculateArea(self):
        pi = 22/7
        rkuadrat = self.getR()**2
        luas = pi*rkuadrat
        return luas


class Square(Shape):
    def __init__(self, n, s):
        super().__init__(n)
        self._s = float(s)

    def getS(self):
        return self._s

    def calculateArea(self):
        luas = self.getS()**2
        return luas


print("Daffa Yagrariksa Ramadhan")
print("081911633046\n")

a = float(input('masukan jari-jari lingkaran : '))
b = float(input('masukan panjang sisi : '))
print()

ling = Circle('lingkaran', a)
kotak = Square('kotak', b)

ling.display()
kotak.display()

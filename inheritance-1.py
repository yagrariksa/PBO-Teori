class B():
    def __init__(self, a, b):
        self._a = float(a)
        self._b = float(b)

    def getA(self):
        return self._a

    def getB(self):
        return self._b

    def showA(self):
        print("a : ", self.getA())

    def showB(self):
        print("b : ", self.getB())


class D(B):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.mul()
        self.dev()

    def mul(self):
        self._c = self.getA()*self.getB()

    def dev(self):
        self._d = self.getA()/self.getB()

    def display(self):
        self.showA()
        self.showB()
        print("c : ", self._c)
        print("d : ", self._d)


print("Daffa Yagrariksa Ramadhan")
print("081911633046\n")
a = int(input('masukan a : '))
b = int(input('masukan b : '))
variabel = D(a, b)
variabel.display()

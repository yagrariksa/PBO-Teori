class Student():
    def __init__(self, a=0):
        self._rollNumber = a

    def getNumber(self):
        return self._rollNumber

    def putNumber(self):
        return print("roll Number : ", self.getNumber())


class Test(Student):
    def __init__(self, a, b, c):
        super().__init__(a)
        self._sub1 = float(b)
        self._sub2 = float(c)

    def getSub1(self):
        return self._sub1

    def getSub2(self):
        return self._sub2

    def putMarks(self):
        print("Sub1 : ", self.getSub1())
        print("Sub2 : ", self.getSub2())


class Result(Test):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.setTotal()

    def setTotal(self):
        self._total = self.getSub1() + self.getSub2()

    def getTotal(self):
        return self._total

    def display(self):
        self.putNumber()
        self.putMarks()
        print("total : ", self.getTotal())


print("Daffa Yagrariksa Ramadhan")
print("081911633046\n")

a = int(input('masukan roll number : '))
b = float(input('masukan sub1 : '))
c = float(input('masukan sub2 : '))
print()

variabel = Result(a, b, c)
variabel.display()

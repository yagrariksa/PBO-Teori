
class Matriks:
    def __init__(self, x=0, y=0):
        self.matriks = []
        for i in range(x):
            aa = []
            for j in range(y):
                string = 'input ' + str(i) + '-' + str(j) + ' : '
                aa.append(int(input(string)))
            self.matriks.append(aa)

    def tampil(self):
        for i in self.matriks:
            print(i)

    def jumlah(self, a):
        m3 = []
        for i in range(len(a.matriks)):
            m4 = []
            for j in range(len(a.matriks[i])):
                m4.append(self.matriks[i][j]+a.matriks[i][j])
            m3.append(m4)
        return m3

    def kurang(self, a):
        m3 = []
        for i in range(len(a.matriks)):
            m4 = []
            for j in range(len(a.matriks[i])):
                m4.append(self.matriks[i][j]-a.matriks[i][j])
            m3.append(m4)
        return m3


print("############# nomor 2 >>>>>>>>>>")
a = int(input('masukan baris : '))
b = int(input('masukan kolom : '))
m1 = Matriks(a, b)
m2 = Matriks(a, b)
print("####################")
m1.tampil()
print("####################")
m2.tampil()
print("####################")
m3 = Matriks()
m3.matriks = m1.jumlah(m2)
m3.tampil()


class Matriks:
    def __init__(self, x, y):
        self.matriks = []
        for i in range(x):
            aa = []
            for j in range(y):
                string = 'masukkan ', i, j, ' : '
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


print("############# nomor 2 >>>>>>>>>>")
m1 = Matriks(3, 4)
m2 = Matriks(3, 4)
m1.tampil()
print("####################")
m2.tampil()
print("####################")
m3 = m1.jumlah(m2)
m3

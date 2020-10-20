
class Array2DimBedaElemen:
    def __init__(self, a=0, b=[]):
        self.arr = []
        print(">>>>>>>>>>>>")
        for i in range(a):
            aa = []
            for j in range(b[i]):
                string = 'input ' + str(i) + '-' + str(j) + ' : '
                aa.append(int(input(string)))
            self.arr.append(aa)

    def tampil(self):
        for i in self.arr:
            print(i)

    def jumlah(self, a):
        m3 = []
        for i in range(len(a.arr)):
            m4 = []
            for j in range(len(a.arr[i])):
                m4.append(self.arr[i][j]+a.arr[i][j])
            m3.append(m4)
        return m3

    def kurang(self, a):
        m3 = []
        for i in range(len(a.arr)):
            m4 = []
            for j in range(len(a.arr[i])):
                m4.append(self.arr[i][j]-a.arr[i][j])
            m3.append(m4)
        return m3


print("############# nomor 3 >>>>>>>>>>")
a = int(input('masukan jumlah baris : '))
b = []
for i in range(a):
    string = 'masukan jumlah kolom ke ' + str(i) + ' : '
    c = int(input(string))
    b.append(c)
t3 = Array2DimBedaElemen(a, b)
t4 = Array2DimBedaElemen(a, b)
t5 = Array2DimBedaElemen()
t5.arr = t3.jumlah(t4)
t6 = Array2DimBedaElemen()
t6.arr = t3.kurang(t4)
print("####################")
t3.tampil()
print("####################")
t4.tampil()
print("####################")
t5.tampil()
print("####################")
t6.tampil()

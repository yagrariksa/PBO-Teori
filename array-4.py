
class Array3DimSama:
    def __init__(self, a=0, b=0, c=0):
        self.arr = []
        print()
        for i in range(a):
            barr = []
            for j in range(b):
                carr = []
                for k in range(c):
                    string = 'input ' + str(i) + '-' + \
                        str(j) + '-'+str(k)+' : '
                    carr.append(int(input(string)))
                barr.append(carr)
            self.arr.append(barr)

    def tampil(self):
        print("##################")
        for i in self.arr:
            print('-')
            for j in i:
                print(j)

    def jumlah(self, a):
        barr = []
        for i in range(len(a.arr)):
            carr = []
            for j in range(len(a.arr[i])):
                darr = []
                for k in range(len(a.arr[i][j])):
                    darr.append(self.arr[i][j][k]+a.arr[i][j][k])
                carr.append(darr)
            barr.append(carr)
        return barr

    def kurang(self, a):
        barr = []
        for i in range(len(a.arr)):
            carr = []
            for j in range(len(a.arr[i])):
                darr = []
                for k in range(len(a.arr[i][j])):
                    darr.append(self.arr[i][j][k]-a.arr[i][j][k])
                carr.append(darr)
            barr.append(carr)
        return barr


print("############### nomor 4 >>>>>>>>>")
a = int(input('masukan ukuran dimensi 1 : '))
b = int(input('masukan ukuran dimensi 2 : '))
c = int(input('masukan ukuran dimensi 3 : '))
t4 = Array3DimSama(a, b, c)
t5 = Array3DimSama(a, b, c)
t4.tampil()
t5.tampil()
t6 = Array3DimSama()
t6.arr = t4.jumlah(t5)
t6.tampil()

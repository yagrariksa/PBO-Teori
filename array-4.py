
class Array3DimSama:
    def __init__(self, a, b, c):
        self.arr = []
        for i in range(a):
            barr = []
            for j in range(b):
                carr = []
                for k in range(c):
                    string = 'input', i, j, k, ' : '
                    carr.append(int(input(string)))
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

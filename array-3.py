
class Array2DimBedaElemen:
    def __init__(self, a, b):
        self.arr = []
        for i in range(a):
            aa = []
            for j in range(b[i]):
                string = 'input ', i, j, ' : '
                aa.append(int(input(string)))
            self.arr.append(aa)

    def tampil(self):
        for i in self.arr:
            print(i)


print("############# nomor 3 >>>>>>>>>>")
t3 = Array2DimBedaElemen(4, [3, 2, 4, 1])
t3.tampil()

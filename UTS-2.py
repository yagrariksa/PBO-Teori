# Buatlah program yang terdiri dari dua class isiL dan isiG yang di dalamnya menyimpan besaran volume.  isiL memuat ltr (liter) dan dltr (deciliter) sedangkan  isiG memiliki besaran galon  dan pint. Member function yang dipunyai dapat digunakan untuk :

# a.     Memasukkan data dalam  ltr dan dltr untuk class isiL

# b.    Memasukkan data dalam  pint dan galon untuk class isiG

# c.     Penjumlahan dua data dari class isiL dan class isiG kemudian tampilkan data hasil jumlahannya dalam format ....... galon  ........ pint (Ingat! satuan di class isiL dan class isiG berbeda sehingga harus disamakan dulu baru dijumlahkan)

# d.    Tampilkan data dalam format : ....... ltr ........ dltr untuk class isiL

# e.     Tampilkan data dalam format : ....... galon  ........ pint untuk class isiG

#    Catatan : 1 ltr = 2.11337 pint dan 1 galon = 8 pint serta 1 ltr = 10 dltr

class isiL:
    def __init__(self, ltr):
        self.ltr = ltr
        self.dltr = self.ltr*10
        self.pint = self.ltr*2.11337
        self.galon = self.pint/8

    def add(self, obj):
        galon = self.galon+obj.galon
        pint = self.pint+obj.pint
        print(galon, "galon", pint, "pint ")

    def show(self):
        print(
            f"{self.ltr} liter {self.dltr} dltr :: {self.pint} pint {self.galon} galon")


class isiG:
    def __init__(self, galon):
        self.galon = galon
        self.pint = self.galon*8
        self.ltr = self.pint/2.11337
        self.dltr = self.ltr*10

    def add(self, obj):
        galon = self.galon+obj.galon
        pint = self.pint+obj.pint
        print(galon, "galon", pint, "pint ")

    def show(self):
        print(f"{self.galon} galon {self.pint} pint :: {self.ltr} ltr {self.dltr} dltr")


# objek
liter = isiL(1)
liter.show()
galon = isiG(1)
galon.show()
liter.add(galon)

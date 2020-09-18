#!usr/bin/env python3

class Segi4:
	def __init__(self, panjang, lebar):
		self._panjang = panjang
		self._lebar = lebar
	def luasBujurSangkar(self):
		luas = self._panjang**2
		print("luas Bujur Sangkar : ",luas)
	def luasPersegiPanjang(self):
		luas = self._panjang*self._lebar
		print("luas Persegi Panjang : ", luas)
	def setPanjang(self, panjang):
		self._panjang = panjang
	def setLebar(self, lebar):
		self._lebar = lebar
	def getPanjang(self):
		return self._panjang
	def getLebar(self):
		return self._lebar
	def display(self):
		print("panjang : ", self._panjang)
		print("lebar : ", self._lebar)

satu = Segi4(4,6)
satu.display()
satu.luasBujurSangkar()
satu.luasPersegiPanjang()
print("-------------")
satu.setPanjang(2)
satu.setLebar(8)
satu.display()
satu.luasBujurSangkar()
satu.luasPersegiPanjang()


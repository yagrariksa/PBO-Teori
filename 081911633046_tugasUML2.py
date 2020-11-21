#!usr/bin/env python3

class SegiEmpat:
	def __init__(self, panjang, lebar):
		self._panjang = panjang
		self._lebar = lebar

	def luasBujurSangkar(self):
		luas = self._panjang**2
		print("luas Bujur Sangkar : ", luas)
		return luas

	def luasPersegiPanjang(self):
		luas = self._panjang*self._lebar
		print("luas Persegi Panjang : ", luas)
		return luas

	def kelilingBujurSangkar(self):
		keliling = 4*self._panjang
		print("keliling Bujur Sangkar : ", keliling)
		return keliling

	def kelilingPersegiPanjang(self):
		sisi = self._panjang+self._lebar
		keliling = sisi*2
		print("keliling Bujur Sangkar : ", keliling)
		return keliling

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


satu = SegiEmpat(4, 6)
satu.display()
satu.luasBujurSangkar()
satu.luasPersegiPanjang()
satu.kelilingBujurSangkar()
satu.kelilingPersegiPanjang()
print("-------------")
satu.setPanjang(2)
satu.setLebar(8)
satu.display()
satu.luasBujurSangkar()
satu.luasPersegiPanjang()
satu.kelilingBujurSangkar()
satu.kelilingPersegiPanjang()

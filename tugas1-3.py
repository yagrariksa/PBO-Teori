#!usr/bin/env python3

class Segi4:
	def luasBujurSangkar(panjang):
		luas = panjang*panjang
		print("luas Bujur Sangkar : ",luas)
	def luasPersegiPanjang(panjang, lebar):
		luas = panjang*lebar
		print("luas Persegi Panjang : ", luas)

Segi4.luasBujurSangkar(4)
Segi4.luasPersegiPanjang(4,6)

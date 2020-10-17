#!/usr/bin/env python3

class BendaBulat:
	def __init__(self, radius=2, tinggi=2):
		self._radius = radius
		self._tinggi = tinggi

	def luaslingkaran(self):
		pi = 22/7
		rk = self._radius**2
		self._luas = pi*rk
		print("luas : ", self._luas)
		return self._luas

	def volumesilinder(self):
		volume = self.luaslingkaran() * self._tinggi
		print("volume silinder : ", volume)
		return volume

	def luaspermukaan(self):
		a = 22/7
		b = 2*a*self._radius
		c = self._radius + self._tinggi
		d = b*c
		print("luas permukaan : ", d)
		return d

	def volumebola(self):
		pi = 22/7
		rk = self._radius**3
		vol = 4/3*pi*rk
		print("volume bola : ", vol)
		return vol


print("========CLASS PERTAMA========")
benbul = BendaBulat(7, 4)
benbul.luaslingkaran()
benbul.volumesilinder()
benbul.luaspermukaan()
benbul.volumebola()


class BendaSegi4:
	def __init__(self, panjang=1, lebar=1, tinggi=1):
		self._panjang = panjang
		self._lebar = lebar
		self._tinggi = tinggi

	def luasBujurSangkar(self):
		luas = self._panjang**2
		return luas

	def volumeKubus(self):
		volume = self._panjang**3
		return volume

	def luasPersegiPanjang(self):
		luas = self._panjang * self._lebar
		return luas

	def volumeBalok(self):
		volume = self.luasPersegiPanjang()*self._tinggi
		return volume


print("========CLASS KEDUA========")
benpat = BendaSegi4(2, 3, 4)
print("luas bujur sangkar : ", benpat.luasBujurSangkar())
print("volume kubus : ", benpat.volumeKubus())
print("luas persegi panjang : ", benpat.luasPersegiPanjang())
print("volume Balok : ", benpat.volumeBalok())

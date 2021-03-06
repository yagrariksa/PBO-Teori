#!/usr/bin/env python3

class Vektor:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def jumlah(self, a, b=None):
		if b is None:
			v2 = Vektor(self.x+a.x, self.y+a.y, self.z+a.z)
			return v2
		else:
			v2 = Vektor(a.x+b.x, a.y+b.y, a.z+b.z)
		return v2

	def tampil(self,a=None):
		if a is None:
			print(self.x, self.y, self.z)
		else:
			print(a.x, a.y, a.z)

	def selisih(self, a, b=None):
		if b is None:
			v2 = Vektor(self.x-a.x, self.y-a.y, self.z-a.z)
			return v2
		else:
			v2 = Vektor(a.x-b.x, a.y-b.y, a.z-b.z)
			return v2


v1 = Vektor(2, 3, 4)
v2 = Vektor(1, 1, 1)
v3 = v1.jumlah(v2)
v3.tampil()
v4 = v1.jumlah(v2, v3)
v4.tampil()
v5 = v1.selisih(v2)
v5.tampil()
v6 = v1.selisih(v5, v2)
v6.tampil()
v6.tampil(v1)

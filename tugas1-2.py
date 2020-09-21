#!usr/bin/env python3

class Bulat:
	def __init__(self, jari):
		# variabel protected	
		self._jari = jari
	def luas(self):
		a = self._jari**2
		b = 22/7
		c = a*b
		print("luas : ",c)
		return c
	def volume(self):
		a = 4/3
		b = 22/7
		c = self._jari**3
		d = a*b*c
		print("volume : ",d)
		return d
	def setJari(self, jari):
		self._jari = jari
	def getJari(self):
		return self._jari

satu = Bulat(7)
print("jari : ", satu.getJari())
satu.luas()
satu.volume()

satu.setJari(14)
print("jari : ", satu.getJari())
satu.luas()
satu.volume()

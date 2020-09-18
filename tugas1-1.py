#!usr/bin/env python3

class Bulat:
	def luas(jari):
		a = jari**2
		b = 22/7
		c = a*b
		print("luas : ",c)
	def volume(jari):
		a = 4/3
		b = 22/7
		c = jari**3
		d = a*b*c
		print("volume : ",d)

jari1 = 7
jari2 = 14
Bulat.luas(jari1)
Bulat.volume(jari1)
Bulat.luas(jari2)
Bulat.volume(jari2)

#!/usr/bin/env python3

class Luas:
	def persegi(x):
		luas = x**2
		print("luas persegi : ",luas)
		return None
	def lingkaran(x):
		pi = 22/7
		kuadrat = x**2
		luas = pi*kuadrat
		print("luas lingkaran : ",luas)

Luas.persegi(4)
Luas.lingkaran(7)

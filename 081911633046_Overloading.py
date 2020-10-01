#!/usr/bin/env python3

class bilbul:
	def hitung(self, a=None, b=None, c=None, d=None):
		sum = 0
		if a is None:
			print("anda tidak memasukkan parameter pertama")
		elif b is None:
			print("anda tidak memasukkan parameter kedua")
		elif d is None:
			if c is None:
				sum = a+b
				self.cetak(sum)
			else:
				sum = a+b+c
				self.cetak(sum)
		else:
			sum = a+b+c+d
			self.cetak(sum)
	def cetak(self, sum):
		print("hasil : ",sum)
print("=======soal pertama=========")
satu = bilbul()
satu.hitung()
satu.hitung(3)
satu.hitung(3,4)
satu.hitung(3,4,5)
satu.hitung(3,4,5,6)

class bungamajemuk:
	def hitung(self,modalawal=None,bunga=None,jangkawaktu=None):
		if modalawal is None:
			print("anda belum memasukkan modalawal")
		elif bunga is None:
			print("anda belum memasukkan bunga")
		elif jangkawaktu is None:
			print("anda belum memasukkan jangka waktu")
		else:
			bag1 = 1+bunga
			bag2 = bag1**jangkawaktu
			bag3 = modalawal*bag2
			modalakhir = bag3
			print("modal akhir : ",modalakhir)

print("=======soal kedua=========")
dua = bungamajemuk()
dua.hitung()
dua.hitung(1000000)
dua.hitung(1000000,0.02)
dua.hitung(1000000,0.02,5)

class volsilinder:
	def hitung(self, jari=None, tinggi=None):
		if jari is None:
			print("anda tidak memasukkan parameter pertama untuk jari-jari")
		elif tinggi is None:
			print("anda tidak memasukkan parameter kedua untuk tinggi")
		else:
			pi = 22/7
			kuadrat = jari**2
			hasil = pi*kuadrat*tinggi
			print("volume silinder : ", hasil)

print("=======soal ketiga=========")
tiga = volsilinder()
tiga.hitung()
tiga.hitung(2)
tiga.hitung(2,3)

class volbalok:
	def hitung(self,p=None,l=None,t=None):
		if p is None:
			print("anda tidak memasukkan panjang balok")
		elif l is None:
			print("anda tidak memasukkan lebar balok")
		elif t is None:
			print("anda tidak memasukkan tinggi balok")
		else:
			vol = p*l*t
			print("volume balok : ", vol)

print("=======soal keempat=========")
empat = volbalok()
empat.hitung()
empat.hitung(2)
empat.hitung(2,3)
empat.hitung(2,3,4)

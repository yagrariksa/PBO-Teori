#!usr/bin/env python3

class SegiEmpat:
    def luasBujurSangkar(panjang):
        luas = panjang*panjang
        print("luas Bujur Sangkar : ", luas)
        return luas

    def luasPersegiPanjang(panjang, lebar):
        luas = panjang*lebar
        print("luas Persegi Panjang : ", luas)
        return luas


SegiEmpat.luasBujurSangkar(4)
SegiEmpat.luasPersegiPanjang(4, 6)

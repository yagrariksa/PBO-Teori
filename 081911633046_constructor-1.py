#!/usr/bin/env python3

class Satu:
    def __init__(self, a=None, b=None):
        if a is None:
            self._a = 1
            self._b = 1
        else:
            if b is None:
                self._a = a
                self._b = 1
            else:
                self._a = a
                self._b = b

    def jumlah(self, a=None, b=None):
        if a is None:
            c = self._a + self._b
        else:
            if b is None:
                c = a + self._b
            else:
                c = a + b
        print(c)
        return c

    def kurang(self, a=None, b=None):
        if a is None:
            c = self._a - self._b
        else:
            if b is None:
                c = a - self._b
            else:
                c = a - b
        print(c)
        return c


satu = Satu(5, 6)
satu.jumlah()
satu.jumlah(1)
satu.jumlah(1, 1)
satu.kurang()
satu.kurang(2)
satu.kurang(4, 2)

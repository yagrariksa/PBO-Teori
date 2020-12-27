import c1

class C3(c1.C1):
    def __init__(self,x=0,y=0,z=0,u=0):
        super().__init__(x,y,z,u)

    def getU(self):
        return self._u

c3  = C3()
c3.m()
print(c3.x)
print(c3.y)
print(c3.z)


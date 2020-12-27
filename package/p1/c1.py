class C1():
    def __init__(self,x = 0,y = 0,z = 0,u = 0):
        self.x = x
        self._y = y
        self.z = z
        self.__u = u
    
    def m(self):
        print("this is method M")

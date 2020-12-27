class RoundShape():
    def __init__(self,radius,center,objC):
        self.radius = radius
        self.center = center
        self.objC = objC

    def area(self):
        luas = (22/7)*(self.radius**2)
        return luas

class Spehere(RoundShape):
    def __init__(self,radius,center,objC):
        super().__init__(radius,center,objC)

    def area(self):
        luas = 4*super().area()
        return luas

class Circle(RoundShape):
    def __init__(self,radius,center,objC):
        super().__init__(radius,center,objC)

    
class Tabung(Circle):
    def __init__(self,radius,center,objC,tinggi):
        super().__init__(radius,center,objC)
        self.tinggi = tinggi

    def area(self):
        luas = self.tinggi*(22/7)*self.radius
        return luas
    

class Main():
    def __init__(self):
        sphere = Spehere(3,4,5)
        print("Sphere area :", sphere.area())

        circle = Circle(3,4,5)
        print("Circle area :",circle.area())

        tabung = Tabung(3,4,5,6)
        print("Tabung area :",tabung.area())

run = Main()
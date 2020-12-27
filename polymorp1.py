class Employee():
    def __init__(self,holiday,name,dept,los):
        self.holiday = holiday
        self.name = name
        self.departement = dept
        self.lengthOfService = los

    def getName(self):
        return str(self.name)

    def getDepartement(self):
        return str(self.departement)

    def getLengthOfService(self):
        return str(self.lengthOfService)

    def getHoliday(self):
        return str(self.holiday)

    def __str__(self):
        string = ("name :", self.getName(),
            "\ndepartement :", self.getDepartement(),
            "\nholiday :", self.getHoliday(),
            "\nLength Of Service :", self.getLengthOfService())
        return (" ".join(string))



class Technician(Employee):
    def __init__(self,holiday,name,dept,los):
        super().__init__(holiday,name,dept,los)

    def getHoliday(self):
        return super().getHoliday()

    def __str__(self):
        return super().__str__()



class Manager(Employee):
    def __init__(self,holiday,name,dept,los):
        super().__init__(holiday,name,dept,los)

    def getHoliday(self):
        return super().getHoliday()

    def __str__(self):
        return super().__str__()



class Main():
    def __init__(self):
        heyho = Technician(12,32,43,54)
        print(heyho)



run = Main()

    
    
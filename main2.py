import abc
class Animal(metaclass=abc.ABCMeta):
    def __init__(self, name, canfly=False):
        self.name = name
        self.canfly = canfly

    @abc.abstractmethod
    def makeSound(self):
        pass
    
    @abc.abstractmethod
    def myName(self):
        pass

    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I need to sleep")


class Cat(Animal):
    def __init__(self,name,canfly=False):
        super().__init__(name,canfly)

    def makeSound(self):
        print("meow meow")

    def myName(self):
        print("name : ", self.name)

kucing = Cat("doraemon", False)
kucing.makeSound()
kucing.eat()
kucing.sleep()
kucing.myName()
print("bisaterbang? : ",kucing.canfly)
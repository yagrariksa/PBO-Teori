import abc
class Animal(metaclass=abc.ABCMeta):
    def __init__(self, name, canfly=False):
        self.name = name
        self.canfly = canfly

    def __str__(self):
        result = '' if self.canfly else 'tidak'
        return self.name+" dan termasuk hewan yang "+result+" bisa terbang"

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

    def __str__(self):
        return "kucing ini bernama "+super().__str__()+" serta bersuara "+self.makeSound()
        # return "heyho"+"boom"

    def makeSound(self):
        return "meow meow"

    def myName(self):
        print("name : ", self.name)

kucing = Cat("doraemon",False)
print(kucing)
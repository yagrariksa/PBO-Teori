import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def makeSound(self):
        pass
    
    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I need to sleep")


class Cat(Animal):
    def makeSound(self):
        print("meow meow")

kucing = Cat()
kucing.makeSound()
kucing.eat()
kucing.sleep()
class Animal:
    def __init__(self,name,speak,bark,eat):
        self.name = name
        self.speak= speak
        self.bark = bark
        self.eat = eat
    def showDetails(self):
        return f"This  is  a {self.name}.it can {self.speak}.it also can {self.bark}.and {self.eat}"
class Dog(Animal):
    def printDetails(self):
        return f"I am a {self.name}.i can {self.speak}.i also can {self.bark}.and {self.eat}"
Dog = Dog("Ozzy","speaking like human","bark loudly","Eating too much")
print(Dog.showDetails())
print(Dog.printDetails())
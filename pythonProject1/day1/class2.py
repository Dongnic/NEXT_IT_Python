#상속
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age=age

    def speak(self):
        print("bark")
class Duck(Animal):
    def speak(self):
        print("quack")
dog = Dog('doggy', 10)
print(dog.name)
print(dog.age)
dog.move()
dog.speak()
duck = Duck('ducky')
print(duck.name)
duck.move()
duck.speak()
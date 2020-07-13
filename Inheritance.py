class Mammal:
    def walk(self):
        print('walking')


class Dog(Mammal):
    pass


class Cat(Mammal):
    def meow(self):
        print('meowwww')


dog1 = Dog()
dog1.walk()


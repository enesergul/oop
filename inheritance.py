#parent
class Animal:
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animals walk parentt")
        
# child
class Monkey(Animal):
    def __init__(self):
        super().__init__()
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
        
class Bird(Animal):
    def __init__(self):
        #super().__init__()
        print("bird is created")
        
    def fly(self):
        print("fly")
m1 = Monkey()
m1.toString()
m1.walk()

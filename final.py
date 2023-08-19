from abc import ABC, abstractmethod
class Shapes(ABC):
    """
        Shape = super class/abstract class  
    """
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass
    def toString(self): pass
    
class Square(Shapes):
    def __init__(self,edge):
        self.__edge = edge
        
    def area(self):
        result = self.__edge**2
        print("Square area is :" , result)
        
    def perimeter(self):
        result = self.__edge *4
    
    def toString(self):        
        print("Square edge : ", self.__edge)

class Circle(Shapes):        
        def __init__(self,radius):
            self.__radius = radius
            self.PI = 3.14
        
        def area(self):
            result = self.PI * self.__radius**2
            print("Square area is :" , result)

        def perimeter(self):
            result = self.__radius *2 * self.PI

        def toString(self):
            print("Circle radius : ", self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()

d = Square(5)
d.area()
d.perimeter()
d.toString()
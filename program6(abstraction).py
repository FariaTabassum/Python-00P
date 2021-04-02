from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def area (self):
        pass
class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle: ",area)
t1 = Triangle(20,30)
t1.area()

t2 = Triangle(30,60)
t2.area()




"""
Warm up.
"""

class Shape:
    __width = 0
    __height = 0
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def area(self):
        return self.get_width() * self.get_height()
        
class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)
        
    def area(self):
        return self.get_width() * self.get_height() / 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

#=======================================

class Mother:
    def __str__(self):
        return "object Mother"

class Daughter(Mother):
    def __str__(self):
        return "object Daughter"



#=======================================

class Animal:
    __name = ""
    __type = ""
    __age = 0
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__type = "Animal"
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_type(self):
        return self.__type
    
    def __str__(self):
        return self.get_str()
    
    def get_str(self):
        return " ".join(["Type:", self.get_type(), "\n",
                        "Name:", self.get_name(), "\n",
                        "Age:", str(self.get_age()), "\n",
                        "------------------------------------------------\n"])
  
    
class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__type = "Zebra"
        
class Dolphin(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__type = "Dolphin"




if __name__ == "__main__":
    t = Triangle(12, 34)
    r = Rectangle(7,8)
    print(t.area(), r.area())
    print()
    
    m = Mother()
    dt = Daughter()
    print(m, dt)
    print()
    
    z = Zebra("Allison", 2)
    print(z)
    d = Dolphin("Greg", 5)
    print(d)
    
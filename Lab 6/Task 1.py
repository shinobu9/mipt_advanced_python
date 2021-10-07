'''
Реализуйте свой класс Complex для комплексных
чисел, аналогично встроенной реализации complex: 
    1. Добавьте инициализатор класса
    2. Реализуйте основные математические операции
    3. Реализуйте операцию модуля (abs, вызываемую как |c|)
    4. Оба класса должны давать осмысленный вывод как при print, 
       так и просто при вызове в ячейке
'''
class Complex(complex):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b,\
                       self.a * other.b + self.b * other.a)
    
    def __truediv__(self, other):
        return Complex((self.a * other.a + self.b * other.b)/(other.a**2 + other.b**2),
                       (self.b * other.a - self.a * other.b)/(other.a**2 + other.b**2))
    
    def __abs__(self):
        return (self.a**2 + self.b**2)**0.5
    
    def __str__(self):
        return str((self.a, self.b))
    
    def __repr__(self):
        return str((self.a, self.b))
    
        
x = Complex(3,4)
y = Complex(1,2)
print(x)



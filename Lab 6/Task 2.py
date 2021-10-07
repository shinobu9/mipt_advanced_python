'''
1. Создайте класс Vector с полями x, y, z определите для него конструктор,
 метод __str__, необходимые арифметические операции.
 Реализуйте конструктор, который принимает строку в формате "x,y". 
 
 #. Используя класс Vector выведите координаты центра масс данного
 множества точек. 
 #. Даны два вектора. Выведите площадь параллелограмма, 
 построенного на заданных векторах. 
 #. Даны три вектора. Выведите объём параллелепипеда,
 построенного на заданных векторах. 
 #. Среди данных точек найдите три точки, образующие
 треугольник с наибольшим периметром. Выведите данный периметр. 
 #. Среди данных точек найдите три точки, образующие треугольник с
 наибольшей площадью. Выведите данную площадь.
 '''

class Vector(list):
    def __init__(self, args="0,0,0"):
         self.x, self.y, self.z = map(int, args.split(','))
         
    def __str__(self):
        return str((self.x, self.y, self.z))
    
    def __repr__(self):
        return str((self.x, self.y, self.z))
    
    def __add__(self, other):
        '''
        Add 2 Vectors
        '''
        return Vector(','.join(map(str, [self.x + other.x, self.y + other.y, self.z + other.z])))
    
    def __sub__(self, other):
        '''
        Substract one Vector from other
        '''
        return Vector(','.join(map(str, [self.x - other.x, self.y - other.y, self.z - other.z])))
    
    def __mul__(self, other):
        '''
        Multiply by an integer or another Vector
        '''
        if type(other) == int:
            return Vector(','.join(map(str, [self.x * other, self.y * other, self.z * other])))
        return Vector(','.join(map(str, [self.x * other.x, self.y * other.y, self.z * other.z])))
    
    def __abs__(self):
        '''
        Length of vector
        '''
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    @staticmethod
    def farthest_point(N, coords):
        dist = 0
        farthest = "0,0,0"
        for i in range(N):
            new_dist = abs(Vector(coords[i]))
            if new_dist > dist:
                dist = new_dist
                farthest = coords[i]
        return Vector(farthest)
    
   
print(Vector.farthest_point(3, ["1,0,0","1,2,1","4,5,6"]))

















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
        Multiply by an integer/Scalar Vector multiplication
        '''
        if type(other) == int:
            return Vector(','.join(map(str, [self.x * other, self.y * other, self.z * other])))
        return Vector(','.join(map(str, [self.x * other.x, self.y * other.y, self.z * other.z])))
    
    def __abs__(self):
        '''
        Length of vector
        '''
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __matmul__(self, other):
        '''
        Vector multiplication
        '''
        return Vector(str(self.y*other.z - self.z*other.y)+','+
                      str(self.z*other.x - self.x*other.z)+','+
                      str(self.x * other.y - self.y * other.x))
    
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
    
    @staticmethod
    def parallelogram(a,b):
        A = Vector(a)
        B = Vector(b)
        C = A @ B
        return C

    @staticmethod
    def parallelepiped(a,b,c):
        C = Vector(c)
        D = Vector.parallelogram(a,b)
        return D*C

    @staticmethod
    def triangle(N , arr):
        peri_arr = []
        area_arr = []
        peri = []
        area = []
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    a = Vector(arr[i])
                    b = Vector(arr[j])
                    c = Vector(arr[k])
                    m = a - b
                    n = a - c
                    p = b - c
                    if m @ n == Vector('0,0,0'):
                        continue
                    else:
                        peri_arr.append([arr[i], arr[j], arr[k]])
                        area_arr.append([arr[i], arr[j], arr[k]])
                        peri.append(abs(m) + abs(n) + abs(p))
                        area.append(1 / 2 * abs(m * n))
        max_peri = max(peri)
        print('The 3 vertices that create the triangle with the largest perimeter are: ')
        for x in peri_arr[peri.index(max_peri)]:
            print(x)
        print('The longest perimeter triangle is: ', max_peri)
        max_area = max(area)
        print('The 3 vertices that create the triangle with the largest area are: ')
        for x in peri_arr[area.index(max_area)]:
            print(x)
        print('The longest area triangle is: ', max_area)

# N = int(input())
# arr= []
# center_point = Vector('0,0,0')
# for i in range(N):
#     a=input()
#     arr.append(a)
#     center_point = center_point + Vector(a)
# '''
# farthest point
# '''
# print('farthest point is : ',end = ' ')
# Vector.farthest_point(N,arr)

# '''
# center point 
# '''
# def center(center_point):
#     return (center_point.x / N, center_point.y / N, center_point.z / N)
# my_center_point = center(center_point)
# print('center point is : ',end= ' ')
# print(my_center_point)

# '''
# area of parallelogram
# '''
# print('enter two vectors :')
# a = input()
# b = input()
# print('area of parallelogram : ',abs(Vector.parallelogram(a,b)))

# '''
# volume of a parallelepiped
# '''
print('enter three vectors :')
a = input()
b = input()
c = input()
print('area of parallelepiped : ', abs(Vector.parallelepiped(a,b,c)))

"""
longest perimeter triangle, longest area triangle
"""
# Vector.triangle(N,arr)
    
   
# print(Vector.farthest_point(3, ["1,0,0","1,2,1","4,5,6"]))

















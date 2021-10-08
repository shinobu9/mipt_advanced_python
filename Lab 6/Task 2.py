class Vector(list):
    def __init__(self, args="0,0,0"):
         self.x, self.y, self.z = map(float, args.split(','))
         
    def __str__(self):
        return str((self.x, self.y, self.z))
    
    def __repr__(self):
        return "Vector" + str((self.x, self.y, self.z))
    
    def __add__(self, other):
        '''
        Add 2 Vectors
        '''
        return Vector(','.join(map(str, [self.x + other.x, self.y + other.y, self.z + other.z])))
    
    def __radd__(self, other):
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
        if type(other) in [int, float]:
            return Vector(','.join(map(str, [self.x * other, self.y * other, self.z * other])))
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __rmul__(self, other):
        '''
        Multiply by an integer/Scalar Vector multiplication
        '''
        if type(other) in [int, float]:
            return Vector(','.join(map(str, [self.x * other, self.y * other, self.z * other])))
        return self.x * other.x + self.y * other.y + self.z * other.z
    
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
        '''
        Return farthest point from origin (0,0,0)
        '''
        dist = 0
        farthest = "0,0,0"
        for i in range(N):
            new_dist = Vector(coords[i]).__abs__()
            if new_dist > dist:
                dist = new_dist
                farthest = coords[i]
        return Vector(farthest)
    
    @staticmethod
    def center_point(N, arr):
        '''
        Return center point of an array of points
        '''
        center_point = Vector()
        for i in arr:
            center_point = center_point + Vector(i)
        return center_point * (1/N)
    
    @staticmethod
    def parallelogram(a, b):
        '''
        input: str
        output: float
        '''
        A = Vector(a)
        B = Vector(b)
        C = A @ B
        return C.__abs__()

    @staticmethod
    def parallelepiped(a, b, c):
        '''
        input: str
        output: float
        '''
        C = Vector(c)
        D = Vector.parallelogram(a,b) #float
        return (D*C).__abs__()

    # TODO: 
        #. Среди данных точек найдите три точки, образующие
        # треугольник с наибольшим периметром. Выведите данный периметр. 
        #. Среди данных точек найдите три точки, образующие треугольник с
        # наибольшей площадью. Выведите данную площадь.
        
    # @staticmethod
    # def triangle(N , arr):
    #     peri_arr = []
    #     area_arr = []
    #     peri = []
    #     area = []
    #     for i in range(N - 2):
    #         for j in range(i + 1, N - 1):
    #             for k in range(j + 1, N):
    #                 a = Vector(arr[i])
    #                 b = Vector(arr[j])
    #                 c = Vector(arr[k])
    #                 m = a - b
    #                 n = a - c
    #                 p = b - c
    #                 if m @ n == Vector('0,0,0'):
    #                     continue
    #                 else:
    #                     peri_arr.append([arr[i], arr[j], arr[k]])
    #                     area_arr.append([arr[i], arr[j], arr[k]])
    #                     peri.append(abs(m) + abs(n) + abs(p))
    #                     area.append(1 / 2 * abs(m * n))
    #     max_peri = max(peri)
    #     print('The 3 vertices that create the triangle with the largest perimeter are: ')
    #     for x in peri_arr[peri.index(max_peri)]:
    #         print(x)
    #     print('The longest perimeter triangle is: ', max_peri)
    #     max_area = max(area)
    #     print('The 3 vertices that create the triangle with the largest area are: ')
    #     for x in peri_arr[area.index(max_area)]:
    #         print(x)
    #     print('The longest area triangle is: ', max_area)




if __name__ == "__main__":    
    N = int(input("Enter number of vectors: "))
    arr = []
    center_point = Vector('0,0,0')
    for i in range(N):
        a = input()
        arr.append(a)
        
    print('1) Farthest point from origin is : {}'.format(Vector.farthest_point(N, arr)))
    print('2) Center point is : {}'.format(Vector.center_point(N, arr)))

    print('Enter two vectors to find area of a parallelogram :')
    a = input()
    b = input()
    print('3) Area of parallelogram is : {}'.format(Vector.parallelogram(a, b)))
    
    print('Enter three vectors to find volume of a parallelepiped :')
    a = input()
    b = input()
    c = input()
    print('4) Area of parallelepiped : {}'.format(Vector.parallelepiped(a,b,c)))

    # Vector.triangle(N,arr)















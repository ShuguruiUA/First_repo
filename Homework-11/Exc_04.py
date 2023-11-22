class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        #print(f'{self.coordinates.x},{self.coordinates.y}')

    def __setitem__(self, index, value):
        if index == 0:
            self.__dict__[index] = value
            self.coordinates.x = value
        elif index == 1:
            self.__dict__[index] = value
            self.coordinates.y = value
        
            

    def __getitem__(self, index):
        # result = str(self.__dict__[index][0])
        # for value in self.__dict__[index][1:]:
        #     result += ", " + str(value)
        # return result
        return self.__dict__[index]

vector = Vector(Point(1,10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 3  # Встановлюємо координату x вектора 10
vector[1] = 4

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

print(vector[0])  # 10
print(vector[1])  # 10

"""
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        print(f'{self.coordinates.x},{self.coordinates.y}')

    def __setitem__(self, index, value):
        if index in (0, 1):
            self.coordinates[index] = value
            
        
            

    def __getitem__(self, index):
            return str(self.coordinates[index])
            
        
            
"""
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, int) == True or isinstance(x, float) == True:
            self.__x = x
        else:
            self.__x = None
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, int) == True or isinstance(y, float) == True:
            self.__y = y
        else:
            self.__y = None
            
point = Point(5, 10)
point_w = Point('x', 10)

print(point)
print(point_w)
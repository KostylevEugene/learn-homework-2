class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def coordinates(self):
        print(f'Координаты: x {self.x}, y {self.y}')



my_point = Point(1, 3)

my_point.coordinates()

my_point.x = 10
my_point.y = -5

my_point.coordinates()
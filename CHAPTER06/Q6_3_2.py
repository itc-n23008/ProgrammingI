class Shape:
    def __init__(self, name):
        self.name = name


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def calc_perimeter(self):
        return 2 * (self.width + self.height)

    def calc_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, width):
        super().__init__("square", width, width)


s1 = Square(4)
print("name:", s1.name)
print("width:", s1.width)
print("height:", s1.height)
print("angle:", 90)
print("perimeter:", s1.calc_perimeter())
print("area:", s1.calc_area())

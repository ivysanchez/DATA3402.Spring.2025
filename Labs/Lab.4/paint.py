import math
from abc import ABC, abstractmethod

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range(height)]

    def set_pixel(self, row, col, char='*'):
        self.data[row][col] = char

    def get_pixel(self, row, col):
        return self.data[row][col]

    def clear_canvas(self):
        self.data = [[' '] * self.width for i in range(self.height)]

    def v_line(self, x, y, w, **kargs):
        for i in range(x, x + w):
            self.set_pixel(i, y, **kargs)

    def h_line(self, x, y, h, **kargs):
        for i in range(y, y + h):
            self.set_pixel(x, i, **kargs)

    def line(self, x1, y1, x2, y2, **kargs):
        slope = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')  # Handle vertical lines
        for y in range(y1, y2 + 1):
            if slope == float('inf'):
                x = x1
            else:
                x = int(x1 + slope * (y - y1))
            
            if 0 <= x < self.width and 0 <= y < self.height:
                self.set_pixel(y, x, **kargs)

    def display(self):
        print("\n".join(["".join(row) for row in self.data]))
        
## question 12
    def __repr__(self):
        return f"Canvas({self.width}, {self.height})"


class Shape(ABC):
    def __init__(self, x, y, name=""):
        self.__x = x
        self.__y = y
        self.name = name
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def get_perimeter_points(self):
        pass
    @abstractmethod
    def is_inside(self, x, y):
        pass
    def overlaps(self, other):
        self_perimeter_points = self.get_perimeter_points()
        other_perimeter_points = other.get_perimeter_points()
        for point in self_perimeter_points:
            if other.is_inside(point[0], point[1]):
                return True
        for point in other_perimeter_points:
            if self.is_inside(point[0], point[1]):
                return True
        return False
## question 12
    def __repr__(self):
        return f"{self.__class__.__name__}({self.get_x()}, {self.get_y()}, name='{self.name}')"


class Rectangle(Shape):
    def __init__(self, length, width, x, y, name=""):
        super().__init__(x, y, name)
        self.__length = length
        self.__width = width
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
    def get_perimeter_points(self):
        x, y = self.get_x(), self.get_y()
        length, width = self.get_length(), self.get_width()
        points = []
        for i in range(16):
            perimeter_fraction = i / 16  
            if 0 <= perimeter_fraction < 0.25:  # Top edge
                points.append((x + perimeter_fraction * 4 * length, y))
            elif 0.25 <= perimeter_fraction < 0.5:  # right edge
                points.append((x + length, y + (perimeter_fraction - 0.25) * 4 * width))
            elif 0.5 <= perimeter_fraction < 0.75:  # bottom edge
                points.append((x + length - (perimeter_fraction - 0.5) * 4 * length, y + width))
            else:  # left edge
                points.append((x, y + width - (perimeter_fraction - 0.75) * 4 * width))
        return points
    def is_inside(self, x, y):
        return x >= self.get_x() and x <= self.get_x() + self.get_length() and y >= self.get_y() and y <= self.get_y() + self.get_width()
# question 10
    def paint(self, canvas):
        x, y = int(self.get_x()), int(self.get_y())
        length, width = int(self.__length), int(self.__width)
        for row in range(y, y + width):
            for col in range(x, x + length):
                if 0 <= row < canvas.height and 0 <= col < canvas.width:
                    canvas.set_pixel(row, col)
## question 12
    def __repr__(self):
        return f"Rectangle({self.get_length()}, {self.get_width()}, {self.get_x()}, {self.get_y()})"

class Circle(Shape):
    def __init__(self, radius, x, y, name=""):
        super().__init__(x, y, name)
        self.__radius = radius
    def get_radius(self):
        return self.__radius
    def area(self):
        return math.pi * (self.__radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.__radius
    def get_perimeter_points(self):
        x, y = self.get_x(), self.get_y()
        radius = self.get_radius()
        points = []
        for i in range(16):
            angle = 2 * math.pi * i / 16 
            points.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
        return points
    def is_inside(self, x, y):
        return (x - self.get_x())**2 + (y - self.get_y())**2 <= self.get_radius()**2
# question 10
    def paint(self, canvas):
        x, y = int(float(self.get_x())), int(float(self.get_y()))
        radius = int(self.get_radius())
        for i in range(16):
            angle = 2 * math.pi * i / 16
            px = x + int(radius * math.cos(angle))
            py = y + int(radius * math.sin(angle))
            
            # Check if coordinates are within canvas bounds
            if 0 <= px < canvas.width and 0 <= py < canvas.height:
                canvas.set_pixel(py, px, char='*')
## question 12
    def __repr__(self):
        return f"Circle({self.get_radius()}, {self.get_x()}, {self.get_y()})"
            

class Triangle(Shape):
    def __init__(self, a, b, c, x, y):
        super().__init__(x, y)
        self.__a = a
        self.__b = b
        self.__c = c
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
    def perimeter(self):
        return self.__a + self.__b + self.__c
    def get_perimeter_points(self):
        x, y = self.get_x(), self.get_y()
        a, b, c = self.get_a(), self.get_b(), self.get_c()
        points = []
        for i in range(int(16*a/(a+b+c))):
            points.append((x + i*a/int(16*a/(a+b+c)), y))  
        for i in range(int(16*b/(a+b+c))):
            points.append((x + a - i*a/int(16*b/(a+b+c)), y + i*b/int(16*b/(a+b+c))))
        for i in range(int(16*c/(a+b+c))):
            points.append((x + (int(16*c/(a+b+c)) - i)*a/int(16*c/(a+b+c)), y + (int(16*c/(a+b+c))-i)*b/int(16*c/(a+b+c))))
        return points
    def is_inside(self, x, y):
        x0, y0 = self.get_x(), self.get_y()
        a, b, c = self.get_a(), self.get_b(), self.get_c()

        denominator = -b * -c - (-a) * (-b - c) 
        if denominator == 0:
            return False
        alpha = (-b * (x - x0 - c) - (-a) * (y - y0 - b - c)) / denominator
        beta = ((y0 - y - c) * (-a) - (x0 - x - a) * (-b)) / denominator
        gamma = 1 - alpha - beta
        return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1
# question 10
    def paint(self, canvas): # moved inside the Triangle class
        x, y = int(float(self.get_x())), int(float(self.get_y()))
        a, b, c = int(self.get_a()), int(self.get_b()), int(self.get_c())
        canvas.line(x, y, x + a, y, char='*')  
        canvas.line(x + a, y, x + a - b, y + b, char='*')  
        canvas.line(x + a - b, y + b, x, y, char='*')
## question 12
    def __repr__(self):
        return f"Triangle({self.get_a()}, {self.get_b()}, {self.get_c()}, {self.get_x()}, {self.get_y()})"


# question 10
class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes
        
    def area(self):
        return sum(shape.area() for shape in self.shapes)
        
    def perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)

    def get_perimeter_points(self):
        all_points = []
        for shape in self.shapes:
            all_points.extend(shape.get_perimeter_points())
        return all_points

    def is_inside(self, x, y):
        return any(shape.is_inside(x, y) for shape in self.shapes)

    def paint(self, canvas):
        for shape in self.shapes:
            shape.paint(canvas)
            
## question 12
    def __repr__(self):
        shapes_repr = ", ".join([repr(shape) for shape in self.shapes])
        return f"CompoundShape([{shapes_repr}])"





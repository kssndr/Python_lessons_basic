# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c
        self.ab = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        self.bc = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        self.ca = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    
    
    def triangle_square(self):
        p = (self.ab + self.bc + self.ca)/2
        self.triangle_square = (p * (p - self.ab) * (p - self.bc) * (p - self.ca)) ** 0.5
        return self.triangle_square
    
    def tringle_height(self, v):
        self.v = v
        s = self.triangle_square * 2
        if self.v == self.a:
            self.tringle_height = s / self.bc
        elif self.v == self.b:
            self.tringle_height = s / self.ca
        elif self.v == self.c:
            self.tringle_height = s / self.ab
        return self.tringle_height
    
    def triangle_perimeter(self):
        self.triangle_perimeter = self.ab + self.bc + self.ca
        return self.triangle_perimeter


my_tri = triangle((1, 1), (-2, 3), (11, 2))
my_tri.triangle_perimeter()
my_tri.triangle_square()
my_tri.tringle_height((1, 1))
print(my_tri.triangle_perimeter)
print(my_tri.triangle_square)
print(my_tri.tringle_height)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.



class trapezium:
    
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.ab = round((((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5), 2)
        self.bc = round((((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5), 2)
        self.cd = round((((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5), 2)
        self.da = round((((x1 - x4) ** 2 + (y1 - y4) ** 2) ** 0.5), 2)
        self.ac = round((((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5), 2) # диагональ
        self.bd = round((((x2 - x4) ** 2 + (y2 - y4) ** 2) ** 0.5), 2) # диагональ
    
    
    def trapezium_sides(self):
        self.trapezium_sides = print("\nстороны трапеции \nAB {}\nBC {}\nCD {}\nDA {}\n".format(self.ab, self.bc, self.cd, self.da))
        return self.trapezium_sides
    
    
    
    def check_trapezium(self):
        if self.ac == self.bd:
            self.check_trapezium = print("трапеция Равнобочная")
        else:
            self.check_trapezium = print("трапеция Не равнобочная")
            return self.check_trapeziu


def trapezium_square(self):
    if self.ac == self.bd:
        self.trapezium_square = print("Площадь:", round((((self.bc + self.da)/4) * (4 * (self.ac ** 2) - (self.bc - self.da) ** 2) ** 0.5), 2))
        else:
            self.trapezium_square = print("трапеция Не равнобочная")
    return self.trapezium_square


def trapezium_perimeter(self):
    self.trapezium_perimeter = print("Периметр:", (self.ab + self.bc + self.cd + self.da))
    
        return self.trapezium_perimeter


my_trap = trapezium(1,2,3,4,5,6,7,8)
my_trap.trapezium_sides()
my_trap.check_trapezium()
my_trap.trapezium_square()
my_trap.trapezium_perimeter()


print(my_trap.trapezium_sides)
print(my_trap.check_trapezium)
print(my_trap.trapezium_square)
print(my_trap.trapezium_perimeter)



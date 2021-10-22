import math


"""Базовым классом для всех фигур сделаем класс Фигура."""


class Shape:
    title = "Фигура"

    """Для абсолютно всех фигур мы можем посчитать площадь, поэтому вынесем этот метод в главный класс."""
    def area(self):
        pass


"""Фигуры делятся на плоские и объемные. Наследуем два этих класса от родительского Фигура.
У всех плоских фигур есть хотя бы один параметр."""


class FlatShape(Shape):
    title = "Плоская фигура"

    def __init__(self, a: float):
        self.a = a
    """Для плоских фигур по мимо площади мы можем считать периметр."""
    def perimeter(self):
        pass


class SolidShape(Shape):
    title = "Объемная фигура"

    """Для объемных фигур кроме площади мы можем посчитаь объем."""
    def volume(self):
        pass


"""Круг является плоской фигурой. Наследуем его от класса FlatShape
Никаких дополнительных параметров кроме радиуса при инициализации нет.
Переопределяем для этого класса методы, вычисляющие площадь и периметр."""


class Circle(FlatShape):
    title = "Круг"

    def __init__(self, a: float):
        super().__init__(a)

    def area(self) -> float:
        return math.pi * self.a ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.a


"""Квадрат так же является плоской фигурой, наследует все соответствующие свойства и методы.
Среди параметров у квадрата одна сторона, поэтому иницилизируем только через super()."""


class Square(FlatShape):
    title = "Квадрат"

    def __init__(self, a: float):
        super().__init__(a)

    def area(self) -> float:
        return self.a ** 2

    def perimeter(self) -> float:
        return 4 * self.a
    """Специфическим методом, который есть у квадрата, но которого нет у части фигур, является вычисление диагонали.
    Объявим этот метод для класса Квадрат"""
    def diagonal(self) -> float:
        return math.sqrt(2 * self.a ** 2)


"""Прямоугольник наследуем от квадрата. В инициализацию добавим объявление второй сторы и переобределим все методы."""


class Rectangle(Square):
    title = "Прямоугольник"

    def __init__(self, a: float, b: float):
        super().__init__(a)
        self.b = b

    def area(self) -> float:
        return self.a * self.b

    def perimeter(self) -> float:
        return 2 * self.a + 2 * self.b

    def diagonal(self) -> float:
        return math.sqrt(self.a ** 2 + self.b ** 2)


"""Ромб является частным случае квадрата. В качество второго параметра при иницализации добавим угол.
Переопределение периметра не требуется, так как вычисляется аналогично квадрату, переопределим остальные методы."""


class Rhombus(Square):
    title = "Ромб"

    def __init__(self, a: float, alfa: float):
        super().__init__(a)
        self.alfa = alfa

    def area(self) -> float:
        return self.a ** 2 * math.sin(self.alfa)

    def diagonal(self) -> float:
        return self.a * math.sqrt(2 + 2 * math.cos(self.alfa))


"""Треугольник задается тремя параметрами (три стороны), одну сторону инициализируем через родительский класс
Плоские фигуры, остальные внутри. Переопределяем классы площадь и периметр, а также добавляем специфические для 
этого класса методы - биссектриса и медиана."""


class Triangle(FlatShape):
    title = "Треугольник"

    def __init__(self, a: float, b: float, c: float):
        super().__init__(a)
        self.b = b
        self.c = c

    def area(self) -> float:
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def bisector(self) -> float:
        return math.sqrt(self.a * self.b * (self.a + self.b + self.c) * (self.a + self.b - self.c)) / (self.a + self.b)

    def median(self) -> float:
        return math.sqrt(2 * self.a ** 2 + 2 * self.b ** 2 - self.c ** 2) / 2


"""Трапеция в отличии от других фигур задаётся 4-мя сторонами, соответственно, добавляем их в свойства.
Переопределим методы, вычисляющие площадь и периметр, а также добавим специфические методы:
диагональ и средняя линяя"""


class Trapezoid(FlatShape):
    title = "Трапеция"

    def __init__(self, a: float, b: float, c: float, d: float):
        super().__init__(a)
        self.b = b
        self.c = c
        self.d = d

    def area(self) -> float:
        d = math.sqrt(self.c ** 2 - (((self. b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / 2 * (self.b - self.a)) ** 2)
        return self.mean_line() * d

    def perimeter(self) -> float:
        return self.a + self.b + self.c + self.c

    def diagonal(self) -> float:
        return math.sqrt(self.d ** 2 + self.a * self.b - self.b * (self.d ** 2 - self.c ** 2) / (self.b - self.a))

    def mean_line(self) -> float:
        return (self.a + self.b) / 2


"""Куб наследуем от класса Объемные фигуры. Заданим через один параметр - основание, которое является квадратом.
Специфическим методом является вычисление диагонали."""


class Cube(SolidShape):
    title = "Куб"

    def __init__(self, ground: Square):
        self.ground = ground

    def area(self) -> float:
        return 6 * self.ground.a ** 2

    def volume(self) -> float:
        return self.ground.a ** 3

    def diagonal(self) -> float:
        return math.sqrt(3) * self.ground.a


"""Прямоугольник наследуем от объемных фигур. Задаем двумя пармаметрами - основание,
которое является прямоугольником, и высота. Переопределяем методы и добавим метод даигональ."""


class Rhomboid(SolidShape):
    title = "Параллелограмм"

    def __init__(self, ground: Rectangle, h: float):
        self.ground = ground
        self.h = h

    def area(self) -> float:
        return 2 * (self.h * self.ground.a + self.ground.a * self.ground.b + self.h * self.ground.b)

    def volume(self) -> float:
        return self.ground.a * self.ground.b * self.h

    def diagonal(self) -> float:
        return math.sqrt(self.ground.a ** 2 + self.ground.b ** 2 + self.h ** 2)


"""Сферу - объемнаяя фигура. Среди свойств только радиус.
Переопределим методы родительского класса - площадь и объем."""


class Sphere(SolidShape):
    title = "Сфера"

    def __init__(self, a: float):
        self.a = a

    def area(self) -> float:
        return 4 * math.pi * self.a ** 2

    def volume(self) -> float:
        return 4 / 3 * math.pi * self.a ** 3


"""Конус инициализируем через два параметра - круг, который лежит в основании, и высота. 
Базовые методы переопределим."""


class Cone(SolidShape):
    title = "Конус"

    def __init__(self, ground: Circle, h: float):
        self.ground = ground
        self.h = h

    def area(self) -> float:
        return math.pi * self.ground.a * (math.sqrt(self.h ** 2 + self.ground.a ** 2) + self.ground.a)

    def volume(self) -> float:
        return 2 * math.pi * self.ground.a * (self.h + self.ground.a)


"""Цилиндр похож на конус, поэтому мы можем наследовать его от конуса. Пеереопределим основные методы.
Специфическим методом также является диагональ. Расширим им класс."""


class Cylinder(Cone):
    title = "Цилиндр"

    def __init__(self, ground: Circle, h: float):
        super().__init__(ground)
        super().__init__(h)

    def area(self) -> float:
        return 4 * math.pi * self.ground.a ** 2

    def volume(self) -> float:
        return 2 * math.pi * self.ground.a * (self.h + self.ground.a)

    def diagonal(self) -> float:
        return math.sqrt(self.h ** 2 + 4 * self.ground.a ** 2)


"""Для упрощения предположим, что у пирамиды в основании лежит треугольник.
Зададим двумя параметрами - основание (тип треугольник) и высота."""


class Pyramid(SolidShape):
    title = "Пирамида"

    def __init__(self, ground: Triangle, h: float):
        self.ground = ground
        self.h = h

    def area(self) -> float:
        return self.ground.perimeter() * self.h / 2 + self.ground.area()

    def volume(self) -> float:
        return self.ground.area() * self.h / 3

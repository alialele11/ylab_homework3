import math


"""Базовым классом для всех фигур сделаем класс Фигура."""


class Shape:
    title = "Фигура"
    """Абсолютно у всех фигур есть хотя бы 1 параметр (будь то сторона или радиус)."""
    def __init__(self, a: float):
        self.a = a
    """Для абсолютно всех фигур мы можем посчитать площадь, поэтому вынесем этот метод в главный класс."""
    def area(self):
        pass


"""Фигуры делятся на плоские и объемные. Наследуем два этих класса от родительского Фигура.
Иницлизируем через super() класс."""


class FlatShape(Shape):
    title = "Плоская фигура"

    def __init__(self, a: float):
        super().__init__(a)
    """Для плоских фигур по мимо площади мы можем считать периметр."""
    def perimeter(self):
        pass


class SolidShape(Shape):
    title = "Объемная фигура"

    def __init__(self, a: float):
        super().__init__(a)
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


class Trapezoid(FlatShape):
    title = "Трапеция"

    def __init__(self, a: float, b: float, c: float = None, d: float = None, h: float = None):
        super().__init__(a)
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def area(self):
        if self.h is not None:
            return self.mean_line() * self.h
        elif self.c is not None and self.d is not None:
            return (self.a + self.b) / 2 * math.sqrt(self.c ** 2 - (((self. b - self.a) ** 2 + self.b ** 2 - self.d ** 2) / 2 * (self.b - self.a) ** 2))
        else:
            return None

    def perimeter(self):
        if self.c is not None and self.d is not None:
            return self.a + self.b + self.c + self.c
        else:
            return None

    def diagonal(self) -> float:
        return

    def bisector(self) -> float:
        return 

    def mean_line(self) -> float:
        return (self.a + self.b) / 2

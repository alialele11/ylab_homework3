import math
import unittest


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
        return self.a ** 2 * math.sin(math.radians(self.alfa))

    def diagonal(self) -> float:
        return self.a * math.sqrt(2 + 2 * math.cos(math.radians(self.alfa)))


"""Треугольник задается тремя параметрами (три стороны), одну сторону инициализируем через родительский класс
Плоские фигуры, остальные внутри. Переопределяем классы площадь и периметр, а также добавляем специфические для 
этого класса методы - биссектриса и медиана. Медиану и биссектрису для примера посчитаем одну - на сторону c"""


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
        d = self.b - self.a
        return self.mean_line() * math.sqrt(self.c ** 2 - ((d ** 2 + self.c ** 2 - self.d ** 2) / 2 / d) ** 2)

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
        return self.ground.area() * self.h / 3


"""Цилиндр похож на конус, поэтому мы можем наследовать его от конуса. Пеереопределим основные методы.
Специфическим методом также является диагональ. Расширим им класс."""


class Cylinder(Cone):
    title = "Цилиндр"

    def __init__(self, ground: Circle, h: float):
        super().__init__(ground, h)

    def area(self) -> float:
        return 2 * math.pi * self.ground.a * (self.h + self.ground.a)

    def volume(self) -> float:
        return math.pi * self.ground.a ** 2 * self.h

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


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(3)

    def test_area(self):
        self.assertEqual(int(self.square.area()), 9)

    def test_perimeter(self):
        self.assertEqual(int(self.square.perimeter()), 12)

    def test_diagonal(self):
        self.assertEqual(round(self.square.diagonal(), 3), 4.243)


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(3)

    def test_area(self):
        self.assertEqual(round(self.circle.area(), 3), 28.274)

    def test_perimeter(self):
        self.assertEqual(round(self.circle.perimeter(), 2), 18.85)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(3, 4)

    def test_area(self):
        self.assertEqual(int(self.rectangle.area()), 12)

    def test_perimeter(self):
        self.assertEqual(int(self.rectangle.perimeter()), 14)

    def test_diagonal(self):
        self.assertEqual(int(self.rectangle.diagonal()), 5)


class TestRhombus(unittest.TestCase):
    def setUp(self):
        self.rhombus = Rhombus(3, 60)

    def test_area(self):
        self.assertEqual(round(self.rhombus.area(), 3), 7.794)

    def test_perimeter(self):
        self.assertEqual(int(self.rhombus.perimeter()), 12)

    def test_diagonal(self):
        self.assertEqual(round(self.rhombus.diagonal(), 3), 5.196)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4, 5)

    def test_area(self):
        self.assertEqual(int(self.triangle.area()), 6)

    def test_perimeter(self):
        self.assertEqual(int(self.triangle.perimeter()), 12)

    def test_median(self):
        self.assertEqual(round(self.triangle.median(), 1), 2.5)

    def test_bisector(self):
        self.assertEqual(round(self.triangle.bisector(), 3), 2.424)


class TestTrapezoid(unittest.TestCase):
    def setUp(self):
        self.trapezoid = Trapezoid(3, 6, 4, 4)

    def test_area(self):
        self.assertEqual(round(self.trapezoid.area(), 3), 16.686)

    def test_perimeter(self):
        self.assertEqual(int(self.trapezoid.perimeter()), 17)

    def test_diagonal(self):
        self.assertEqual(round(self.trapezoid.diagonal(), 3), 5.831)

    def test_mean_line(self):
        self.assertEqual(round(self.trapezoid.mean_line(), 1), 4.5)


class TestCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(Square(4))

    def test_area(self):
        self.assertEqual(int(self.cube.area()), 96)

    def test_volume(self):
        self.assertEqual(int(self.cube.volume()), 64)

    def test_diagonal(self):
        self.assertEqual(round(self.cube.diagonal(), 3), 6.928)


class TestRhomboid(unittest.TestCase):
    def setUp(self):
        self.rhomboid = Rhomboid(Rectangle(4, 3), 3)

    def test_area(self):
        self.assertEqual(int(self.rhomboid.area()), 66)

    def test_volume(self):
        self.assertEqual(int(self.rhomboid.volume()), 36)

    def test_diagonal(self):
        self.assertEqual(round(self.rhomboid.diagonal(), 3), 5.831)


class TestSphere(unittest.TestCase):
    def setUp(self):
        self.sphere = Sphere(3)

    def test_area(self):
        self.assertEqual(round(self.sphere.area(), 3), 113.097)

    def test_volume(self):
        self.assertEqual(round(self.sphere.volume(), 3), 113.097)


class TestCone(unittest.TestCase):
    def setUp(self):
        self.cone = Cone(Circle(3), 4)

    def test_area(self):
        self.assertEqual(round(self.cone.area(), 3), 75.398)

    def test_volume(self):
        self.assertEqual(round(self.cone.volume(), 3), 37.699)


class TestCylinder(unittest.TestCase):
    def setUp(self):
        self.cylinder = Cylinder(Circle(3), 4)

    def test_area(self):
        self.assertEqual(round(self.cylinder.area(), 3), 131.947)

    def test_volume(self):
        self.assertEqual(round(self.cylinder.volume(), 3), 113.097)

    def test_diagonal(self):
        self.assertEqual(round(self.cylinder.diagonal(), 3), 7.211)


class TestPyramid(unittest.TestCase):
    def setUp(self):
        self.pyramid = Pyramid(Triangle(3, 4, 5), 4)

    def test_area(self):
        self.assertEqual(int(self.pyramid.area()), 30)

    def test_volume(self):
        self.assertEqual(int(self.pyramid.volume()), 8)


if __name__ == "__main__":
    unittest.main()

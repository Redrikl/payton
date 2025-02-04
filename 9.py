class ShapeError(Exception):
    """
    Кастомное исключение, которое бросается при некорректных параметрах фигуры
    (например, отрицательные размеры).
    """
    pass


class Shape:
    """
    Базовый класс для всех фигур.
    Содержит общий интерфейс (поля: id, x, y, ...).
    """

    def __init__(self, shape_id: str, x: float = 0, y: float = 0):
        self.shape_id = shape_id
        # Координаты, например, 'центра' фигуры:
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        """
        Сдвигает фигуру на плоскости на (dx, dy).
        """
        self.x += dx
        self.y += dy

    def area(self) -> float:
        """
        Площадь фигуры (базовая заглушка).
        У потомков должен быть переопределён метод.
        """
        raise NotImplementedError("Метод area() должен быть переопределён в подклассе.")

    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.shape_id}', x={self.x}, y={self.y})"


# ---------- Классы типа T1 ----------

class Rectangle(Shape):
    """
    Прямоугольник (относится к типу T1).
    """
    def __init__(self, shape_id: str, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(shape_id, x, y)
        if width <= 0 or height <= 0:
            raise ShapeError(f"Некорректные размеры прямоугольника: width={width}, height={height}")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    """
    Треугольник (тоже тип T1).
    Для простоты храним только "основание" и "высоту".
    """
    def __init__(self, shape_id: str, base: float, height: float, x: float = 0, y: float = 0):
        super().__init__(shape_id, x, y)
        if base <= 0 or height <= 0:
            raise ShapeError(f"Некорректные размеры треугольника: base={base}, height={height}")
        self.base = base
        self.t_height = height

    def area(self) -> float:
        return 0.5 * self.base * self.t_height


class Quad(Rectangle):
    """
    Квадрат (тип T1), просто частный случай Rectangle с width=height.
    """
    def __init__(self, shape_id: str, side: float, x: float = 0, y: float = 0):
        super().__init__(shape_id, side, side, x, y)


# Можно добавить Tetragon, etc., аналогично…

# ---------- Классы типа T2 ----------

class Pentagon(Shape):
    """
    Пятиугольник (относится к типу T2).
    Упростим: пусть у нас "правильный пятиугольник" со стороной side.
    Считаем площадь по известной формуле (что-то вроде 1.72 * side^2).
    """
    def __init__(self, shape_id: str, side: float, x: float = 0, y: float = 0):
        super().__init__(shape_id, x, y)
        if side <= 0:
            raise ShapeError(f"Некорректный размер пятиугольника: side={side}")
        self.side = side

    def area(self) -> float:
        # Площадь правильного пятиугольника ~ (1/4)*√(5*(5+2√5))* side^2
        # Численно это примерно ~1.72 * side^2, для наглядности.
        return 1.72 * (self.side ** 2)

# ---------- Дополнительные функции (методы "внешние") ----------

def compare(obj1: Shape, obj2: Shape) -> int:
    """
    Сравнивает два объекта по площади.
    Возвращает:
      -1, если obj1 меньше obj2
       0, если равны
       1, если obj1 больше obj2
    """
    area1 = obj1.area()
    area2 = obj2.area()
    if abs(area1 - area2) < 1e-9:
        return 0
    return 1 if area1 > area2 else -1


def is_intersect(t1: Shape, t2: Shape) -> bool:
    """
    Проверка факта пересечения фигур t1 и t2.
    В реальности нужно анализировать их координаты и геометрию,
    здесь упрощённо предполагаем, что фигуры пересекаются, 
    если расстояние между их центрами < (некий порог, зависящий от размеров).
    """
    import math
    dx = t1.x - t2.x
    dy = t1.y - t2.y
    distance = math.hypot(dx, dy)
    # Условно считаем "радиус" фигуры = sqrt(area/pi), просто для демонстрации
    r1 = (t1.area() / 3.14159) ** 0.5
    r2 = (t2.area() / 3.14159) ** 0.5
    return distance < (r1 + r2)


def is_include(t1: Shape, t2: Shape) -> bool:
    """
    Проверка "включения" t2 в t1 — упрощённо: 
    если центр t2 достаточно "близко" к центру t1, 
    а размер t2 (area) значительно меньше.
    """
    import math
    dx = t1.x - t2.x
    dy = t1.y - t2.y
    distance = math.hypot(dx, dy)
    # Допустим, t2 "внутри" t1, если расстояние <= некий радиус "вместимости"
    # и при этом площадь t2 <= половины площади t1
    r1 = (t1.area() / 3.14159) ** 0.5
    return (distance + (t2.area() / 3.14159)**0.5 <= r1) and (t2.area() <= 0.5 * t1.area())


# ---------- Демонстрация ----------

if __name__ == "__main__":
    try:
        # Пробуем создать несколько объектов
        rect = Rectangle("RectA", width=10, height=5, x=0, y=0)
        tri = Triangle("TriB", base=6, height=4, x=2, y=2)
        sq = Quad("SquareC", side=5, x=10, y=10)
        pent = Pentagon("PentD", side=4, x=7, y=9)
        
        # Выводим площади
        print(f"{rect} имеет площадь {rect.area():.2f}")
        print(f"{tri} имеет площадь {tri.area():.2f}")
        print(f"{sq} имеет площадь {sq.area():.2f}")
        print(f"{pent} имеет площадь {pent.area():.2f}")
        
        # Сдвигаем треугольник move()
        tri.move(-2, -2)
        print("После move(-2, -2):", tri)
        
        # compare по площади
        cmp_result = compare(rect, tri)
        if cmp_result == 1:
            print(f"{rect.shape_id} больше {tri.shape_id}")
        elif cmp_result == -1:
            print(f"{rect.shape_id} меньше {tri.shape_id}")
        else:
            print(f"{rect.shape_id} и {tri.shape_id} равны по площади")

        # Проверка пересечения
        print(f"rect и tri пересекаются? -> {is_intersect(rect, tri)}")
        print(f"sq и pent пересекаются? -> {is_intersect(sq, pent)}")

        # Проверка включения
        print(f"tri внутри rect? -> {is_include(rect, tri)}")
        print(f"sq внутри pent? -> {is_include(pent, sq)}")

        # Пример броска исключения
        bad_tri = Triangle("BadTriangle", base=-3, height=2)

    except ShapeError as e:
        print("Произошла ошибка в параметрах фигуры:", e)
    except Exception as e:
        print("Некоторое иное исключение:", e)

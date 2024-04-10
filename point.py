"""
Высчитываем Евклидова расстояния
"""
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, x: float, y: float) -> float:
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def set_x(self, x: float):
        self.x = x

    def set_y(self, y: float):
        self.y = y


if __name__ == '__main__':
    point = Point(1, 2)
    print(point.distance_to(6, 5))
    point.set_x(5)
    print(f"Новая координата x первой точки: {point.get_x()}")


class Point:
    def __init__(self, point_a, point_b) -> None:
        self.__point_a = point_a
        self.__point_b = point_b

    def __add__(self, point):
        x = self.__point_a + point.__point_a
        y = self.__point_b + point.__point_b

        return Point(x, y)
    
    def __str__(self) -> str:
        return f"({self.__point_a}, {self.__point_b})"

def main():

    point_1 = Point(4, 4)
    point_2 = Point(6, 6)

    point_3 = point_1 + point_2

    print(point_3)

main()

class Points:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def __add__(self, point):
        x = self.point_a + point.point_a
        y = self.point_b + point.point_b

        return Points(x, y)
    
    def __str__(self) -> str:
        return f"({self.point_a}, {self.point_b})"
    
def main():
    
    point_1 = Points(2, 3)
    point_2 = Points(3,2)

    print(point_1.__add__(point_2))
    
    #point_3 = point_1 + point_2

   # print(point_3)

main()

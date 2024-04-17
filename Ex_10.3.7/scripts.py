from function import circle_square, rect_square

r = float(input('Введите радиус круга: '))
a, b = input('Введите длину и ширину прямоугольника a b: ').split()
a, b = float(a), float(b)

def bigger(circle: float, rect: float) -> str:
    if circle > rect:
        return f'Круг больше прямоугольника'
    elif circle == rect:
        return f'Фигуры равны'
    else:
        return f'Прямоугольник больше круга'

print(bigger(circle_square(r), rect_square(a, b)))
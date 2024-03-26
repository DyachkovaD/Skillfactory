class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, edge, l, ort):
        self.edge = edge # class Dot(x, y)
        self.l = l #int
        self.ort = ort # 0 - horizontal 1 - vertical
        self.lives = l

    @property
    def dots(self):
        ship_dots = []

        for i in range(self.l):
            if self.ort:
                dot = Dot(self.edge.x, self.edge.y + i)
                ship_dots.append(dot)
            else:
                dot = Dot(self.edge.x + i, self.edge.y)
                ship_dots.append(dot)
        return ship_dots

s = Ship(Dot(1, 4), 2, 1)
print(s.dots)

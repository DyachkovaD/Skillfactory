class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            raise ValueError("side must be above zero")


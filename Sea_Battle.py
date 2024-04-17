from random import randint

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return f"Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return f"Вы уже стреляли в эту клетку!"

class BoardWrongShipException(BoardException):
    pass


class Dot:    
    def __init__(self, x, y):
        self.x = x        
        self.y = y  
    
    def __eq__(self, other):        
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, bow, l, o): # o - ориентация корабля
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l
    @property
    def dots(self):
        ship_dots = []

        cur_x = self.bow.x
        cur_y = self.bow.y
        for i in range(self.l):
            if self.o == 0:
                cur_x += 1
            elif self.o == 1:
                cur_y += 1
            ship_dots.append(Dot(cur_x, cur_y))
        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0
        self.field = [["~"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        res = ''
        res += "    1   2   3   4   5   6  "
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + "   ".join(row) + " | "

        if self.hid:
            res = res.replace("▄", "~")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb=False):
        for dot in ship.dots:
            for x in range(dot.x - 1, dot.x + 2):
                for y in range(dot.y - 1, dot.y + 2):
                    if not(self.out(Dot(x, y))) and Dot(x, y) not in self.busy:
                        if verb:
                            self.field[x][y] = '.'
                        self.busy.append(Dot(x, y))

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "▄"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()
            
        if d in self.busy:
            raise BoardUsedException()
            
        self.busy.append(d)

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен")
                    return False
                else:
                    print("Корабль подбит")
                    return True
        self.field[d.x][d.y] = '.'
        print("Мимо!")
        return False
    
    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print("Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit() or y.isdigit()):
                print("Введите числа! ")
                continue

            x, y = int(x), int(y)
            return Dot(x - 1, y - 1)

class Game:

    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)
    
    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attampts = 0
        for l in lens:
            while True:
                attampts += 1
                if attampts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print(f''' {'-' * 50}
                  Приветствуем вас   
                      в игре        
                   Морской бой     
               ---------------------
                 формат ввода: x y  
                 x - номер строки   
                 у - номер столбца  ''')

    def play(self):
        turn = 0
        while True:
            print("_" * 25)
            print("Ваша доска: ")
            print(self.us.board)
            print("\nДоска противника: ")
            print(self.ai.board)
            print("_" * 25)
            if turn % 2 == 0:
                print("Вы ходите --> ")
                repeat = self.us.move()
            else:
                print("Ходит противник --> ")
                repeat = self.ai.move()
            if repeat:
                turn -= 1

            if self.ai.board.count == 7:
                print("-" * 30)
                print("Вы выиграли!")
                break
                
            if self.us.board.count == 7:
                print("-" * 30)
                print("Противник выиграл!")
                break
            turn += 1

    def start(self):
        self.greet()
        self.play()
        
g = Game()
g.start()
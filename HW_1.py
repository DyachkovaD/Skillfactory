# первый ходит крестиками
# второй ноликами

F = [['' for x in range(3)] for y in range(3)]
fild = f"""      0    1    2
    0 {F[0][0]:3} {F[0][1]:3} {F[0][2]:3} |
    1 {F[1][0]:3} {F[1][1]:3} {F[1][2]:3} |
    2 {F[2][0]:3} {F[2][1]:3} {F[2][2]:3} |
       ___ ___ ___
        """
print('Начнём игру!')
print(fild)
counter = 0
rezult = None
while True:

    for g in range(len(F)):
        for v in range(len(F)):
            if F[g][0] == F[g][1] == F[g][2] != "":
                rezult = "Победил игрок X" if counter & 1 else "Победил игрок O"
                break
            if F[0][v] == F[1][v] == F[2][v] != "":
                rezult = "Победил игрок X" if counter & 1 else "Победил игрок O"
                break
            if F[0][0] == F[1][1] == F[2][2] != "":
                rezult = "Победил игрок X" if counter & 1 else "Победил игрок O"
                break
            if F[0][2] == F[1][1] == F[2][0] != "":
                rezult = "Победил игрок X" if counter & 1 else "Победил игрок O"
                break
        else:
            break

    if rezult:
        print(rezult)
        break
    if counter == 9:
        print("Ничья")
        break

    counter += 1
    if counter & 1:
        player1_move = input('Ходит игрок X. Введите команду в формате (строка столбец)')
        gor, vert = map(int, player1_move.strip().split())
        while F[gor][vert] != '':
            player1_move = input('Ячейка занята, Вы можете ходить только на свободные ячейки. Поменяйте ход')
            gor, vert = map(int, player1_move.strip().split())
        F[gor][vert] = "x"
    else:
        player2_move = input('Ходит игрок O. Введите команду в формате (строка столбец)')
        gor, vert = map(int, player2_move.strip().split())
        while F[gor][vert] != '':
            player1_move = input('Ячейка занята, Вы можете ходить только на свободные ячейки. Поменяйте ход')
            gor, vert = map(int, player1_move.strip().split())
        F[gor][vert] = "o"

    fild = f"""          0    1    2
        0 {F[0][0]:3} {F[0][1]:3} {F[0][2]:3} |
        1 {F[1][0]:3} {F[1][1]:3} {F[1][2]:3} |
        2 {F[2][0]:3} {F[2][1]:3} {F[2][2]:3} |
           ___ ___ ___
        """
    print(fild)




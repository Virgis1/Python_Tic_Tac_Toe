table1 = ['1', '|', '2', '|', '3']
table2 = ['4', '|', '5', '|', '6']
table3 = ['7', '|', '8', '|', '9']

player1_win = False
player2_win = False
count = 0
def showTable():
    for row in table1:
        print(row, end="")
    print()
    for row in table2:
        print(row, end="")
    print()
    for row in table3:
        print(row, end="")

def check_x_win():
    global player1_win
    if ((table1[0] == 'X' and table1[2] == 'X' and table1[4] == 'X')
            or
    (table2[0] == 'X' and table2[2] == 'X' and table2[4] == 'X')
            or
    (table3[0] == 'X' and table3[2] == 'X' and table3[4] == 'X')
            or
    (table1[0] == 'X' and table2[0] == 'X' and table3[0] == 'X')
            or
    (table1[2] == 'X' and table2[2] == 'X' and table3[2] == 'X')
            or
    (table1[4] == 'X' and table2[4] == 'X' and table3[4] == 'X')
            or
    (table1[0] == 'X' and table2[2] == 'X' and table3[4] == 'X')
            or
    (table1[4] == 'X' and table2[2] == 'X' and table3[0] == 'X')):
        # print('Player1 wins')

        player1_win = True

def check_0_win():
    global player2_win
    if ((table1[0] == '0' and table1[2] == '0' and table1[4] == '0')
            or
    (table2[0] == '0' and table2[2] == '0' and table2[4] == '0')
            or
    (table3[0] == '0' and table3[2] == '0' and table3[4] == '0')
            or
    (table1[0] == '0' and table2[0] == '0' and table3[0] == '0')
            or
    (table1[2] == '0' and table2[2] == '0' and table3[2] == '0')
            or
    (table1[4] == '0' and table2[4] == '0' and table3[4] == '0')
            or
    (table1[0] == '0' and table2[2] == '0' and table3[4] == '0')
            or
    (table1[4] == 'X' and table2[2] == 'X' and table3[0] == 'X')):
        # print('Player1 wins')

        player2_win = True

def player1_move():
    match player1:
        case '1':
            table1[0] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '2':
            table1[2] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '3':
            table1[4] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '4':
            table2[0] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '5':
            table2[2] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '6':
            table2[4] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '7':
            table3[0] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '8':
            table3[2] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case '9':
            table3[4] = 'X'
            showTable()
            check_x_win()
            if player1_win:
                print(f'\nplayer1 win')
                return True
        case _:
            print("Neteisingai pasirinktas veiksmas")

def player2_move():
    match player2:
        case '1':
            table1[0] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '2':
            table1[2] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '3':
            table1[4] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '4':
            table2[0] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '5':
            table2[2] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '6':
            table2[4] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '7':
            table3[0] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '8':
            table3[2] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case '9':
            table3[4] = '0'
            showTable()
            check_0_win()
            if player2_win:
                print(f'\nplayer2 win')
                return True
        case _:
            print("Neteisingai pasirinktas veiksmas")

showTable()

while True:
    player1 = input(f'\nZaidejas1 pasirinkite laukeli, i kuri deti "X" ')
    player1_move()
    count += 1
    if player1_win or player2_win:
        break
    elif count == 9:
        print('\nlygiosios')
        break
    player2 = input(f'\nZaidejas2 pasirinkite laukeli, i kuri deti "0" ')
    player2_move()
    count += 1
    if player1_win or player2_win:
        break
    elif count == 9:
        print(f'\nlygiosios')
        break

import string


def print_grid(played_grid):
    print("-" * 9)
    for row in range(3):
        print("| " + " ".join(grid[row * 3:(row + 1) * 3]) + " |")
    print("-" * 9)


def has_in_a_row(played_grid, player):
    return played_grid[0:3] == 3 * player or played_grid[3:6] == 3 * player or played_grid[6:9] == 3 * player or\
           played_grid[0::3] == 3 * player or played_grid[1::3] == 3 * player or played_grid[2::3] == 3 * player or\
           played_grid[0::4] == 3 * player or played_grid[2:7:2] == 3 * player


def is_impossible(played_grid):
    return abs(played_grid.count('X') - played_grid.count('O')) >=2 or\
           has_in_a_row(played_grid, 'X') and has_in_a_row(played_grid, 'O')


def has_empty_cells(played_grid):
    return '_' in played_grid


def analyze_grid(played_grid):
    if is_impossible(grid):
        print('Impossible')
    elif has_in_a_row(grid, 'O'):
        print('O wins')
    elif has_in_a_row(grid, 'X'):
        print('X wins')
    elif not has_empty_cells(grid):
        print('Draw')
    else:
        print('Game not finished')
        return False
    return True

def is_move_ok(played_grid, current_move):
    if current_move[0] not in string.digits or current_move[1] not in string.digits:
        print('You should enter numbers!')
    elif int(current_move[0]) not in range(1,4) or int(current_move[1]) not in range(1,4):
        print('Coordinates should be from 1 to 3!')
    elif '_' not in played_grid[(int(current_move[0]) - 1) * 3 + int(current_move[1]) - 1]:
        print('This cell is occupied! Choose another one!')
    else:
        return True
    return False


grid = '_________'
players = ['X', 'O']
player = 0

print_grid(grid)
while True:
    move = input().split(' ')
    if is_move_ok(grid, move):
        index = (int(move[0]) - 1) * 3 + int(move[1]) - 1
        if index == 0:
            grid = players[player] + grid[1:]
        elif index == 8:
            grid = grid[:-1] + players[player]
        else:
            grid = grid[:index] + players[player] + grid[index + 1:]
        print_grid(grid)
        player = int(not player)
        if analyze_grid(grid):
            break

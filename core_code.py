import numpy as np
from matplotlib import pyplot as plt

diags = [
 [[0, 0], [1, 1], [2, 2], [3, 3]],
 [[0, 1], [1, 2], [2, 3], [3, 4]],
 [[0, 2], [1, 3], [2, 4], [3, 5]],
 [[0, 3], [1, 4], [2, 5], [3, 6]],
 [[1, 0], [2, 1], [3, 2], [4, 3]],
 [[1, 1], [2, 2], [3, 3], [4, 4]],
 [[1, 2], [2, 3], [3, 4], [4, 5]],
 [[1, 3], [2, 4], [3, 5], [4, 6]],
 [[2, 0], [3, 1], [4, 2], [5, 3]],
 [[2, 1], [3, 2], [4, 3], [5, 4]],
 [[2, 2], [3, 3], [4, 4], [5, 5]],
 [[2, 3], [3, 4], [4, 5], [5, 6]],
 [[0, 6], [1, 5], [2, 4], [3, 3]],
 [[0, 5], [1, 4], [2, 3], [3, 2]],
 [[0, 4], [1, 3], [2, 2], [3, 1]],
 [[0, 3], [1, 2], [2, 1], [3, 0]],
 [[1, 6], [2, 5], [3, 4], [4, 3]],
 [[1, 5], [2, 4], [3, 3], [4, 2]],
 [[1, 4], [2, 3], [3, 2], [4, 1]],
 [[1, 3], [2, 2], [3, 1], [4, 0]],
 [[2, 6], [3, 5], [4, 4], [5, 3]],
 [[2, 5], [3, 4], [4, 3], [5, 2]],
 [[2, 4], [3, 3], [4, 2], [5, 1]],
 [[2, 3], [3, 2], [4, 1], [5, 0]],
 ]

def show_board(board):
    fig, ax = plt.subplots()
    ax.imshow(board, cmap='Greys', vmin=-1, vmax=1)
    ax.set_yticks([])
    ax.set_xticks(np.linspace(.5, 6.5, 7), minor=True)
    ax.set_yticks(np.linspace(.5, 5.5, 6), minor=True)
    ax.grid(True, which='minor', )
    plt.show()
    
def check_move(board, move):
    if isinstance(move, type(None)):
        return False
    elif move not in range(0,7):
        valid = False
    else:
        valid = board[5-np.sum(board[:,move]!=0), move] == 0
    if not valid:
        print("Invalid Move!")
    return valid

def init_possible_wins():
    wins = []
    for row in range(6):
        for col in range(7-3):
            win = np.zeros((1,6,7))
            win[0,row,col:col+4] = 1
            wins.append(win)
    for col in range(7):
        for row in range(6-3):
            win = np.zeros((1,6,7))
            win[0,row:row+4,col] = 1
            wins.append(win)
    for diag in diags:
        win = np.zeros((1,6,7))
        for spot in diag:
            win[0,spot[0],spot[1]]=1
        wins.append(win)
    wins = np.array(wins)
    return wins.reshape(wins.shape[0], -1)

possible_wins = init_possible_wins()
    
def check_win(board):
    return 4 in np.abs(board.reshape(1,-1) @ possible_wins.T)

def return_outcome(board, player):
    if check_win(board):
        return player*-1
    elif np.sum(board==0) == 0:
        return 0
    else:
        return None
    

def test_bot(board, player):
    return np.random.randint(0,7,1)[0]

def play(bots=None, display_board=True):
    board = np.zeros((6,7))
    player = 1
    while not check_win(board):
        if display_board:
            show_board(board)
        move = None
        while not check_move(board, move):
            if isinstance(bots, type(None)) or (len(bots)==1 and player==1):
                move = int(input(f"\n{'Black' if player==1 else 'White'}, choose a column: "))
            else:
                move = bots[0](board.copy(),player) if player==-1 else bots[1](board.copy(),player)
        board[5-np.sum(board[:,move]!=0), move] = player
        player *= -1
    if display_board:
        show_board(board)
    outcome = return_outcome(board, player)
    if outcome == 0:
        print("It's a Draw!")
    else:
        print('Black' if player!=1 else 'White', "has won!")
    return outcome
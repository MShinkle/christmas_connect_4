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
    
def check_win(board):
    won = False
    for row in range(board.shape[0]-3):
        if 4 in np.abs(np.sum(board[row:row+4], axis=0)):
            won=True
    for col in range(board.shape[1]-3):
        if 4 in np.abs(np.sum(board[:,col:col+4], axis=1)):
            won=True
    if np.sum(board==0) == 0:
        won=True
    for diag in diags:
        piece_sum = 0
        for pt in diag:
            piece_sum += board[pt[0], pt[1]]
        if abs(piece_sum) == 4:
            won=True
    return won

def test_bot:
    return np.random.randint(0,7,1)[0]

def play(bots=None):
    board = np.zeros((6,7))
    player = 1
    while not check_win(board):
        show_board(board)
        move = None
        while not check_move(board, move):
            if isinstance(bots, type(None)):
                move = int(input(f"\n{'Black' if player==1 else 'White'}, choose a column: "))
            else:
                move = bots[0](board,player) if player==1 else bots[1](board,player)
        board[5-np.sum(board[:,move]!=0), move] = player
        player *= -1
    show_board(board)
    if np.sum(board==0) == 0:
        print("It's a Draw!")
        return 0
    else:
        print('Black' if player!=1 else 'White', "has won!")
        return player*-1
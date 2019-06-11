import numpy as np

def is_ok(board, x, y):
    row_sum = board[x, :].sum()
    col_sum = board[:, y].sum()
    dia_sum = sum([ board[a,b] for a in range(8) for b in range(8) if a + b == x + y or (x - a) == (y - b)])
    # print(f'row sum = {row_sum}, col_sum = {col_sum}, dia_sum = {dia_sum}')
    if row_sum == 0 and col_sum == 0 and dia_sum == 0:
        return True
    else:
        return False

def findQueen(board, row):
    global total
    if row == 8:
        print_board(board)
        total += 1
        print(f'Find {total} solution(s)'.center(50, '-'))
        # return
    else:
        for col in range(8):
            if is_ok(board, row, col):
                board[row, col] = 1
                findQueen(board, row + 1)
                board[row, col] = 0 # reset because this is the wrong decision

def print_board(board):
    for i in range(8):
        for j in range(8):
            print('[ ]', end='') if board[i, j] == 0 else print('[X]', end='')
        print()


def main():
    global total
    total = 0
    board = np.zeros(64).reshape(8, 8)
    findQueen(board, 0)


if __name__ == '__main__':
    main()

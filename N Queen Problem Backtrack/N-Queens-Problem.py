global size
size = 6


def solve(board, col):
    if col >= size:
        return True
    
    for row in range(size):
        if is_safe_to_put(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1) == True:
                return True
            board[row][col] = 0
        
    return False


def is_safe_to_put(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i,j in zip(range(row, size, 1), (col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def print_board(board):
    for row in range(size):
        for col in range(size):
            print(board[row][col], end = " ")
        print()


def main():
    board = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0] ]
    
    if solve(board, 0) == False:
        print("No solution exists")
        return False

    print_board(board)

main()


import math

# Print the board
def print_board(board):
    for row in board:
        print(row)

# Check winner
def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X": return -1
    if winner == "O": return 1
    if not empty_cells(board): return 0
    
    if is_maximizing:
        best_score = -math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for (i, j) in empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Main game
board = [[" " for _ in range(3)] for _ in range(3)]
while True:
    print_board(board)
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    if board[row][col] == " ":
        board[row][col] = "X"
    else:
        print("Invalid move, try again!")
        continue
    
    if check_winner(board) == "X":
        print_board(board)
        print("You win!")
        break
    
    if not empty_cells(board):
        print_board(board)
        print("It's a draw!")
        break
    
    move = best_move(board)
    board[move[0]][move[1]] = "O"
    
    if check_winner(board) == "O":
        print_board(board)
        print("AI wins!")
        break

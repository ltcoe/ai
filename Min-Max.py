# Initialize the tic-tac-toe board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("---------")

def is_winner(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_full(board):
    return " " not in board

def is_game_over(board):
    return is_winner(board, "X") or is_winner(board, "O") or is_full(board)

def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return evaluate(board)

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = -1
    best_eval = -float("inf")

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i

    return best_move

# Main game loop
while not is_game_over(board):
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == " ":
        board[player_move] = "O"
    else:
        print("Invalid move. Try again.")
        continue

    if is_game_over(board):
        break

    computer_move = find_best_move(board)
    board[computer_move] = "X"

print_board(board)
if is_winner(board, "X"):
    print("Computer wins!")
elif is_winner(board, "O"):
    print("You win!")
else:
    print("It's a tie!")

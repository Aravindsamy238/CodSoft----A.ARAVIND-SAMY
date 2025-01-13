import random

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"
WINNING_COMBOS = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8], 
    [0, 4, 8], 
    [2, 4, 6], 
]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    for combo in WINNING_COMBOS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(cell != EMPTY for cell in board)

def minimax(board, depth, is_maximizing_player, alpha, beta):
    if check_winner(board, PLAYER_X):
        return -10 + depth  
    if check_winner(board, PLAYER_O):
        return 10 - depth  
    if is_board_full(board):
        return 0  
    
    if is_maximizing_player:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_O
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = PLAYER_X
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = PLAYER_O
            move_val = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == EMPTY:
                return move
            else:
                print("This cell is already occupied.")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

def play_game():
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        move = human_move(board)
        board[move] = PLAYER_X
        print_board(board)
        
        if check_winner(board, PLAYER_X):
            print("Congratulations! You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        
        print("AI's turn:")
        move = best_move(board)
        board[move] = PLAYER_O
        print_board(board)
        
        if check_winner(board, PLAYER_O):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()


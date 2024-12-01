def minmax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X": 
        return 10 - depth
    elif winner == "O":  
        return depth - 10
    elif is_draw(board):  
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move] = "X"  
            score = minmax(board, depth + 1, False)
            board[move] = " "  
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "O"  
            score = minmax(board, depth + 1, True)
            board[move] = " "  
            best_score = min(best_score, score)
        return best_score

def check_winner(board):
    
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            return board[combination[0]]
    return None

def is_draw(board):
    return " " not in board  

def get_available_moves(board):
    return [i for i in range(len(board)) if board[i] == " "] 


def best_move(board):
    best_score = float("-inf")
    move = None
    for i in get_available_moves(board):
        board[i] = "X" 
        score = minmax(board, 0, False)
        board[i] = " " 
        if score > best_score:
            best_score = score
            move = i
    return move


board = [
    "X", "O", "X",
    "O", "X", " ",
    " ", "O", " "
]

print("Best Move for X:", best_move(board))

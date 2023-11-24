def evaluate(board):
    # Checking rows for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10

    # Checking columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10

    # Checking diagonals for a win
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10

    # No winner yet
    return 0


def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # If the maximizer or minimizer wins the game, return the score
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth

    # If there are no more moves left, it's a tie
    if not is_moves_left(board):
        return 0

    # Maximizing player's turn
    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    alpha = max(alpha, best)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best
    else:  # Minimizing player's turn
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    beta = min(beta, best)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best


def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    alpha = -1000
    beta = 1000

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, alpha, beta)
                board[i][j] = '_'

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


# Example usage:
if __name__ == "__main__":
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]

    print("Current Board State:")
    for row in board:
        print(" ".join(row))

    while is_moves_left(board):
        player_row = int(input("Enter row (0, 1, or 2): "))
        player_col = int(input("Enter column (0, 1, or 2): "))
        if board[player_row][player_col] != '_':
            print("Invalid move. Cell already taken. Try again.")
            continue
        board[player_row][player_col] = 'O'

        if evaluate(board) == -10:
            print("You win!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'

        print("Current Board State:")
        for row in board:
            print(" ".join(row))

        if evaluate(board) == 10:
            print("AI wins!")
            break

        if not is_moves_left(board):
            print("It's a tie!")
            break

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def display_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

def get_player_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = player
                return True
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def check_win():
    for player in ["X", "O"]:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)) or \
               all(board[j][j] == player for j in range(3)) or \
               all(board[j][2-j] == player for j in range(3)):
                return player
    return None

def check_draw():
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def main():
    player = "X"
    while True:
        display_board()
        if get_player_move(player):
            winner = check_win()
            if winner:
                display_board()
                print(f"Player {winner} wins!")
                break
            elif check_draw():
                display_board()
                print("Game over: Draw")
                break
            player = "O" if player == "X" else "X"

if __name__ == "__main__":
    main()

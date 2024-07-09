import random

class TicTacToe:
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def get_random_first_player(self):
        return random.randint(0, 1)
    
    def fix_spot(self, row, col, player):
        if self.board[row][col] == '-':
            self.board[row][col] = player
            return True
        else:
            print("Spot already taken. Choose another spot.")
            return False

    def is_player_win(self, player):
        n = len(self.board)

        # Check rows
        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)):
                return True

        # Check columns
        for j in range(n):
            if all(self.board[i][j] == player for i in range(n)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(n)):
            return True
        if all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def is_board_filled(self):
        for row in self.board:
            if '-' in row:
                return False
        return True
    
    def swap_player(self, player):
        return 'X' if player == '0' else '0'
    
    def show_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def start(self):
        player = 'X' if self.get_random_first_player() == 1 else '0'
        while True:
            print(f"Player {player}'s turn")
            self.show_board()

            # Taking user input
            try:
                row, col = map(int, input("Enter row and column numbers to fix spot (1-3): ").split())
                if row < 1 or row > 3 or col < 1 or col > 3:
                    print("Invalid input. Please enter values between 1 and 3.")
                    continue
                if not self.fix_spot(row - 1, col - 1, player):
                    continue
            except ValueError:
                print("Invalid input. Please enter integer values.")
                continue

            # Check if the current player has won
            if self.is_player_win(player):
                self.show_board()
                print(f"Player {player} wins the game!")
                break

            # Check if the game is a draw
            if self.is_board_filled():
                print("Match Draw!")
                break

            # Swap player
            player = self.swap_player(player)

        # Show the final view of the board
        print("Final board:")
        self.show_board()

# Starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()

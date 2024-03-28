import random

class BattleshipGame:
    def __init__(self):
        self.board_size = 10
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.player_ships = []
        self.computer_ships = []
        self.ships = {"Aircraft Carrier": 5, "Battleship": 4, "Submarine": 3, "Cruiser": 3, "Destroyer": 2}
        self.ship_symbols = {"Aircraft Carrier": "A", "Battleship": "B", "Submarine": "S", "Cruiser": "C", "Destroyer": "D"}

    def create_board(self):
        return [[" " for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ships(self):
        for ship, size in self.ships.items():
            self.place_ship(self.player_board, ship, size)
            self.place_ship(self.computer_board, ship, size, random_placement=True)

    def place_ship(self, board, ship, size, random_placement=False):
        while True:
            if random_placement:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - size)
                else:
                    row = random.randint(0, self.board_size - size)
                    col = random.randint(0, self.board_size - 1)
            else:
                print(f"Placing {ship} of size {size}")
                row, col = map(int, input("Enter coordinates (row, col): ").split())
                orientation = input("Enter orientation (horizontal or vertical): ").lower()

            if self.is_valid_placement(board, row, col, size, orientation):
                self.add_ship_to_board(board, ship, row, col, size, orientation)
                break
            else:
                print("Invalid placement! Try again.")

    def is_valid_placement(self, board, row, col, size, orientation):
        if orientation == "horizontal":
            for c in range(col, col + size):
                if board[row][c] != " ":
                    return False
        else:
            for r in range(row, row + size):
                if board[r][col] != " ":
                    return False
        return True

    def add_ship_to_board(self, board, ship, row, col, size, orientation):
        if orientation == "horizontal":
            for c in range(col, col + size):
                board[row][c] = self.ship_symbols[ship]
        else:
            for r in range(row, row + size):
                board[r][col] = self.ship_symbols[ship]
        self.ships[ship] -= 1
        if self.ships[ship] == 0:
            del self.ships[ship]

    def player_turn(self):
        while True:
            try:
                row, col = map(int, input("Enter coordinates to fire (row, col): ").split())
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    if self.computer_board[row][col] == " ":
                        print("Miss!")
                        self.computer_board[row][col] = "O"
                    elif self.computer_board[row][col] == "X" or self.computer_board[row][col] == "*":
                        print("You've already fired at this position!")
                    else:
                        print("Hit!")
                        ship_symbol = self.computer_board[row][col]
                        self.computer_board[row][col] = "X"
                        if self.check_ship_sunk(self.computer_board, ship_symbol):
                            print(f"You've sunk the {self.get_ship_name(ship_symbol)}!")
                        if not self.computer_ships:
                            print("You've won!")
                            return
                    break
                else:
                    print("Invalid coordinates! Please enter coordinates within the board.")
            except ValueError:
                print("Invalid input! Please enter row and column numbers.")

    def computer_turn(self):
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if self.player_board[row][col] == " ":
                print(f"Computer fires at {row}, {col}")
                print("Miss!")
                self.player_board[row][col] = "O"
                break
            elif self.player_board[row][col] == "X" or self.player_board[row][col] == "*":
                continue
            else:
                print("Computer fires at", row, col)
                print("Hit!")
                ship_symbol = self.player_board[row][col]
                self.player_board[row][col] = "X"
                if self.check_ship_sunk(self.player_board, ship_symbol):
                    print(f"Computer has sunk your {self.get_ship_name(ship_symbol)}!")
                if not self.player_ships:
                    print("Computer wins!")
                    return

    def check_ship_sunk(self, board, ship_symbol):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if board[row][col] == ship_symbol:
                    return False
        return True

    def get_ship_name(self, ship_symbol):
        for ship, symbol in self.ship_symbols.items():
            if symbol == ship_symbol:
                return ship

    def display_board(self, board):
        print("  ", " ".join(str(i) for i in range(self.board_size)))
        for i, row in enumerate(board):
            print(i, " ".join(row))

    def run(self):
        print("Welcome to Battleship!")
        self.place_ships()
        while True:
            print("\nPlayer's Turn:")
            self.display_board(self.player_board)
            self.player_turn()

            print("\nComputer's Turn:")
            self.computer_turn()
            print()

            input("Press Enter to continue...")


if __name__ == "__main__":
    game = BattleshipGame()
    game.run()

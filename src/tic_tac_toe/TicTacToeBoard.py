class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None

    def is_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def play_game(self):
        while True:
            self.print_board()
            row = int(input(f"Player {self.current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {self.current_player}, enter column (0, 1, 2): "))

            if self.make_move(row, col):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == "Draw":
                        print("It's a draw!")
                    else:
                        print(f"Player {winner} wins!")
                    break

                if self.is_full():
                    self.print_board()
                    print("It's a draw!")
                    break

                self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()

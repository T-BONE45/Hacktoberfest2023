class ChessGame:
    def __init__(self):
        self.board = self.setup_board()
        self.current_player = 'White'

    def setup_board(self):
        # Create an 8x8 chess board as a list of lists
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # Place initial chess pieces on the board
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[1] = ['P'] * 8
        board[6] = ['p'] * 8
        board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

        return board

    def print_board(self):
        # Print the chess board
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, piece, start, end):
        # Check if the move is valid
        # Implement chess rules here
        return True

    def move_piece(self, start, end):
        # Move a piece from start to end if the move is valid
        piece = self.board[start[0]][start[1]]
        if self.is_valid_move(piece, start, end):
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = ' '

    def play(self):
        while True:
            self.print_board()
            print(f"{self.current_player}'s turn.")
            move = input("Enter your move (e.g., 'e2 e4'): ").split()
            
            if len(move) != 2:
                print("Invalid input. Try again.")
                continue

            start = (int(move[0][1]) - 1, ord(move[0][0]) - ord('a'))
            end = (int(move[1][1]) - 1, ord(move[1][0]) - ord('a'))

            if not self.is_valid_input(start) or not self.is_valid_input(end):
                print("Invalid input. Try again.")
                continue

            if self.is_valid_move(self.board[start[0]][start[1]], start, end):
                self.move_piece(start, end)
                self.current_player = 'Black' if self.current_player == 'White' else 'White'
            else:
                print("Invalid move. Try again.")

    def is_valid_input(self, pos):
        # Check if the input position is within the board bounds
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8


if __name__ == "__main__":
    game = ChessGame()
    game.play()

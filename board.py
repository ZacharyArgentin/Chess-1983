import piece

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize an 8x8 chess board with pieces in starting positions
        board = [[None for _ in range(8)] for _ in range(8)]  # Placeholder for an empty board
        for y, rank in enumerate(board):
            for x, file in enumerate(rank):
                if y == 0:  # Black pieces
                    if x == 0 or x == 7:  # Rooks
                        board[y][x] = piece.Rook("black")
                    elif x == 1 or x == 6:  # Knights
                        board[y][x] = piece.Knight("black")
                    elif x == 2 or x == 5:  # Bishops
                        board[y][x] = piece.Bishop("black")
                    elif x == 3:  # Queen
                        board[y][x] = piece.Queen("black")
                    elif x == 4:  # King
                        board[y][x] = piece.King("black")
                if y == 1:  # Black pawns
                    board[y][x] = piece.Pawn("black")
                if y == 6:  # White pawns
                    board[y][x] = piece.Pawn("white")
                if y == 7:  # White pieces
                    if x == 0 or x == 7:  # Rooks
                        board[y][x] = piece.Rook("white")
                    elif x == 1 or x == 6:  # Knights
                        board[y][x] = piece.Knight("white")
                    elif x == 2 or x == 5:  # Bishops
                        board[y][x] = piece.Bishop("white")
                    elif x == 3:  # Queen
                        board[y][x] = piece.Queen("white")
                    elif x == 4:  # King
                        board[y][x] = piece.King("white")
        return board


    def print_board(self):
        for i, row in enumerate(self.board):
            # print the rank number on the left side
            print(8-i, end="")
            print("|", end="")
            # print the contents of each square
            for square in row:
                if square:
                    print(square, end=" ") # Print the piece symbol
                else:
                    print("-", end=" ")  # Print a dash for empty squares
            print()  # Print a newline after each row
        # print("  " + "_" * 16)  # Print the file labels at the bottom
        print("  a b c d e f g h")  # Print the file labels at the bottom
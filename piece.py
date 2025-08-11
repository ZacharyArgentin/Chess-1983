class Piece:

    unicode_symbols = {
    # The color-filled unicode chess pieces are dubbed "black", however they appear white
    # in a terminal with a dark background.
    # We will assume 95% of the time the player will have a dark background. So we will call the
    # filled pieces "white" and the empty pieces "black".
    # We'll add an option later to switch if needed.
    'black': {
        'king':   '\u2654',  # ♔
        'queen':  '\u2655',  # ♕
        'rook':   '\u2656',  # ♖
        'bishop': '\u2657',  # ♗
        'knight': '\u2658',  # ♘
        'pawn':   '\u2659',  # ♙
    },
    'white': {
        'king':   '\u265A',  # ♚
        'queen':  '\u265B',  # ♛
        'rook':   '\u265C',  # ♜
        'bishop': '\u265D',  # ♝
        'knight': '\u265E',  # ♞
        'pawn':   '\u265F',  # ♟
    }
}

    def __init__(self, color):
        """
        Initialize a chess piece with a color and a position.
        :param color: 'white' or 'black'
        :param position: Initial position on the board (e.g., 'e4')
        """
        self.symbol = "?"  # Placeholder symbol for generic piece
        self.color = color  # 'white' or 'black'
        # self.position = position  # Will be set when the piece is placed on the board
        self.is_captured = False  # Track if the piece has been captured

    def __str__(self):
        return self.symbol

    # def symbol(self):
    #     return "?"  # Placeholder symbol for generic piece
    #     # raise NotImplementedError("This method should be overridden by subclasses")

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("This method should be overridden by subclasses")
    

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["pawn"]


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["rook"]

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["knight"]

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["bishop"]

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["queen"]

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = self.unicode_symbols[color]["king"]
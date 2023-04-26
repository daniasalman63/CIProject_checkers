class Piece:

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.row = row
        self.col = col

    def __repr__(self):
        return str(self.color)
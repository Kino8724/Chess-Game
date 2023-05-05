class Player:
    def __init__(self, name):
        self.name = name
        self.total_points = 0
        self.color = 0
        self.hasWon = False

class Piece:
    def __init__(self):
        self.color = ""
        self.points = 0
        self.inplay = True
        self.can_move = True

class Pawn:
    pass

class Knight:
    pass

class Rook:
    pass

class Bishop:
    pass

class King:
    pass

class Queen:
    pass



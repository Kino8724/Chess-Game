import PySimpleGUI as sg

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

class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Rook(Piece):
    pass

class Bishop(Piece):
    pass

class King(Piece):
    pass

class Queen(Piece):
    pass

def main():
    layout = [[sg.Canvas(background_color="White", size=(500,500), expand_x=True, expand_y=True)]]

    # Create the window
    window = sg.Window("Hello", layout, resizable = True)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()



if __name__ == "__main__":
    main()

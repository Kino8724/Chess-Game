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
    #-----things to figure out-----#
    # Opens at default size, can expand, but has a minimum size req
    # Figure out how to show grid lines
    # Show graph position, according to mouse position (text box next to mouse)[hide later]
    # Get tiles on the board

    layout = [[sg.Graph(canvas_size=(500,500), 
                        key="Board", 
                        background_color="White", 
                        enable_events = True, 
                        motion_events = True, 
                        graph_bottom_left= (-250,-250), 
                        graph_top_right=(250,250), 
                        expand_x= False, 
                        expand_y= False)]]

    # Create the window
    window = sg.Window("Hello", layout, resizable = True)
    window.Finalize()
    window["Board"].draw_rectangle((0,0), (0,0), fill_color= 'purple', line_color='purple')
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


class Game:
    """
    Main class for the game to be played
    """
    def __init__(self):
        """
        Function to create the game board
        """
        # Create the list with length 9 that represents
        # a 3x3 game board
        self.board = ['  ' for _ in range(9)]

        # Variable to keep track of who the current winner is
        self.current_winner = None

    def show_board(self):
        """
        Function that will show the board on
        the command line
        """

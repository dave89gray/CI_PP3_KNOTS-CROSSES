
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
        # a for loop for i in range of 3, which 3 spaces
        # are chosen which represents the row indices i.e first row = 012
        for row in [self.board[i*3:(i+i)*3] for i in range(3)]:
            # String concatentation to print vertical lines
            # for the game board for each row
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    ##
    def show_board_layout():
        """
        Function to show which numbers are at which spot on the board
        i.e 0|1|2. Board layout to be populated with a string for each
        i in the range of the board size, create 3 sub-arrays
        """

        board_layout = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

        # for loop to add the 3 rows of the board and add columns lines
        for row in board_layout:
            # String concatentation to print vertical lines
            # for the game board for each row
            print('| ' + ' | '.join(row) + ' |')

    def player_moves(self):
        """
        Function to return a list of indices of the available moves
        for a player after they have made a move
        """

        # Empty list to add moves to
        moves = []

        # Add enumerate to create a list and assign tuples that have
        # the index and the value at the index i.e 0,X 1,X

        for (i, place) in enumerate(self.board):
            # For loop to go through each tuple and assign first item to i
            # and the second item to 'place'. if place empty space
            # then its an available move, then add i to the list
            if place == ' ':
                moves.append(i)
            return moves

    def available_selection(self):
        """
        Function to check if there are any avaialble selections for the
        game player to make.
        """

        # Space and self. are to be returned a boolean (true or false)
        # of whether they are indeed available selections
        return " " in self.board

    def available_selections_left(self):
        """
        Function to return the number of empty squares left on the game board
        """
        return len(self.player_moves())

    def player_move(self, box, player):
        """
        Function to check if the chosen move is valid, to then make
        the move i.e place a letter in a box and if the move is good
        it is to return true, if the move is invalid it will return false
        """
        # if statement to check if the selected box is empty (available)
        if self.board[box] == ' ':
            self.board[box] = player
            return True
        return False


def play_game(Game, player_x, player_O, print_game=True):
    """
    Function for the game to play and pass it the arguments of game,
    and players for x & o. The extra variable for print is included so
    if it is set to True it prints out all steps for the user to
    play the game. This function is to iterate continually until
    there are no more moves left i.e someone wins or ties
    """

    if print_game:
        # Printing the board so the user can see which numbers
        # are in which position on the board
        Game.show_board_layout()

    # Assigns the starting letter as "X"
    player = "X"

    # Keep iterating through the game while there are moves available
    while Game.available_selection():
        # make sure the correct player is making the next move, if
        # its not player O then it's player X
        if player == 'O':
            box = player_O.get_next_move(Game)
        else:
            box = player_x.get_next_move(Game)

        # Takes the available squares and player letter as arguments
        if Game.player_move(box, player):
            if print_game:
                print(player + f' made a move to {box}')
                Game.show_board()
                print('')

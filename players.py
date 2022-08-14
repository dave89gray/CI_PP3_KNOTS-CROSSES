import random

class Player:
    """
    Base player class for the player of the game which
    the user or computer will be be derived from
    """
    def __init__(self, player):
        """
        This function represents which player is playing
        """
        # Set the current instance of player (user or computer)
        self.player = player

        def get_next_move(self, game):
            """
            This function ensures each player gets a next
            move if its available
            """
            pass

class User(Player):
    """
    User to inherit the base Player function and develop it
    further into the user
    """  
    def __init__(self, player):
        """
        Function to create instance of user while using
        super() to inherit player attributes
        """
        super().__init__(player)

    def get_next_move(self, game):
        """
        Function to allow the uer to imput their choice of square,
        we will check if it is a number or valid input or if the
        chosen square on the board is not available
        """
        check_square = False
        # Default value of None as user is yet to put an input in
        check = None

        # While check_square is false, user selection is going to be
        while not check_square:
            # Command terminal to show who's turn is it is and prompt
            # a move 0 to 8
            selection = input(self.player + '\'s turn. Please choose from (0-8): \n')

        # Try block to test if the user selection is an integer and valid
        # or the move is not available on the board we
        # tell the user and raise a Value Error
        try:
            check = int(square)
            if check not in game.available_moves():
                raise ValueError()

            # If the selection passes both those check then it's
            # a valid move and passes true
            check_square = True
        except ValueError:
            print("Ooops, looks like that was an invalid choice, please try again!")
        
        return check


class Computer(Player):
    """
    Function to create instance of user while using
    super() to inherit player attributes
    """
    def __init__(self, player):
        super().__init__(player)

    def get_next_move(self, game):
        """
        Function for the Computer to select a random square on the
        board thats empty, passing our game in as an argument
        and returning the square the computer chose
        """
        square = random.choice(game.player_moves())
        return square

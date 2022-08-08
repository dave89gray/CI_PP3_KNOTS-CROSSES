
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

class computer(player):
        """
        Function to create instance of user while using
        super() to inherit player attributes
        """
        super().__init__(player)

        def get_next_move(self, game):


class User:
    """
    Base player class for the player of the game
    """
    def __init__(self, player):
        """
        This function represents which player is playing
        """
        # Set the current instance of player (user or computer)
        self.player = player
welcome_ascii = """

              |          |
              |          |
        ______|__________|_______
              |          |
              |          |
              |          |
              |          |
        ______|__________|_______
              |          |
              |          |

        """

class Welcome:
    """
    Contains a function that will print the welcome
    """
    def welcome(self):
        """
        This function shall print the welcome
        message and the ASCII game board
        """
        print("Welcome to Knoughts and Crosses")
        print(welcome_ascii)
        print("Shall we play a game?")

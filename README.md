# Knoughts and Crosses
(Developer: David Gray)

![Home Screen]

## Table of Contents

1.  [Project Goals](#project-goals)
    1.  [User Goals](#user-goals)
    2.  [Site Owner Goals](#site-owner-goals)
2.  [User Experience](#user-experience)
    1.  [Target Audience](#target-audience)
    2.  [User requirements and Expectations](#user-requirements-and-expectations)
    3.  [User Stories](#user-stories)
    4.  [Site Owner Stories](#site-owner-stories)
3.  [Design](#design)
    1.  [Flowchart](#flowchart)
4.  [Technologies Used](#technologies-used)
    1.  [Languages](#languages)
    2.  [Frameworks and Tools](#frameworks-and-tools)
5.  [Features](#features)
6.  [Validation](#validation)
    1.  [PEP8](#pep8)
    2.  [Test User Stories](#test-user-stories)
7.  [Bugs](#bugs)
8.  [Deployment](#deployment)
9.  [Future Considerations](future-considerations)
10. [Credits](credits)
11. [Acknowledgments](#acknowledgments)

## Project Goals
Knoughts and Crosses is an app of the classic that the user can play in the terminal.

### User Goals
- Enjoy a game of Knoughts and Crosses

### Site Owner Goals
- Offer a simple and easy to use game to players who want some relaxing fun

## User Experience

### Target Audience
- Knoughts and Crosses Enthusiasts
- Children who want to learn the game

### User Requirements and Expectations
- That the game is easy to use
- That the game is easy to understand
- That the game is easy to read on the terminal

### User Stories
1. As a user, I want to be able to see what numbers correspond to which square
2. As a user, I want to be able to choose which square my letter goes into
3. As a user, i want to see my selection appear on the game board
4. As a user, I want to have an opponent
5. As a user, I want to see who's turn it is next
6. As a user, I want to see the winner

### Site Owner Stories
7. As a site owner, I want the user to select whichever square they want
8. As a site owner, I want the user to get feedback on who won the game
9. As a site owner, I was the user to have fun!

## Design

### Flowchart
<details><summary>Flowchart</summary>
<img src="documents/flowchart_knoughts_and_crosses.png">
</details>

## Technologies Used

### Languages
- Python 3

### Frameworks and Tools
- GitHub
- GitPod
- Git
- Lucid Charts - to create Flowchart

## Features

### Welcome Message
- The welcome message is printed welcome message and ASCII art of a Knoughts and Crossed board

<details><summary>Welcome Message</summary>
<img src="documents/features/features_welcome_message.png">
</details>

### Game Board
- Shows the user the game board and which numbers apply to which square
- User stories 1, 3, 7

<details><summary>Game Board</summary>
<img src="documents/features/features_game_board.png">
</details>

### User Input
- Input line for the user to make their selection
- User stories 2, 5, 7

<details><summary>User Input</summary>
<img src="documents/features/features_user_input.png">
</details>

### Game Progressing
- Each players selection should progressively populate the board
- User story 3, 4

<details><summary>Game Progressing</summary>
<img src="documents/features/features_game_progressing.png">
</details>

### Alternating Players
- There has to be an opponent to play against and no player can play more than one shot at a time
- User story 4, 5

<details><summary>Alternating Players</summary>
<img src="documents/features/features_alternating_players.png">
</details>

### Feedback error
- The user is to be alerted if they make an invalid choice of input

<details><summary>Feedback Error</summary>
<img src="documents/features/features_feedback_error.png">
</details>

### Winner
- The user should be alerted if there is a winner
- User story 6, 7

<details><summary>Winner</summary>
<img src="documents/features/features_winner.png">
</details>

## Validation

### PEP8 Validation
PEP8 online was used to check the code for warnings and errors for the code.
All the code pases with no errors and no warnings.

<details><summary>run.py</summary>
<img src="documents/validation/pep8_validation_run.png">
</details>

<details><summary>players.py</summary>
<img src="documents/validation/pep8_validation_players.png">
</details>

### Testing User Stories

1. As a user, I want to be able to see what numbers correspond to which square

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Board populates | Run Program | The board should pop up and show which numbers will populate to which square of the board | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_1.png">
</details>

2. As a user, I want to be able to choose which square my letter goes into

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| User chooses place | Input an integer between 0-8 | a 'x' or 'o' will appear on the board | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_2.png">
</details>

3. As a user, i want to see my selection appear on the game board

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Board populating | players alternating shots | Board populates with players selections until the game is over | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_3.png">
</details>

4. As a user, I want to have an opponent

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Computer player | User makes a move | The computer should respond with it's own move | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_4.png">
</details>

5. As a user, I want to see who's turn it is next

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Alternating players | One of the players makes a selection | The next player should pop up on the command line to tell them its their shot | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_5.png">
</details>

6. As a user, I want to see the winner

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game winner | Play the game to the end | Either one of the users wins or the game is drawn | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_6.png">
</details>

7. As a site owner, I want the user to select whichever square they want

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game board + User input | Player chooses a square | The chosen square should be populated with the players letter i.e "x" or "o" | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_2.png">
</details>

8. As a site owner, I want the user to get feedback on who won the game

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game winner | The players play the game to the end | Either one of the players wins or the game is drawn | Works as expected |

<details><summary>Snapshot</summary>
<img src="documents/user_stories/user_story_6.png">
<img src="documents/user_stories/user_story_8.png">
</details>

9. As a site owner, I was the user to have fun!

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Enjoyment | Play the game | User has fun | Hopefully the user had lots of fun playing the game :) |


## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| The game would not work due to extra blank spaces in line 14 of run.py | Remove extra blank space |
| The game would not detect a winner of the game | Fix line 98 so it returns an even number (% 2 ==0) |
| Class Players would not allow the functions within to be used in the run.py file | Change the class name to Contestants |
| Game wouldnt print when a player had made a selections | Add an f(string) on line 190 of run.py |

## Deployment

The website was deployed using Heroku by following these steps (taken from Code Institute):
1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be instaled in the file as instructed by Code Institute.
2. Login or create a Heroku account
3. Click the "new" button in the upper right corner and select "create new app"
4. Choose an app name and your region and click "Create app"
5. Go to the "settings" tab, add the python build pack and then the node.js build pack
6. Go to the "deploy" tab and pick GitHub as a deployment method
7. Search for a repository to connect to
8. Click enable automatic deploys and then deploy branch
9. Wait for the app to build and then click on the "View" link

You can fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on the Fork button in the upper right-hand corner

## Future Considerations

I would have liked time to work on this and develop the game further. Some improvements i would make in the future are below:
1. I would have a separate file for the welcome message to tidy the code up. This would also require User Input to confirm they want to play the game.
2. I would create a choice so that the user could decide to play the computer or another person.
3. I would add a loop at the end of the game so the user is offered to play again.

## Credits
- The idea to create this game came from my neice who asked me for a game when i was visiting home.

### Code
- Guidance for creating the app from here - https://www.askpython.com/python/examples/tic-tac-toe-using-python 
- Guidance for creating the app from here - https://youtu.be/8ext9G7xspg?t=2169
- Guidance for using enumerate - https://realpython.com/python-enumerate/
- Further information for Try Except - https://www.w3schools.com/python/python_try_except.asp
- Further information for @staticmethod - https://www.tutorialsteacher.com/python/staticmethod-decorator
- Guidance for printing the ASCII art - https://www.youtube.com/watch?v=arcFqEuV_XQ
- Guidance on the README file structure was taken from my first two Code Institute Project Milestones.

### Media
- ASCII art was taken from - https://ascii.co.uk/art/tictactoe

## Acknowledgements
I would like to take the opportunity to thanks:
- My family and girlfriend for supporting me throughout.
- The incredible Code Institute Tutor staff who are always patient and helpful no matter what.
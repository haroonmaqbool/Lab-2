
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print("Welcome to the Trivia Trek!")
    print("Enjoy the game!")
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    # Add your code here
    #------------------------
    print("Choose a category from the following list:")
    print(categories)
    selected_category = input("Enter the name of the category: ")
    if selected_category in categories:
        return selected_category
    else:
        print("Invalid category. Please try again.")
        return selected_category(categories)
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print(f"Round {round_number} - Your Score: {score}")
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    print("Game over!")
    print(f"Your final score is: {final_score}")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    for i in range(5):
        print(categories)
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return  player_answer == correct_answer
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    # Add your code here
    #------------------------
    if correct:
        return score + 1
    else:
        return score
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    # Add your code here
    #------------------------
    return round_number + 1
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    return incorrect_answers >= 3
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    choice = input("Do you want to play the game again? (yes/no): ")
    if choice.lower() == "yes":
        print("Restarting the game. Please wait....")
    else:
        print("Exiting the game....")
    #------------------------

#---------------------------------------

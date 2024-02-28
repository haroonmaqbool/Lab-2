# main.py
#---------------------------------------
#  Main Application
#    Integration of all components
#---------------------------------------

import game_mechanics
import question_bank
import user_experience

def main():
    # Display welcome message
    game_mechanics.welcome_message()
    
    # Allow the player to choose a difficulty (if applicable)
    difficulty = user_experience.choose_difficulty()
    
    # Initialize game state variables
    categories = list(question_bank.questions.keys())
    score = 0
    incorrect_answers = 0
    round_number = 1
    
    # Main game loop
    while not game_mechanics.check_game_over(incorrect_answers):
        # Player chooses a category
        chosen_category = game_mechanics.choose_category(categories)
        
        # A question is selected randomly from the chosen category
        question, correct_answer = question_bank.select_random_question(chosen_category)
        
        # Display the question and accept the player's answer
        player_answer = question_bank.display_question_and_accept_answer(question)
        
        # Validate the player's answer
        correct = question_bank.check_answer(player_answer, correct_answer)
        
        # Update score and incorrect_answers based on the player's answer
        if correct:
            score = game_mechanics.update_score(score, correct)
        else:
            incorrect_answers += 1
            question_bank.display_correct_answer(correct_answer)
        
        # Display the current score and round information
        game_mechanics.display_score(score, round_number)
        
        # Prepare for the next round
        round_number = game_mechanics.next_round(round_number)
        
        # Optionally, remove the question from the pool to prevent repetition
        question_bank.remove_question(chosen_category, question)
        
        # Check if the game should continue or end based on rounds or incorrect answers
        if game_mechanics.check_game_over(incorrect_answers):
            break
    
    # Display game over message and final score
    game_mechanics.game_over_message(score)
    
    # Save the score
    player_name = input("Enter your name: ")
    user_experience.save_score(player_name, score)
    
    # Display leaderboard
    leaderboard = user_experience.load_top_scores()
    user_experience.display_leaderboard(leaderboard)
    
    # Ask the player if they want to restart or exit
    game_mechanics.restart_or_exit()


#---------------------------------
#  Application Entry Point
main()
#---------------------------------

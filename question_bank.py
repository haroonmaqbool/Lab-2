#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for Potassium?", "K"),
        ("What is the chemical symbol for Calcium?", "Ca")
    ],

    "Maths": [
        ("What is the formula of area of circle?", "pi * r**2"),
        ("What is the formula of area of square?", "L**2"),
        ("What is the formula of Perimeter?", "2*(l+b)")],

    "Computer": [
        ("Best Programming Language?", "Python"),
        ("RAM stands for?", "Random Access Memory"),
        ("ROM stands for?", "Read Only Memory")]
}


hints = {
    "Science": ["Two elements, first one is H", "Symbol is around I", "Starts with C"],
    "Maths": ["Involves radius", "Involves length of one side", "Involves adding all sides"],
    "Computer": ["Known for readability and versatility", "Allows quick access to stored data", "Retains data even when power is off"]

    # Repeat for other categories as needed.
}

#---------------------------------------


def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    #------------------------
    question = random.choice(questions[category])
    return question
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    if player_answer == correct_answer:
        return True
    else:
        return False
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------

    for c1, listQA in questions.items():
        if c1 == category:
            qindex1 = 0
            for tupleQA in listQA:
                Q1, A1 = tupleQA
                if Q1 == question:
                    break
                else:
                    qindex1 = qindex1 + 1

    questions[category].pop(qindex1)


    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    #------------------------
    print("QUESTION:", question)
    answer = input("Enter Your Answer: ")
    return answer
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    for c1, listQA in questions.items():
        if c1 == category:
            qindex1 = 0
            for tupleQA in listQA:
                Q1, A1 = tupleQA
                if Q1 == question:
                    break
                else:
                    qindex1 = qindex1 + 1

    return hints[category][qindex1]
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    print("The correct answer is:", correct_answer)
    #------------------------

#---------------------------------------



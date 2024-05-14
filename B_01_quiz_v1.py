import random

# checks users enter yes (y) or no (n)


def yes_no(question):
    while True:
        response = input(question).lower()

        # check user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions
def instructions():
    print('''

**** Instructions ****
To begin, you choose the number of questions you would like
to be asked. Press <enter> for infinite. 

Then you may either customise the operation, or go with the
default game. (where all operations are included)
Answer the questions, aiming to get as many correct as possible.
If you get one wrong, the computer will show the correct answer.

Good luck!

NOT FINALIZED INSTRUCTIONS

        ''')


# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting game
def int_check(question, low=None, high=None, exit_code=None):

    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number'
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # checks for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            return response

        except ValueError:
            print(error)

# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        response = input(question).lower()
        if response in valid_ans:
            return response
        print(error)


# Generate questions and checks if answer is correct


def generate_question():
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Randomly choose an operation
    operation = random.choice(['+', '-', '*', '/'])

    # Create and solve the question
    if operation == '+':
        correct_answer = num1 + num2
        question = f"What is {num1} + {num2}?"
    elif operation == '-':
        correct_answer = num1 - num2
        question = f"What is {num1} - {num2}?"
    elif operation == '/':
        correct_answer = num1 / num2
        question = f"What is {num1} / {num2}?"
    elif operation == '*':
        correct_answer = num1 * num2
        question = f"What is {num1} * {num2}?"
    elif operation == '/':
        correct_answer = num1 / num2
        question = f"What is {num1} / {num2}?"

    print(question)
    # get user choice
    user_answer = float(input("Your answer: "))
    if user_answer - correct_answer < 0.01:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer:.2f}.")

# Main routine
print()
print("✈️ Basic Math ✈️")
print()

game_history = []
questions_asked = 0
correct_answers = 0

# Does users want to read instructions?
want_instructions = yes_no("Do you want to read the instructions? ").lower()

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


# Ask user for number of rounds / infinite mode
num_questions = int_check("How many questions would you like to be asked? ,"
                          "<enter> for infinite: ",
                          low=1, exit_code="")


# Initialise game variables
mode = "regular"
questions_asked = 0
end_game = "no"
feedback = ""

if num_questions == "":
    mode = "infinite"
    num_questions = 5

# if user are in infinite mode, increase number of rounds!
if mode == "infinite":
    num_questions += 1

# check if the user want to do basic game settings
default_game = yes_no("Do you want to keep the basic game settings?")
if default_game == "yes":
    operation_list = ["+", "-", "*", "/"]
    operation = random.choice(operation_list)

# allow users to customise operation if they wish
else:
    quiz_list = ["multiplication", "m", "division", "d", "subtraction",
                 "s", "addition", "a"]

    user_choice = string_checker("Choose: ", quiz_list)
    print("You chose: ", user_choice)

# if user chose to customise their operation
# only give them one operation
if default_game == "no":
    operation = user_choice

    questions_asked += 1
    if generate_question(operation):
        correct_answers += 1


# Game start here
while questions_asked < num_questions:
    # Rounds heading (base on mode)
    if mode == "infinite":
        game_heading = f"\n✈️✈️Question: {questions_asked + 1} (Infinite mode)✈️✈️"
    else:
        game_heading = f"\n✈️✈️Question: {questions_asked + 1} of {num_questions}✈️✈️"

    print(game_heading)

    # get user choice
    user_answer = float(input("Your answer: "))
    if user_answer - correct_answer < 0.01:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer:.2f}.")
    if questions_asked >= num_questions:
        break

    # check that they don't want to quit
    if user_answer == "xxx":
        # set end_game to use so that outer loop can be
        end_game = "yes"
        break

# How do I continue this game??????????????
print("What do i do next????")

# Game history / statistics area

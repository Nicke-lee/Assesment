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
default quiz. (where a random operation is chosen)
Answer the questions, aiming to get as many correct as possible.
If you get one wrong, the computer will show the correct answer.

Good luck!

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
            else:
                return response

        except ValueError:
            print(error)

# Check that users have entered a valid
# option based on a list


def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        response = input(question).lower()
        if response == "xxx":
            return "exit"
        if response in valid_ans:
            return response
        print(error)


# Generate questions and checks if answer is correct


def generate_question(operation):
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operation == "addition" or operation == "a":
        correct_answer = num1 + num2
        question = f"What is {num1} + {num2}?"
    elif operation == "subtraction" or operation == "s":
        correct_answer = num1 - num2
        question = f"What is {num1} - {num2}?"
    elif operation == "multiplication" or operation == "m":
        correct_answer = num1 * num2
        question = f"what is {num1} x {num2}?"
    elif operation == "division" or operation == "d":
        num1 = num1 * num2
        correct_answer = num1 / num2
        question = f"What is {num1} / {num2}?"
    print(question)

    while True:
        user_input = input("Your answer: ")
        if user_input.lower() == "xxx":
            return "exit", None, None, None
        try:
            user_answer = float(user_input)
            break
        except ValueError:
            print("Please enter a valid number.")

    if abs(user_answer - correct_answer) < 0.01:
        print("Correct!")
        return True, question, user_answer, correct_answer
    else:
        print(f"Wrong! The correct answer is {correct_answer:.2f}.")
        return False, question, user_answer, correct_answer

# Main routine


print()
print("✈️ Basic Math ✈️")
print()

quiz_history = []
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

if num_questions == "":
    mode = "infinite"
    # print("Infinite mode selected")


# check if the user want to do basic game settings
default_quiz = yes_no(f"Do you want a random operation to be chosen for you?")
if default_quiz == "no":
    operation = {
        "m": "multiplication",
        "d": "division",
        "s": "subtraction",
        "a": "addition"
    }

    chosen_operation = string_checker("Choose operation (m, d, s, a): ", operation)
    operation = operation[chosen_operation]
else:
    operation = random.choice(["addition", "subtraction", "multiplication", "division"])

# quiz start here
while mode == "infinite" or questions_asked < num_questions:
    if mode == "infinite":
        game_heading = f"\n✈️✈️ Question: {questions_asked + 1} (Infinite mode) ✈️✈️"
    else:
        game_heading = f"\n✈️✈️ Question: {questions_asked + 1} of {num_questions} ✈️✈️"
    print(game_heading)

    # let the users leave infinite mode
    result, question, user_answer, correct_answer = generate_question(operation)
    if result == "exit":
        break

    if result:
        correct_answers += 1
    questions_asked += 1

    quiz_history.append({
        "Question": question,
        "User Answer": user_answer,
        "Correct Answer": correct_answer,
        "Result": "Correct" if result else "Incorrect"
    })

    if mode != "infinite" and questions_asked >= num_questions:
        break

# Quiz loop ends here
# Game statistics

# check the user have answered at least one question
if questions_asked > 0:

    # Game history / statistics area
    see_history = yes_no("\nDo you want to see the quiz history? (y/n) ")
    if see_history == "yes":
        question_number = 1
        for item in quiz_history:
            print(f"{question_number}: {item['Question']}")
            if item["Result"] == "Correct":
                print("You answered correctly.")
            else:
                print(f"You answered {item['User Answer']}. Correct answer was {item['Correct Answer']:.2f}.")
            question_number += 1

        percent_correct = (correct_answers / questions_asked) * 100
        print("\n🍭🍭🍭 Game Statistics 🍭🍭🍭")
        print(
            f"Total Questions: {questions_asked}, Correct Answers: {correct_answers}, Accuracy: {percent_correct:.2f}%")

        print("Thank you for playing")




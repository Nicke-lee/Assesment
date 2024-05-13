import random


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

    # displays questions
    print(question)

    # get user choice
    user_answer = input("Your answer: ")

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")

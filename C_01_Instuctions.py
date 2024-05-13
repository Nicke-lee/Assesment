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

Answer the questions, aiming to get as many correct as possible.
(if you get one wrong the computer will show the correct answer)

Good luck!

        ''')

# Main routine


print()
print("✈️ Basic Math (not finalised)✈️")
print()

want_instructions = yes_no("Do you want to read the instructions? ").lower()

# check users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

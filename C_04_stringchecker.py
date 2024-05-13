# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=("multiplication", "m", "division",
                                        "d", "subtraction", "s", "addition", "a")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a work in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

            # print error if user does not enter something that is valid
            print(error)
            print()

#  Main routine goes here


quiz_list = ["multiplication", "m", "division", "d", "subtraction",
             "s", "addition", "a"]

user_choice = string_checker("Choose: ", quiz_list)
print("You chose: ", user_choice)

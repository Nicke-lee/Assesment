def string_checker(user_response, valid_ans):
    # Get user response and make sure it's lowercase
    user_response = user_response.lower()

    for item in valid_ans:
        # check if the user response is a word in the list
        if item == user_response:
            return item

        # check if the user response is the same as
        # the first letter of an item in the list
        elif user_response == item[0]:
            return item

    # If no valid response was found, return "invalid"
    return "invalid"

# Automated testing is below in the form (test_case, expected value)

to_test = [
    ("yes", "yes"),
    ("Y", "yes"),
    ("no", "no"),
    ("N", "no"),
    ("YeS", "yes"),
    ("Maybe", "invalid"),
]

# run test!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test string_checker function)
    actual = string_checker(case, ["yes", "no"])

    # compare actual and expected and output pass/fail
    if actual == expected:
        print(f"✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual}✅✅✅")
    else:
        print(f"❌❌❌Failed! Case: {case}, expected: {expected}, received: {actual}❌❌❌")

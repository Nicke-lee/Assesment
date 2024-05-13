# Game history / statistics area

# Calculate Statistics
questions_correct = num_questions - questions_incorrect
percent_won = questions_correct / num_questions * 100
percent_lost = questions_incorrect / num_questions * 100
percent_tied = 100 - percent_won - percent_lost

# Output Game Statistics
print("Game Statistics")
print(f" Won: {percent_won:.2f} \t"
      f" Lost: {percent_lost:.2f} \t"
      f" Tied: {percent_tied:.2f}")

# Display game history if user want to see it
see_history = string_checker("\nDo you want to see the game history? ")
if see_history == "yes":
    print("\n⌛⌛⌛Game History⌛⌛⌛")

    for item in see_history:
        print(item)

    print()
    print("Thanks for playing. ")

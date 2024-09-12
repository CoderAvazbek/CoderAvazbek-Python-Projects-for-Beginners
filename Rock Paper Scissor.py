import random

emojis = {
    "r": '🪨',
    "s": '✂️',
    "p": '📄',
}
choices = ('r', 's', 'p')

user_choice = input("Rock, Paper or Scissors? (r/p/s) ").lower()
if user_choice not in choices:
    print("Invalid choice")
else:
    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif \
        (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "s" and computer_choice == "p") or \
        (user_choice == "p" and computer_choice == "r"):
        print("You win!")
    else:
        print("You lose!")

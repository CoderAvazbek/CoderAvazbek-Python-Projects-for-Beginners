import random

random_number = random.randint(1, 15)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < random_number:
            print("Too High")
        elif guess > random_number:
            print("Too Low")
        else:
            print("Well Done")
            break
    except ValueError:
        print("Please enter a valid number")
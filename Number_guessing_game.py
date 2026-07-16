import random

# int() will throw ValueError if the user types something
# non-numeric — wrap both prompts in one try since either
# failing means we can't proceed either way.
try:
    min_value = int(input("Enter the minimum value for the guessing game: "))
    max_value = int(input("Enter the maximum value for the guessing game: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

# Guard against a backwards or invalid range before it reaches
# random.randint(), which would otherwise throw a confusing error.
if min_value >= max_value:
    print("Minimum value must be less than maximum value. Please try again.")
    exit()

number = random.randint(min_value, max_value)

# None (not 0 or -1) is used so the while condition below is
# guaranteed True on the very first pass, regardless of range.
guess = None
max_attempts = 10

# Resets to 0 once here — this variable's scope is "one full game,"
# so it doesn't need special reset logic inside the loop like
# `results` did in the dice game.
guess_count = 0

# Loop continues only while BOTH conditions hold:
# they haven't won yet, AND they still have attempts left.
# The moment either becomes False, the loop exits.
while guess != number and guess_count < max_attempts:
    try:
        guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
    except ValueError:
        print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")
        # Skip straight back to the while condition — an invalid
        # guess shouldn't count toward guess_count.
        continue

    guess_count += 1  # only reached if the input was valid

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        print(f"It took you {guess_count} guesses.")

# The loop alone can't tell us WHY it stopped — we check that here.
# If they ran out of attempts without a correct final guess,
# reveal the number. If they won, this condition is False
# (guess == number), so nothing extra prints.
if guess_count == max_attempts and guess != number:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
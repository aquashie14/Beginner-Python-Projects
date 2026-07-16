import random

# Declared OUTSIDE the main loop because it needs to persist
# across every round of the game, not reset each time.
roll_count = 0

while True:
    user_input = input("Roll your dice ? (yes/no): ").lower()

    if user_input == "yes":
        num_dice = int(input("How many dice do you want to roll? "))

        # Declared INSIDE the loop, right before use, so it starts
        # fresh every round. If this were outside the while loop,
        # old rolls from previous rounds would never clear out.
        results = []

        for i in range(num_dice):
            # Counts individual dice, not rounds — deliberate choice.
            # If we wanted to count rounds instead, this would sit
            # after the for loop, not inside it.
            roll_count += 1
            roll = random.randint(1, 6)
            results.append(roll)

        print(results)

    elif user_input == "no":
        print("Okay, maybe next time!")
        print(f"You rolled the dice {roll_count} times.")
        break  # only way out of the infinite while loop

    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
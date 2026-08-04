import random  # We use a tool to generate a random number

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} tries to get it right.")

    while attempts < max_attempts:
        # Get input from the user (and convert it to a number)
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        # Check the logic (If-Else)
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} tries!")
            return # Exit the game because they won

    print(f"Game Over! The number was {secret_number}.")

# Run the game
start_game()
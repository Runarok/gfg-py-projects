import random  # Used for shuffling digits and selecting random guesses

# Validates that the input is a 4-digit number with all unique digits
def is_valid_code(code):
    return code.isdigit() and len(code) == 4 and len(set(code)) == 4

# Compares secret and guess to compute number of bulls and cows
# Bulls = correct digit at correct position
# Cows = correct digit at wrong position
def get_bulls_cows(secret, guess):
    bulls = sum(secret[i] == guess[i] for i in range(4))
    cows = sum(1 for d in guess if d in secret) - bulls
    return bulls, cows

# Generates a random 4-digit code with unique digits
def generate_random_code():
    digits = list("0123456789")
    random.shuffle(digits)  # Shuffle digits randomly
    return ''.join(digits[:4])  # Pick first 4 unique digits

# Allows user to choose difficulty and sets max attempts accordingly
def get_attempt_limit():
    print("\nChoose difficulty:")
    print("1. Easy (10 attempts)")
    print("2. Normal (7 attempts)")
    print("3. Hard (5 attempts)")
    print("4. Custom")

    while True:
        choice = input("Select (1–4): ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 7
        elif choice == '3':
            return 5
        elif choice == '4':
            try:
                limit = int(input("Enter number of attempts (0 for unlimited): "))
                return limit if limit >= 0 else 0  # Ensure it's non-negative
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid choice.")

# Human player guesses the AI-generated or player-provided secret code
def human_guesses(secret):
    attempts = 0
    max_attempts = get_attempt_limit()  # Set limit based on difficulty

    while True:
        guess = input("Enter your 4-digit guess: ")
        if not is_valid_code(guess):
            print("Invalid input. Must be 4 unique digits.")
            continue

        attempts += 1
        bulls, cows = get_bulls_cows(secret, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print(f"You cracked the code in {attempts} tries!")
            break

        # Check if the user has exhausted all attempts
        if max_attempts and attempts >= max_attempts:
            print(f"\nOut of attempts! The code was: {secret}")
            break

# AI tries to guess the user-provided code using automatic feedback
def ai_guesses_with_known_code(secret):
    # Generate all possible 4-digit codes with unique digits
    def all_possibilities():
        lst = []
        for a in '0123456789':
            for b in '0123456789':
                for c in '0123456789':
                    for d in '0123456789':
                        guess = a + b + c + d
                        if len(set(guess)) == 4:
                            lst.append(guess)
        return lst

    possibilities = all_possibilities()
    attempts = 0

    while possibilities:
        guess = random.choice(possibilities)
        attempts += 1
        bulls, cows = get_bulls_cows(secret, guess)
        print(f"AI guess #{attempts}: {guess} → Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            print(f"\nAI cracked the code '{secret}' in {attempts} tries.")
            break

        # Narrow down the possibilities based on feedback
        possibilities = [p for p in possibilities if get_bulls_cows(p, guess) == (bulls, cows)]

# AI guesses user's code, and user manually inputs bulls and cows after each guess
def ai_guesses_with_manual_feedback():
    def all_possibilities():
        lst = []
        for a in '0123456789':
            for b in '0123456789':
                for c in '0123456789':
                    for d in '0123456789':
                        guess = a + b + c + d
                        if len(set(guess)) == 4:
                            lst.append(guess)
        return lst

    possibilities = all_possibilities()
    attempts = 0

    while possibilities:
        guess = random.choice(possibilities)
        attempts += 1
        print(f"\nAI guess #{attempts}: {guess}")

        # Ask the user for feedback manually
        while True:
            try:
                bulls = int(input("Enter number of Bulls: "))
                cows = int(input("Enter number of Cows: "))
                if 0 <= bulls <= 4 and 0 <= cows <= 4 and bulls + cows <= 4:
                    break
                else:
                    print("Invalid input. Total must not exceed 4, and each between 0–4.")
            except ValueError:
                print("Please enter valid numbers.")

        if bulls == 4:
            print(f"\nAI cracked your secret code '{guess}' in {attempts} tries.")
            break

        # Filter all valid guesses based on the user's feedback
        new_poss = []
        for p in possibilities:
            b, c = get_bulls_cows(p, guess)
            if b == bulls and c == cows:
                new_poss.append(p)
        possibilities = new_poss

# Two human players play: one sets the code, the other guesses
def mode_player_vs_player():
    code = input("Player 1, enter a 4-digit secret code (will be hidden): ")
    while not is_valid_code(code):
        print("Invalid code. Must be 4 unique digits.")
        code = input("Enter again: ")
    
    # Simulate screen clearing so Player 2 doesn't see the code
    for _ in range(50):
        print()
    
    print("Player 2, start guessing!")
    human_guesses(code)

# Human vs AI: Human tries to guess AI's code
def mode_player_vs_ai():
    code = generate_random_code()
    print("AI has chosen a 4-digit secret code.")
    human_guesses(code)

# AI tries to guess a code: either known or kept secret by player
def mode_ai_vs_player():
    print("\nChoose input mode:")
    print("1. Enter the full code once (AI gets auto feedback)")
    print("2. Keep the code secret (you give feedback each turn)")
    choice = input("Choice (1 or 2): ")

    if choice == '1':
        code = input("Enter your 4-digit code for AI to guess: ")
        while not is_valid_code(code):
            print("Invalid code. Must be 4 unique digits.")
            code = input("Enter again: ")
        ai_guesses_with_known_code(code)
    elif choice == '2':
        print("Keep your code in mind. You'll give Bulls and Cows after each AI guess.")
        ai_guesses_with_manual_feedback()
    else:
        print("Invalid choice.")

# Main game loop where user chooses game mode
def main():
    while True:
        print("\n=== COWS AND BULLS ===")
        print("1. Player vs Player")
        print("2. You guess AI's secret")
        print("3. AI guesses your secret")
        print("4. Exit")
        mode = input("Choose a mode (1–4): ")

        if mode == '1':
            mode_player_vs_player()
        elif mode == '2':
            mode_player_vs_ai()
        elif mode == '3':
            mode_ai_vs_player()
        elif mode == '4':
            print("Exiting. Thanks for playing!")
            break
        else:
            print("Invalid choice.")

# Entry point for running the game
main()

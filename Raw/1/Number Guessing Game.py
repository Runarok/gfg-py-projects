import random

# Game Difficulty Levels
DIFFICULTY_LEVELS = {
    "Easy": (1, 10),
    "Medium": (1, 50),
    "Hard": (1, 100),
    "Extreme": (1, 1000),
}

# Proximity Clues
PROXIMITY_CLUES = {
    "🔥": 3,
    "Warm": 10,
    "❄️": 20,
}

# Motivational Messages
MOTIVATIONAL_MESSAGES = [
    "Don't worry, you'll get it next time!",
    "Practice makes perfect. Keep trying!",
    "Failure is the first step to success.",
    "Every mistake is a learning opportunity.",
    "You're doing great, keep up the good work!",
]

class NumberGuessingGame:
    def __init__(self):
        self.player_profile = PlayerProfile()
        self.game_engine = GameEngine()

    def start_game(self):
        self.display_title_screen()
        self.game_engine.start_game(self.player_profile)

    def display_title_screen(self):
        print("=== Welcome to the Number Guessing Game! ===")
        print("Guess the random number to win!")
        print("Your progress will be saved across sessions.")
        print()

    def display_difficulty_menu(self):
        print("Choose a difficulty level:")
        all_choices = list(DIFFICULTY_LEVELS.keys()) + ["Custom"]
        for i, difficulty in enumerate(all_choices, 1):
            if difficulty != "Custom":
                min_num, max_num = DIFFICULTY_LEVELS[difficulty]
                print(f"{i}. {difficulty} ({min_num}-{max_num})")
            else:
                print(f"{i}. Custom: Choose your own range and number of attempts")
        print()

        return self.get_user_input("Enter your choice (name or number): ", all_choices)

    def get_user_input(self, prompt, valid_inputs=None):
        while True:
            user_input = input(prompt).strip()
            if valid_inputs is None:
                return user_input

            # Handle numbered input
            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(valid_inputs):
                    return valid_inputs[index]

            # Handle case-insensitive text match
            lower_valid = {v.lower(): v for v in valid_inputs}
            if user_input.lower() in lower_valid:
                return lower_valid[user_input.lower()]

            print("Invalid input. Please try again.")

class GameEngine:
    def start_game(self, player_profile):
        difficulty = self.display_difficulty_menu()
        if difficulty == "Custom":
            min_num, max_num, attempts = self.get_custom_difficulty()
        else:
            min_num, max_num = DIFFICULTY_LEVELS[difficulty]
            attempts = self.get_attempts_for_difficulty(difficulty, player_profile)

        self.play_game(min_num, max_num, attempts, player_profile)

    def display_difficulty_menu(self):
        return game.display_difficulty_menu()

    def get_custom_difficulty(self):
        min_num = int(self.get_user_input("Enter the minimum number: "))
        max_num = int(self.get_user_input("Enter the maximum number: "))
        attempts = int(self.get_user_input("Enter the number of attempts: "))
        return min_num, max_num, attempts

    def get_attempts_for_difficulty(self, difficulty, player_profile):
        base_attempts = {
            "Easy": 7,
            "Medium": 10,
            "Hard": 15,
            "Extreme": 20,
        }[difficulty]
        return base_attempts + player_profile.get_extra_attempts()

    def get_user_input(self, prompt):
        return game.get_user_input(prompt)

    def play_game(self, min_num, max_num, attempts, player_profile):
        target_number = random.randint(min_num, max_num)
        print(f"\nGuess the number between {min_num} and {max_num}.\n")

        guess_count = 0

        while attempts > 0:
            guess = self.get_user_guess(min_num, max_num)
            guess_count += 1

            if guess == target_number:
                self.handle_win(player_profile, guess_count)
                return

            self.provide_feedback(guess, target_number, attempts)
            attempts -= 1
            print(f"Attempts remaining: {attempts}\n")

        self.handle_loss(target_number, guess_count)

    def get_user_guess(self, min_num, max_num):
        while True:
            try:
                guess = int(self.get_user_input(f"Enter your guess ({min_num}-{max_num}): "))
                if min_num <= guess <= max_num:
                    return guess
                print("Invalid guess. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def provide_feedback(self, guess, target_number, attempts):
        difference = abs(guess - target_number)
        if difference < PROXIMITY_CLUES["🔥"]:
            print("🔥 Very close!")
        elif difference < PROXIMITY_CLUES["Warm"]:
            print("Warm")
        elif difference < PROXIMITY_CLUES["❄️"]:
            print("❄️ Cold")
        else:
            if guess < target_number:
                print("Too low")
            else:
                print("Too high")

        if attempts >= 3 and difference > 10:
            self.provide_statistical_hint(target_number)

    def provide_statistical_hint(self, target_number):
        if target_number % 2 == 0:
            print("Hint: The number is divisible by 2.")
        elif target_number % 3 == 0:
            print("Hint: The number is divisible by 3.")
        else:
            print("Hint: The number is between 1 and 100.")

    def handle_win(self, player_profile, guess_count):
        win_message = self.get_win_message(guess_count)
        print("\n" + win_message)
        player_profile.update_win(guess_count)

    def get_win_message(self, guess_count):
        if guess_count == 1:
            return "Genius! You guessed it in 1 try!"
        elif guess_count <= 3:
            return f"Excellent! You guessed it in {guess_count} tries."
        else:
            return f"You got it! That took some effort, but you did it in {guess_count} tries."

    def handle_loss(self, target_number, guess_count):
        print(f"Sorry, the number was {target_number}.")
        print(f"You made {guess_count} guesses.")
        print(random.choice(MOTIVATIONAL_MESSAGES))

class PlayerProfile:
    def __init__(self):
        self.total_games = 0
        self.wins = 0
        self.best_streak = 0
        self.current_streak = 0
        self.extra_attempts = 0

    def update_win(self, guess_count):
        self.total_games += 1
        self.wins += 1
        self.current_streak += 1
        if self.current_streak > self.best_streak:
            self.best_streak = self.current_streak
        if self.current_streak % 3 == 0:
            self.extra_attempts += 1
            print(f"You've earned an extra attempt! You now have {self.extra_attempts} extra attempts.")

    def get_extra_attempts(self):
        return self.extra_attempts

# Run the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()

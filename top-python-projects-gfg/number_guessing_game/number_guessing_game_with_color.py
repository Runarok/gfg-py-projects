import random
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama

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
        print(Fore.YELLOW + "=== Welcome to the Number Guessing Game! ===" + Style.RESET_ALL)
        print("Guess the random number to win!")
        print("Your progress will be saved across sessions.")
        print()

    def display_difficulty_menu(self):
        print(Fore.CYAN + "Choose a difficulty level:" + Style.RESET_ALL)
        all_choices = list(DIFFICULTY_LEVELS.keys()) + ["Custom"]
        for i, difficulty in enumerate(all_choices, 1):
            if difficulty != "Custom":
                min_num, max_num = DIFFICULTY_LEVELS[difficulty]
                print(f"{Fore.CYAN}{i}. {difficulty} ({min_num}-{max_num}){Style.RESET_ALL}")
            else:
                print(f"{Fore.CYAN}{i}. Custom: Choose your own range and number of attempts{Style.RESET_ALL}")
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

            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

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
        print(f"\nGuess the number between {Fore.MAGENTA}{min_num}{Style.RESET_ALL} and {Fore.MAGENTA}{max_num}{Style.RESET_ALL}.\n")

        guess_count = 0

        while attempts > 0:
            guess = self.get_user_guess(min_num, max_num)
            guess_count += 1

            if guess == target_number:
                self.handle_win(player_profile, guess_count)
                return

            self.provide_feedback(guess, target_number, attempts)
            attempts -= 1
            print(f"Attempts remaining: {Fore.YELLOW}{attempts}{Style.RESET_ALL}\n")

        self.handle_loss(target_number, guess_count)

    def get_user_guess(self, min_num, max_num):
        while True:
            try:
                guess = int(self.get_user_input(f"Enter your guess ({min_num}-{max_num}): "))
                if min_num <= guess <= max_num:
                    return guess
                print(Fore.RED + "Invalid guess. Please try again." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

    def provide_feedback(self, guess, target_number, attempts):
        difference = abs(guess - target_number)
        if difference < PROXIMITY_CLUES["🔥"]:
            print(Fore.RED + "🔥 Very close!" + Style.RESET_ALL)
        elif difference < PROXIMITY_CLUES["Warm"]:
            print(Fore.YELLOW + "Warm" + Style.RESET_ALL)
        elif difference < PROXIMITY_CLUES["❄️"]:
            print(Fore.BLUE + "❄️ Cold" + Style.RESET_ALL)
        else:
            if guess < target_number:
                print(Fore.GREEN + "Too low" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "Too high" + Style.RESET_ALL)

        if attempts >= 3 and difference > 10:
            self.provide_statistical_hint(target_number)

    def provide_statistical_hint(self, target_number):
        if target_number % 2 == 0:
            print(Fore.CYAN + "Hint: The number is divisible by 2." + Style.RESET_ALL)
        elif target_number % 3 == 0:
            print(Fore.CYAN + "Hint: The number is divisible by 3." + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Hint: The number is between 1 and 100." + Style.RESET_ALL)

    def handle_win(self, player_profile, guess_count):
        win_message = self.get_win_message(guess_count)
        print("\n" + Fore.GREEN + win_message + Style.RESET_ALL)
        player_profile.update_win(guess_count)

    def get_win_message(self, guess_count):
        if guess_count == 1:
            return "Genius! You guessed it in 1 try!"
        elif guess_count <= 3:
            return f"Excellent! You guessed it in {guess_count} tries."
        else:
            return f"You got it! That took some effort, but you did it in {guess_count} tries."

    def handle_loss(self, target_number, guess_count):
        print(Fore.RED + f"Sorry, the number was {target_number}." + Style.RESET_ALL)
        print(f"You made {guess_count} guesses.")
        print(Fore.MAGENTA + random.choice(MOTIVATIONAL_MESSAGES) + Style.RESET_ALL)

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
            print(Fore.CYAN + f"You've earned an extra attempt! You now have {self.extra_attempts} extra attempts." + Style.RESET_ALL)

    def get_extra_attempts(self):
        return self.extra_attempts

# Run the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.start_game()

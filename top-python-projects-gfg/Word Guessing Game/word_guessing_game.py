import random
import time

# -------------------------------
# Word Bank with Categories
# -------------------------------
WORD_CATEGORIES = {
    "Animals": [
        "tiger", "elephant", "giraffe", "kangaroo", "zebra", "lion", "cheetah", "panda", "ostrich", "rhinoceros",
        "whale", "octopus", "squid", "penguin", "hippopotamus"
    ],
    "Technology": [
        "python", "laptop", "server", "keyboard", "monitor", "network", "compiler", "database", "robotics", "sensor",
        "terminal", "firmware", "bluetooth", "algorithm", "protocol"
    ],
    "Nature": [
        "volcano", "tsunami", "rainfall", "earthquake", "avalanche", "hurricane", "sunshine", "glacier", "tornado", "island"
    ],
    "Countries": [
        "brazil", "germany", "nigeria", "canada", "japan", "france", "australia", "iceland", "nepal", "thailand",
        "singapore", "sweden", "switzerland", "argentina", "colombia"
    ],
    "Food": [
        "pizza", "burger", "lasagna", "noodles", "sandwich", "pancake", "biryani", "dumpling", "samosa", "taco",
        "croissant", "curry", "steak", "noodle", "mango"
    ]
}

# -------------------------------
# Stats (Session Based)
# -------------------------------
session_stats = {
    "games_played": 0,
    "games_won": 0,
    "games_lost": 0,
    "total_time": 0
}

# -------------------------------
# UI Helpers
# -------------------------------
def print_banner(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

def display_progress(word, guessed_letters):
    display = [ch if ch in guessed_letters else "_" for ch in word]
    print("Word: " + " ".join(display))

def get_valid_guess(used_letters):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1:
            print("⚠️  Enter only one character.")
        elif not guess.isalpha():
            print("⚠️  Only letters are allowed.")
        elif guess in used_letters:
            print("⚠️  You've already guessed that.")
        else:
            return guess

# -------------------------------
# Word Selection Logic
# -------------------------------
def get_random_word(min_len, max_len):
    eligible = []
    for category, words in WORD_CATEGORIES.items():
        for word in words:
            if min_len <= len(word) <= max_len:
                eligible.append((word, category))
    return random.choice(eligible) if eligible else ("", "")

# -------------------------------
# Difficulty Setup
# -------------------------------
def choose_difficulty():
    print("\nSelect Difficulty:")
    print("1. Easy (3–6 letters, 10 attempts)")
    print("2. Medium (6–8 letters, 7 attempts)")
    print("3. Hard (8+ letters, 5 attempts)")
    print("4. Custom")

    while True:
        choice = input("Your choice: ").strip()
        if choice == "1":
            return 3, 6, 10
        elif choice == "2":
            return 6, 8, 7
        elif choice == "3":
            return 8, 20, 5
        elif choice == "4":
            return get_custom_difficulty()
        else:
            print("⚠️  Invalid input. Try again.")

def get_custom_difficulty():
    while True:
        try:
            min_len = int(input("Minimum word length (e.g., 4): ").strip())
            max_len = int(input("Maximum word length (e.g., 10): ").strip())
            attempts = int(input("Number of attempts (e.g., 8): ").strip())
            if min_len < 1 or max_len < min_len or attempts < 1:
                print("⚠️  Invalid values. Try again.")
                continue
            return min_len, max_len, attempts
        except ValueError:
            print("⚠️  Enter numeric values only.")

# -------------------------------
# Game Round Logic
# -------------------------------
def play_round(min_len, max_len, max_attempts):
    word, category = get_random_word(min_len, max_len)
    if not word:
        print("⚠️  No words found for selected settings.")
        return

    guessed_letters = set()
    incorrect_letters = set()
    remaining = max_attempts
    start_time = time.time()

    print_banner("🕹️ Game Started!")
    print(f"Category Hint: {category}")
    print(f"The word has {len(word)} letters.")

    while remaining > 0:
        display_progress(word, guessed_letters)
        print(f"Used: {' '.join(sorted(guessed_letters | incorrect_letters))}")
        print(f"Remaining Attempts: {remaining}")
        guess = get_valid_guess(guessed_letters | incorrect_letters)

        if guess in word:
            guessed_letters.add(guess)
            print("✅ Correct!")
        else:
            incorrect_letters.add(guess)
            remaining -= 1
            print("❌ Wrong guess.")

        if all(char in guessed_letters for char in word):
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            print_banner("🎉 YOU WON!")
            display_progress(word, guessed_letters)
            print(f"The word was: {word}")
            print(f"Time taken: {duration}s")
            session_stats["games_won"] += 1
            session_stats["total_time"] += duration
            session_stats["games_played"] += 1
            return

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print_banner("💀 YOU LOST!")
    print(f"The word was: {word}")
    print(f"Time taken: {duration}s")
    session_stats["games_lost"] += 1
    session_stats["total_time"] += duration
    session_stats["games_played"] += 1

# -------------------------------
# Summary
# -------------------------------
def show_session_summary():
    print_banner("📊 SESSION SUMMARY")
    print(f"Games Played: {session_stats['games_played']}")
    print(f"Games Won:    {session_stats['games_won']}")
    print(f"Games Lost:   {session_stats['games_lost']}")
    if session_stats['games_played'] > 0:
        avg_time = session_stats['total_time'] / session_stats['games_played']
        print(f"Avg Time:     {round(avg_time, 2)} seconds")

# -------------------------------
# Main Game Loop
# -------------------------------
def main():
    print_banner("WORD GUESSING GAME")
    while True:
        min_len, max_len, attempts = choose_difficulty()
        play_round(min_len, max_len, attempts)

        again = input("\nPlay another game? (y/n): ").strip().lower()
        if again != 'y':
            break

    show_session_summary()
    print("\nThanks for playing!")

# Run the game
main()

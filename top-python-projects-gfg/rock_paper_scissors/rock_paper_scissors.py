import random

# Constants
CHOICES = {
    '1': 'Rock', 'rock': 'Rock',
    '2': 'Paper', 'paper': 'Paper',
    '3': 'Scissors', 'scissors': 'Scissors',
    '5': 'menu'
}

WIN_RULES = {
    'Rock': 'Scissors',
    'Scissors': 'Paper',
    'Paper': 'Rock'
}

LOSES_TO = {v: k for k, v in WIN_RULES.items()}

CELEBRATIONS = [
    "🔥 You're on fire!",
    "🎯 Perfect shot!",
    "👏 Nice move!",
    "💥 Boom! Nailed it.",
    "⚡ That's a clean win!"
]

AI_DIFFICULTY = {
    '1': 'easy',
    '2': 'hard',
    '3': 'impossible'
}


def print_rules():
    print("\n📜 WINNING RULES:")
    for winner, loser in WIN_RULES.items():
        print(f"🔹 {winner} beats {loser}")
    print()


def get_valid_choice(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return options[user_input]
        print("❌ Invalid input. Try again.")


def select_game_mode():
    print("\n🎮 Select Game Mode:")
    print("1 - Best of 3")
    print("2 - Best of 5")
    print("3 - Free Play (infinite rounds)")
    return get_valid_choice("Choose mode (1/2/3): ", {
        '1': ('best_of', 3),
        '2': ('best_of', 5),
        '3': ('infinite', None)
    })


def select_difficulty():
    print("\n🧠 Select AI Difficulty:")
    print("1 - Easy (random)")
    print("2 - Hard (learns from your last move)")
    print("3 - Impossible (always counters your move)")
    return get_valid_choice("Choose difficulty (1/2/3): ", AI_DIFFICULTY)


def get_user_choice():
    print("\nYour move: [1] Rock  [2] Paper  [3] Scissors  [5] Menu")
    while True:
        choice = input("Type your choice: ").strip().lower()
        if choice in CHOICES:
            return CHOICES[choice]
        print("❌ Invalid choice. Please enter Rock/Paper/Scissors or 1/2/3 (or 5 for menu).")


def get_computer_choice_easy():
    return random.choice(list(WIN_RULES.keys()))


def get_computer_choice_hard(last_user_move):
    if last_user_move:
        return LOSES_TO[last_user_move]
    return get_computer_choice_easy()


def get_computer_choice_impossible(user_move):
    return LOSES_TO[user_move]


def get_computer_choice(ai_level, user_move=None, last_user_move=None):
    if ai_level == 'easy':
        return get_computer_choice_easy()
    elif ai_level == 'hard':
        return get_computer_choice_hard(last_user_move)
    elif ai_level == 'impossible':
        return get_computer_choice_impossible(user_move)


def decide_winner(user, computer):
    if user == computer:
        return 'Draw'
    elif WIN_RULES[user] == computer:
        return 'User'
    else:
        return 'Computer'


def print_score(score):
    total = score['User'] + score['Computer'] + score['Draw']
    win_ratio = (score['User'] / total * 100) if total else 0
    print("\n📊 SCOREBOARD:")
    print(f"✅ User Wins     : {score['User']}")
    print(f"🤖 Computer Wins : {score['Computer']}")
    print(f"🤝 Draws         : {score['Draw']}")
    print(f"📈 Win Ratio     : {win_ratio:.2f}%\n")


def game_menu(score, current_ai, current_mode, target_wins):
    print("\n📋 PAUSE MENU")
    print("1 - Change AI Difficulty")
    print("2 - Change Game Mode")
    print("3 - Reset Score")
    print("4 - Exit Game")
    print("5 - Continue")

    while True:
        choice = input("Select an option (1-5): ").strip()
        if choice == '1':
            current_ai = select_difficulty()
            print(f"✅ AI difficulty set to: {current_ai.capitalize()}")
        elif choice == '2':
            current_mode, target_wins = select_game_mode()
            print(f"✅ Game mode changed.")
        elif choice == '3':
            score.update({'User': 0, 'Computer': 0, 'Draw': 0})
            print("🔄 Score reset.")
        elif choice == '4':
            print("👋 Exiting game. Thanks for playing!")
            exit()
        elif choice == '5':
            return current_ai, current_mode, target_wins
        else:
            print("❌ Invalid option. Try again.")


def play_game():
    print("👋 Welcome to Rock-Paper-Scissors!")
    print_rules()

    score = {'User': 0, 'Computer': 0, 'Draw': 0}
    last_user_move = None
    round_number = 0

    # Initial selections
    current_mode, target_wins = select_game_mode()
    current_ai = select_difficulty()

    print("\n🕹 Tip: Type 5 at any time to open the menu (change difficulty, reset, or quit)")

    while True:
        round_number += 1
        print(f"\n🔄 ROUND {round_number}")

        user_choice = get_user_choice()
        if user_choice == 'menu':
            current_ai, current_mode, target_wins = game_menu(score, current_ai, current_mode, target_wins)
            continue

        comp_choice = get_computer_choice(current_ai, user_choice, last_user_move)
        print(f"🧑 You:      {user_choice}")
        print(f"🤖 Computer: {comp_choice}")

        result = decide_winner(user_choice, comp_choice)
        score[result] += 1

        if result == 'Draw':
            print("🤝 It's a draw.")
        elif result == 'User':
            print(f"✅ You win! {random.choice(CELEBRATIONS)}")
        else:
            print("❌ Computer wins this round.")

        print_score(score)
        last_user_move = user_choice

        # Best-of mode ending logic
        if current_mode == 'best_of':
            if score['User'] > target_wins // 2:
                print("🏆 You won the match!")
                break
            elif score['Computer'] > target_wins // 2:
                print("😞 Computer won the match.")
                break

        # Infinite continues without auto-break
        if current_mode == 'infinite':
            pass  # Player uses menu (5) to quit/reset/change

    print("\n🏁 Final Results:")
    print_score(score)
    print("Thanks for playing! 👋")


if __name__ == "__main__":
    play_game()

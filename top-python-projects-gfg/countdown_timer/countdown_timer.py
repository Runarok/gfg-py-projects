import time

# ----- Utility Functions -----
def format_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def parse_time(user_input):
    try:
        if ":" in user_input:
            parts = list(map(int, user_input.strip().split(":")))
            while len(parts) < 3:
                parts.insert(0, 0)
            h, m, s = parts
            return h * 3600 + m * 60 + s
        else:
            return int(user_input)
    except:
        return -1

def countdown(duration, label=""):
    print(f"\n▶️  Starting '{label or 'Unnamed Session'}' — Duration: {format_time(duration)}")
    for remaining in range(duration, 0, -1):
        print(f"\r⏳ {format_time(remaining)}", end="")
        time.sleep(1)
    print("\r⏰ Time's up!          ")
    post_timer_message()

def post_timer_message():
    messages = [
        "💡 Break the problem, not yourself.",
        "🏁 One step closer to your goal.",
        "🔥 Good session. Stay consistent.",
        "🌱 Progress, not perfection.",
        "🎯 Sharp focus beats long hours."
    ]
    print("\n" + messages[int(time.time()) % len(messages)])

# ----- Preset Modes -----
PRESETS = {
    "1": ("Pomodoro", 25 * 60),
    "2": ("Short Break", 5 * 60),
    "3": ("Long Break", 15 * 60),
    "4": ("Focus Session", 50 * 60)
}

# ----- Timer System -----
def main():
    session_stats = {
        "total_sessions": 0,
        "total_time": 0,
        "longest_session": 0
    }

    last_custom = 0
    loop_mode = False

    while True:
        print("\n⏲️  Countdown Timer Menu:")
        for key, (name, duration) in PRESETS.items():
            print(f"{key}. {name} ({format_time(duration)})")
        print("5. Custom Time")
        print("6. Toggle Loop Mode (Currently: " + ("ON 🔁" if loop_mode else "OFF") + ")")
        print("7. Show Stats")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice in PRESETS:
            label, duration = PRESETS[choice]
        elif choice == "5":
            custom_input = input("Enter time (seconds or HH:MM:SS): ").strip()
            duration = parse_time(custom_input)
            if duration <= 0:
                print("❌ Invalid time. Try again.")
                continue
            label = input("Label this session (optional): ").strip() or "Custom Session"
            last_custom = duration
        elif choice == "6":
            loop_mode = not loop_mode
            continue
        elif choice == "7":
            show_stats(session_stats)
            continue
        elif choice == "8":
            print("👋 Goodbye. Stay focused.")
            break
        else:
            print("❌ Invalid choice.")
            continue

        # Run session
        while True:
            countdown(duration, label)
            session_stats["total_sessions"] += 1
            session_stats["total_time"] += duration
            session_stats["longest_session"] = max(session_stats["longest_session"], duration)

            if not loop_mode:
                break

            print("\n🔁 Looping session again. Press Ctrl+C anytime to quit loop.")
            time.sleep(1)

def show_stats(stats):
    print("\n📊 Session Stats:")
    print(f"✔️  Total Sessions: {stats['total_sessions']}")
    print(f"⏱️  Total Time     : {format_time(stats['total_time'])}")
    print(f"🏆 Longest Session : {format_time(stats['longest_session'])}")

# ----- Entry Point -----
if __name__ == "__main__":
    main()

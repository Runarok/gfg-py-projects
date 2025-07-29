# Number Guessing Game - Improved Version

This is my enhanced take on the classic **Number Guessing Game** in Python, originally inspired by [this GeeksforGeeks tutorial](https://www.geeksforgeeks.org/python/number-guessing-game-in-python/).

---

## Overview

This project is a modular, user-friendly number guessing game with several improvements over the basic version, including:

- **Multiple difficulty levels** with predefined ranges (Easy, Medium, Hard, Extreme) and a customizable mode
- **Dynamic attempts count** that can increase as you win more games consecutively (extra attempts awarded every 3 wins)
- **Helpful proximity clues** using intuitive emojis and colored feedback (`🔥 Very close!`, `Warm`, `❄️ Cold`, etc.)
- **Motivational messages** to encourage the player after losses
- **Robust input handling** supporting case-insensitive difficulty selection, and numeric or textual input (e.g., "1" or "easy")
- **Statistical hints** when the player is far off, giving extra clues (divisible by 2, 3, or range hints)
- **Progress tracking** with win counts and streaks
- Modular code architecture with clear separation of game engine, player profile, and interface

---

## Code Files

* 🔸 **[`number_guessing_game_with_color.py`](./number_guessing_game_with_color.py)** — The main game script with color output using `colorama` for a more engaging terminal experience.
* 🔹 **[`number_guessing_game_no_color.py`](./number_guessing_game_no_color.py)** — A plain version of the game without color — ideal for basic terminal environments or systems without color support.



Both scripts contain the same game logic and modular design but differ only in their use of colored output.

---

## How to Use

Simply run either script in your Python environment. The game will guide you through:

1. **Choosing a difficulty level** (by name or number, case-insensitive)
2. **Guessing the target number** within a limited number of attempts
3. **Receiving feedback and hints** after each guess
4. **Tracking your wins and streaks** across sessions (in-memory per run)

The modular design lets you easily extend or integrate components, such as:

- Adding new difficulty levels or changing ranges
- Modifying motivational messages or clues
- Adjusting attempt counts or win conditions

---

## Inspiration & Original Idea

This project is a substantial update and improvement over the classic version found here:

[Python Number Guessing Game - GeeksforGeeks](https://www.geeksforgeeks.org/python/number-guessing-game-in-python/)

I built upon the original by making the game more interactive, user-friendly, and visually engaging with colored feedback and a richer set of features.

---

Enjoy the game, and happy guessing!

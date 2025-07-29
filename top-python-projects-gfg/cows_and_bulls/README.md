# 🐮🐂 Cows and Bulls — Multi-Mode Python Game

A modern, feature-rich version of the classic **Cows and Bulls** game.
Includes single-player, AI-vs-you, and hidden-input human-vs-human modes — built to run standalone on any Python 3+ environment.

---

## 🧩 Overview

This is a number-based code-breaking game where the player tries to guess a **4-digit secret number**. Each digit must be unique. After every guess, the game provides feedback:

* **🐂 Bull** → Correct digit, correct position
* **🐮 Cow** → Correct digit, wrong position

The game ends when the player correctly guesses all 4 digits in the correct order (4 Bulls).

---

## 🎮 How to Play

1. A **4-digit number** is chosen (either by AI or a player).
2. The guesser attempts to find this number.
3. After each guess:

   * Bulls = correct digit in the correct position
   * Cows = correct digit in the wrong position
4. The process repeats until 4 Bulls are achieved.

**Example:**
Secret = `1234`, Guess = `1246` → `2 Bulls` (`1`, `2`), `1 Cow` (`4`)

---

## 🧠 Modes Available

* **👥 Human vs Human**
  One player sets the secret code, screen is cleared, and the other player guesses.

* **🤖 You vs AI**
  AI generates a random 4-digit code, and you try to crack it.

* **🧠 AI vs You**
  You set a code, and AI auto-guesses using deduction from previous attempts.

---

## 📂 Code Files

🔸 **[`cows_and_bulls.py`](./cows_and_bulls.py)**
Standalone full game with all modes included. Compatible with browser-based Python compilers.

> ⚙️ Requires only Python 3+. No external libraries.

---

## 🚀 How to Use the Code

1. Open any Python 3-compatible compiler (e.g. [Replit](https://replit.com/), [GFG IDE](https://www.geeksforgeeks.org/python-compiler/)).
2. Paste the contents of `cows_and_bulls.py`.
3. Run the script.
4. Choose a mode from the menu.
5. Follow the prompts and play.

---

## 📚 Inspiration

Based on the classic version here:
🔗 [GeeksForGeeks - Python | Cows and Bulls Game](https://www.geeksforgeeks.org/python/python-cows-and-bulls-game/)

> This version improves upon it with:
> – Multi-mode support
> – Hidden code entry in PvP
> – Smarter AI guessing logic
> – Cleaner UI & structured flow


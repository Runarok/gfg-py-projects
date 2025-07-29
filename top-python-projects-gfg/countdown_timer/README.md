# ⏲️ Countdown Timer

This is my extended take on the classic **Countdown Timer** in Python, originally inspired by [this GeeksforGeeks tutorial](https://www.geeksforgeeks.org/python/how-to-create-a-countdown-timer-using-python/).

---

## 🧠 Overview

This project is a **versatile, interactive countdown timer tool** built for terminal use. Designed for online Python compilers, it's **standalone, minimal on imports**, and packed with features:

* **Predefined Modes**: Pomodoro (25m), Short Break (5m), Long Break (15m), Deep Focus (50m)
* **Custom Input**: Accepts both total seconds or formatted time (HH\:MM\:SS)
* **Smart Loop Mode**: Automatically restart sessions — great for routine workflows
* **Real-Time Progress Bar**: Visual indicator of elapsed vs remaining time
* **Session Tracking**: Tracks total time across sessions and completed cycles
* **Minimal Dependencies**: Uses only built-in `time` module for high compatibility
* **Auto-Padding & Clean Formatting**: Timer always shows as `HH:MM:SS`, with progress indicators
* **Menu-Driven CLI**: Interactive and intuitive, no prior setup needed

---

## 📂 Code Files

🔸 **[`countdown_timer.py`](./countdown_timer.py)** — Full-feature standalone countdown timer with all features listed above.

> ⚙️ Requires only Python 3+. Designed to work cleanly in browser-based compilers.

---

## 🚀 How to Use

Just run the script. You'll get an interactive menu:

```text
⏲️ Countdown Timer Menu:
1. Pomodoro (00:25:00)
2. Short Break (00:05:00)
3. Long Break (00:15:00)
4. Focus Session (00:50:00)
5. Custom Time
6. Toggle Loop Mode (Currently: OFF)
7. Show Stats
8. Exit
```

**Choose a mode** → Timer begins → View live countdown + progress bar.
Session summary and stats are printed at the end.

---

## 🧱 Extension Ideas

This modular script makes it easy to:

* Add keyboard shortcuts or automation triggers
* Log session stats to a file
* Extend with CLI args for advanced usage
* Add alerts (like beeps or OS-level notifications, depending on platform)

---

## 🧬 Inspiration & Origin

This tool is a significant upgrade over the basic version here:

[Python Countdown Timer – GeeksforGeeks](https://www.geeksforgeeks.org/python/how-to-create-a-countdown-timer-using-python/)

While the original shows the core idea, this version expands it into a **functional, reusable timer tool** with real use-case utility — especially for productivity-focused workflows (e.g., studying, deep work blocks, task sprints).


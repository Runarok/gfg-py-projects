Here’s your clean and minimal **README.md** for the enhanced FLAMES Compatibility Tool, matching your previous format:

---

# 🔥 FLAMES Compatibility Tool — Clean Python Edition

> A polished, case-insensitive FLAMES game implementation with full **batch vs batch** and **ranking features**.
> Based on the classic game from [GeeksForGeeks](https://www.geeksforgeeks.org/python/python-program-to-implement-simple-flames-game/) — upgraded with better structure, scoring, and clean UX.

---

## 📌 Features

* ✅ **Compare any two names**
* ✅ **One name vs many** (batch compatibility ranked top to bottom)
* ✅ **Group vs group** — auto picks best match per person
* ✅ **Ranked output** with relation scores
* ✅ Case-insensitive and space-tolerant
* ✅ Fully standalone Python 3 script (no imports required)

---

## 📂 Code Files

🔸 **[`flames_matcher.py`](./flames_matcher.py)** — Full FLAMES compatibility matcher with all features above.

> ⚙️ Requires only Python 3+. Designed to work in browser-based compilers as well.

---

## 🧠 Sample Usage (Batch vs Batch)

```
📊 Top Matches for Each Person:

Alex 💫 Best match → Riya (Love, Score: 6)
Sam  💫 Best match → Diya (Affinity, Score: 4)

📋 Full Comparison Table:

Alex           <-> Riya           | Love         | 6
Alex           <-> Diya           | Friendship   | 3
Sam            <-> Riya           | Sibling-like | 2
Sam            <-> Diya           | Affinity     | 4
```

---

## 🔡 Compatibility Legend

| Letter | Meaning      | Score |
| ------ | ------------ | ----- |
| F      | Friendship   | 3     |
| L      | Love         | 6     |
| A      | Affinity     | 4     |
| M      | Marriage     | 5     |
| E      | Distance     | 1     |
| S      | Sibling-like | 2     |

---

## 🚀 How to Use

1. Run the script with Python 3
2. Choose:

   * `1` → Two names
   * `2` → One name vs group (comma-separated)
   * `3` → Group vs group
3. View top matches and scores

---

## 📎 Credits

Based on the logic from:
🔗 [GeeksForGeeks – FLAMES Game in Python](https://www.geeksforgeeks.org/python/python-program-to-implement-simple-flames-game/)

---

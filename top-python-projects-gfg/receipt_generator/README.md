# 🧾 PDF Receipt Generator (Dark/Light Mode)

This script generates a **professional PDF receipt** using Python’s ReportLab library — with built-in support for **light and dark themes**, clear tabular formatting, timestamps, and custom branding.

> ⚙️ This is a **refined version** of the base idea from [this GeeksforGeeks article](https://www.geeksforgeeks.org/python/creating-payment-receipts-using-python/), with improved structure, theming, and minimal hardcoding.

---

## ✅ Features

* 🔁 **Dark & Light Mode** toggle via `THEME` variable
* 🧠 Auto-timestamped receipt generation
* 📋 Structured layout with subtotal, discount, total
* 🧾 Custom footer and organization name support
* 📄 A4-sized PDF output with clean font, spacing, and alignment

---

## 📂 Code File

🔸 **[`receipt_generator.py`](./receipt_generator.py)** — PDF receipt generator with light/dark theme toggle, styled table layout, and timestamp/footer support.

> ⚙️ Requires only `reportlab`. Designed to run smoothly in Python 3+ environments. Output is an A4-format professional receipt.

---

## 🖼 Output Preview

| Theme   | Sample Filename     |
| ------- | ------------------- |
| `light` | `receipt_light.pdf` |
| `dark`  | `receipt_dark.pdf`  |

*(Run the script to generate actual PDF — preview not embedded here)*

---

## ⚙️ Config Options

```python
THEME = "dark"  # Change to "light" for white background
ORG_NAME = "GeeksforGeeks"
FOOTER_TEXT = "Thank you for your purchase!"
```

---

## 🚀 How to Run

1. First, make sure you have ReportLab installed. If not, install it using pip:

   ```bash
   pip install reportlab
   ```

2. Run the script:

   ```bash
   python receipt_generator.py
   ```

3. Output will be saved as `receipt_dark.pdf` or `receipt_light.pdf` depending on theme.

---

## 📄 Based On

Original concept from:
👉 [GeeksforGeeks: Creating Payment Receipts using Python](https://www.geeksforgeeks.org/python/creating-payment-receipts-using-python/)

This version adds:

* Theme toggle
* Cleaner table formatting
* Separation of data/config from logic
* Timestamp and footer support

---

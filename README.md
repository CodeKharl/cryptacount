# 📘 CryptaCount: Discrete Password Entropy Analyzer

**CryptaCount** is a Python-based tool that analyzes password strength using **Discrete Mathematics**—specifically **Permutations, Combinations, and the Rule of Product**.
It computes the password search space, entropy (bits), and generates a valid random password that satisfies exact character-type constraints (e.g., _exactly 2 digits_).

This tool was created for **CS 211 – Discrete Structure 2** as a demonstration of applying counting principles in real-world security.

---

## 🔧 Features

- Calculates password **search space** (N) using counting principles
- Computes **entropy** in bits (log₂ N)
- Supports character constraints (e.g., _must contain exactly k digits_)
- Uses **multinomial coefficients & combinations**
- Generates a valid random password
- Handles impossible constraints safely
- Supports **command-line arguments**
- Uses cryptographically secure random generation

---

## 🧠 Discrete Math Concepts Used

### **1. Rule of Sum & Rule of Product**

Used to derive total available characters and total ways to fill positions:

```
C = 26_lower + 26_upper + 10_digits = 62
N = C^L
```

---

### **2. Combinations & Multinomial Coefficient**

Used to compute placement ways of required characters:

```
Placement = L! / (k1! k2! ... km! (L−Σki)!)
```

Implemented using:

```python
multinomial_coefficient()
```

---

# ▶️ How to Run

## ✔ Method 1 — Default Behavior

If you run the script with no arguments:

```
python cryptacount.py
```

It will use the built-in example:

- Length: 8
- Included classes: lower, upper, digits
- Exact requirement: 2 digits

---

# 🖥️ ✔ Method 2 — Using Command-Line Arguments (Recommended)

You can fully configure the program using CLI arguments.

### ## Syntax

```
python cryptacount.py \
    --length <L> \
    --include <class1> <class2> ... \
    --require <class>=<k> <class>=<k> ...
```

---

# 📌 Available Arguments

| Argument    | Description                     | Example                                |
| ----------- | ------------------------------- | -------------------------------------- |
| `--length`  | Password length (integer)       | `--length 12`                          |
| `--include` | Classes allowed in the password | `--include lower upper digits symbols` |
| `--require` | Exact required character counts | `--require digits=3 symbols=1`         |

---

# 📚 Character Class List

| Class Name | Characters                     |
| ---------- | ------------------------------ |
| `lower`    | a–z                            |
| `upper`    | A–Z                            |
| `digits`   | 0–9                            |
| `symbols`  | punctuation/special characters |

---

# 🧪 Examples

### **Example 1 — 10-character password with 2 digits**

```
python cryptacount.py \
   --length 10 \
   --include lower upper digits \
   --require digits=2
```

### **Example 2 — 12-character password with 4 digits & 2 symbols**

```
python cryptacount.py \
   --length 12 \
   --include lower upper digits symbols \
   --require digits=4 symbols=2
```

### **Example 3 — Only lowercase allowed**

```
python cryptacount.py --length 8 --include lower
```

---

# ⚙️ How to Use It (Internals)

1. Choose your password length
2. Select which character classes you want to use
3. (Optional) Add exact count requirements
4. Run the program
5. The output will include:
   - Search space (N)
   - Entropy (bits)
   - Secure sample password
   - All computation steps are based on discrete math counting rules

---

# 📜 Core Formula

```
N = (L! / (k1! k2! ... km! (L − Σki)!))
    × Π (Ci^ki)
    × (Cother^(L − Σki))
```

Where:

- **L** = password length
- **ki** = required counts
- **Ci** = class sizes
- **Cother** = allowed characters for filler positions

---

# 🔐 Security Notes

- Uses Python’s `secrets` module
- Strong randomness (SystemRandom)
- Designed for educational and academic demonstration

---

# 📄 License

This project is intended for academic use in **CS 211 – Discrete Structure 2**.
You may modify or extend it for learning purposes.

---

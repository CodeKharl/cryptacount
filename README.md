# 📘 CryptaCount: Discrete Password Entropy Analyzer

**CryptaCount** is a Python-based tool that analyzes password strength using **Discrete Mathematics** — specifically **Permutations, Combinations, and the Rule of Product**.
It computes the password search space, entropy (bits), and generates a valid random password that satisfies exact character-type constraints (e.g., _exactly 2 digits_).

This tool was created for **CS 211 – Discrete Structure 2** as a demonstration of applying counting principles in real-world security.

---

## 🔧 Features

- Calculates password **search space** (N) using counting principles
- Computes **entropy** in bits (log₂ N)
- Supports character constraints (e.g., _must contain exactly k digits_)
- Uses **multinomial coefficients & combinations**
- Generates a valid random password
- Handles impossible constraints safely (raises `ValueError` when exact counts exceed length)
- Supports **command-line arguments**
- Uses cryptographically secure random generation (`secrets`)

---

## 🧠 Discrete Math Concepts Used

### **1. Rule of Sum & Rule of Product**

Used to derive total available characters and total ways to fill positions.

With all four classes enabled, the pool is:

```
C = 26_lower + 26_upper + 10_digits + 32_symbols = 94
N = C^L   (no exact constraints)
```

Without exact constraints, this is simply `C^L`. With exact constraints, the formula in [Core Formula](#-core-formula) is used instead.

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

## ✔ Method 1 — Built-in Example

Run the example directly from the module file:

```
python3 cryptacount/password_generator.py
```

It uses the built-in example:

- Length: 8
- Included classes: lower, upper, digits
- Exact requirement: 2 digits

---

# 🖥️ ✔ Method 2 — Using Command-Line Arguments (Recommended)

Run the package from the project root:

```
python3 -m cryptacount \
    --length <L> \
    --include <class1> <class2> ... \
    [--exact <class>=<k> <class>=<k> ...]
```

### ## Syntax

| Argument    | Required | Description                     | Example                                |
| ----------- | -------- | ------------------------------- | -------------------------------------- |
| `--length`  | Yes      | Password length (integer)       | `--length 12`                          |
| `--include` | Yes      | Classes allowed in the password | `--include lower upper digits symbols` |
| `--exact`   | No       | Exact required character counts | `--exact digits=3 symbols=1`           |

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
python3 -m cryptacount \
   --length 10 \
   --include lower upper digits \
   --exact digits=2
```

### **Example 2 — 12-character password with 4 digits & 2 symbols**

```
python3 -m cryptacount \
   --length 12 \
   --include lower upper digits symbols \
   --exact digits=4 symbols=2
```

### **Example 3 — Only lowercase allowed**

```
python3 -m cryptacount --length 8 --include lower
```

---

# 📁 Project Structure

```
cryptacount/
├── cryptacount/
│   ├── __main__.py          # CLI entry point
│   └── password_generator.py # core logic (search space, entropy, generation)
├── docs/                     # academic papers & reference material
│   ├── CryptaCount-Discrete.pdf
│   ├── CryptaCount-Paper.pdf
│   ├── CryptaCount-Program.pdf
│   └── Password_Entropy_Cheatsheet.odt
├── LICENSE                   # MIT License
└── README.md
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

Sample output:

```
Length: 10
Included Classes: ['lower', 'upper', 'digits']
Exact Count: {'digits': 2}
Search space (N): 240,568,778,391,552,000
Entropy: 57.74 bits
Sample password: 8udTFhxU7l
```

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

- Uses Python's `secrets` module
- Strong randomness (`SystemRandom`)
- Designed for educational and academic demonstration

---

# 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

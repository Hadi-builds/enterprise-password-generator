# Enterprise Random Password Generator

A cryptographically secure command-line password generator engineered in Python, designed in compliance with modern **NIST SP 800-63-4** guidelines and structured around the **Input-Process-Output (IPO)** architectural pattern.

Developed under the **DecodeLabs Industrial Training Program (Project 3)**.

---

## Core Technical Highlights

- **Cryptographically Secure Pseudo-Random Number Generation (CSPRNG)**: Replaces deterministic pseudo-random engines (`random` / Mersenne Twister) with Python's built-in `secrets` module, deriving entropy directly from OS hardware-level noise.
- **Linear Time & Memory Efficiency ($O(N)$)**: Eliminates the quadratic memory overhead caused by repeated string concatenation (`+=`) on immutable strings by utilizing list comprehension and `str.join()`.
- **Standardized Character Sets**: Leverages the `string` module (`ascii_letters`, `digits`, `punctuation`) for platform-independent, locale-agnostic consistency.
- **NIST SP 800-63-4 Alignment**: Emphasizes absolute length over outdated, predictable complexity rules. Validates minimum length constraints to protect against high-performance brute-force attacks.
- **Shannon Information Entropy Engine**: Computes theoretical password resistance mathematically in bits ($E = L \times \log_2(R)$) before credential delivery.

---

## Architecture (Input-Process-Output)

```
[ Input Stage ]    --> User length capture & NIST boundary validation
       ↓
[ Process Stage ]  --> Cryptographic sampling via secrets.choice() & O(N) ''.join()
       ↓
[ Output Stage ]   --> Credential delivery, pool size calculation & entropy verification
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Running the Application

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/enterprise-password-generator.git](https://github.com/YOUR-USERNAME/enterprise-password-generator.git)
   cd enterprise-password-generator
   ```

2. Run the script:
   ```bash
   python main.py
   ```

---

## Sample Execution

```text
==================================================
  Enterprise Random Password Generator
==================================================

Enter desired password length (min 15 recommended): 16

--------------------------------------------------
Generated Password : k9#F!zL2@mQ9$WpX
Character Pool (R) : 94
Entropy Strength   : 104.87 bits
Security Status    : Highly Secure (Enterprise Grade)
--------------------------------------------------
```

---

## Mathematical Security Model

Information entropy measures the unpredictability of a password string:

$$E = L \times \log_2(R)$$

Where:
- **$E$**: Entropy measured in bits.
- **$L$**: Password length.
- **$R$**: Total character pool size ($R = 94$ for alphanumeric + punctuation).

Passwords with an entropy rating of **80+ bits** provide robust resistance against offline GPU cluster attacks.

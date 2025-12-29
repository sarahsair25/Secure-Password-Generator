# Secure-Password-Generator
A secure random password generator built in Python with a clean CLI interface.Secure password generator using Python’s cryptographic randomness, packaged as a reusable CLI tool with __main__.py and pyproject.toml.
# 🔐 Secure Password Generator (Python CLI)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![CLI](https://img.shields.io/badge/Interface-CLI-green.svg)
![Security](https://img.shields.io/badge/Focus-Security-critical.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A **secure random password generator** built in **Python** and packaged as a **command-line interface (CLI)** tool.  
This project focuses on **clean Python packaging**, **secure password generation**, and **real-world CLI design**.

Perfect as a **portfolio project** for entry-level Python / backend / security-focused roles.

---

## ✨ Features

- 🔐 Cryptographically secure password generation
- 🖥️ Easy-to-use **command-line interface**
- 📏 Customizable password length
- 🔡 Toggle uppercase, lowercase, digits, and symbols
- 📦 Proper Python package structure
- 🚀 Run with **one command**
- 🧩 Beginner-friendly, production-style layout

---

## 🛠️ Tech Stack

- **Python 3.9+**
- `secrets` & `string` (secure randomness)
- `argparse` (CLI parsing)
- Python packaging (`__main__.py`, `pyproject.toml`)

---

## 📦 Installation

### Clone the repository
```bash
git clone https://github.com/your-username/secure-password-generator.git
cd secure-password-generator

Install in editable mode
python -m pip install -e .

▶️ Usage

Run the password generator from anywhere:

password-generator


Example output:

7pfUni]BhPi40}uL

🔧 CLI Options
password-generator --help

Option	Description
-l, --length	Password length (default: 16)
--no-upper	Disable uppercase letters
--no-lower	Disable lowercase letters
--no-digits	Disable digits
--no-symbols	Disable symbols

Examples:

password-generator -l 24
password-generator --no-symbols
password-generator -l 20 --no-digits
📂 Project Structure
secure-password-generator/
│
├── password_generator/
│   ├── __init__.py
│   ├── __main__.py        # Package entry point
│   ├── cli.py             # CLI logic
│   ├── generator.py       # Password generation logic
│   └── strength.py        # (Optional) password strength logic
│
├── pyproject.toml         # Packaging & CLI entry point
└── README.md
git clone https://github.com/your-username/secure-password-generator.git
cd secure-password-generator

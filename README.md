# 🔐 Password Checker  
A lightweight Python tool that checks whether a password appears in a known list of weak or commonly used passwords. This project is ideal for learning basic Python, exploring file operations, and understanding simple password-strength validation logic.

---

## 📁 Project Structure

password-checker/
│
├── password_checker.py # Main script that runs the checker
└── common_passwords.txt # List of weak or commonly used passwords


---

## 🚀 Features

- 🔎 **Checks whether a password exists in a known weak-password list**
- 📄 Uses a local text file (`common_passwords.txt`) for fast lookup
- 💡 Provides clear "safe" or "unsafe" feedback
- 🧪 Simple and beginner-friendly Python example
- 🖥️ CLI-based, no external dependencies required

---

## 🛠️ Installation & Setup

1. **Clone your repository**

   ```bash
   git clone https://github.com/gmsmith928-sudo/password-checker.git
   cd password-checker/password-checker

    Ensure Python is installed

    python --version

    (Python 3.x recommended)

    No additional libraries are required — everything runs out of the box.

▶️ How to Use

Run the script:

python password_checker.py

When prompted, enter a password:

Enter a password to check: hunter2
Warning! This password appears in the common password list.

Or a safe example:

Enter a password to check: MyU$erP@ssw0rd2025
Good news! This password does NOT appear in the weak password list.

🧠 How It Works

The script:

    Loads a list of weak/common passwords from common_passwords.txt

    Prompts the user securely for a password

    Compares the input password against the list

    Outputs whether the password is found or not

📦 Example Snippet (from password_checker.py)

with open("common_passwords.txt") as file:
    common_passwords = file.read().splitlines()

password = input("Enter a password to check: ")

if password in common_passwords:
    print("Warning! This password appears in the common password list.")
else:
    print("Good news! This password does NOT appear in the weak password list.")

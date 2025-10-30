# Password-Strength-Checker
A comprehensive Python-based password strength analyzer that evaluates password security and provides actionable feedback to help users create stronger, more secure passwords.
📋 Features

Multi-Level Strength Analysis: Rates passwords from "Very Weak" to "Very Strong"
Length Validation: Checks password length and recommends 12+ characters
Character Variety Detection: Validates presence of uppercase, lowercase, numbers, and special characters
Common Pattern Detection: Identifies weak patterns like "123", "password", "qwerty", etc.
Repetition Detection: Flags repeated characters (e.g., "aaa", "111")
Entropy Calculation: Measures password randomness in bits
Crack Time Estimation: Estimates time needed for brute force attacks
Color-Coded Feedback: Visual indicators for easy interpretation
Interactive Interface: Test multiple passwords in one session
No external dependencies required! Uses only Python standard library (re, math)

💻 Usage
Run the script:
bashpython PasswordChecker.py
Enter passwords when prompted:
Enter password to check (or 'quit' to exit): MyP@ssw0rd123
The tool will display:

Overall strength rating (Very Weak → Very Strong)
Score out of 10
Password length
Entropy (bits of randomness)
Estimated crack time
Detailed feedback with specific improvement suggestions

Type quit to exit the program.
📊 Scoring System
The tool evaluates passwords based on:
CriterionPointsLength (12+ chars)3Lowercase letters1Uppercase letters1Numbers1Special characters2No common patterns1No repetitionsBonus
Strength Ratings:

0-3: Very Weak 🔴
4-5: Weak 🟠
6-7: Moderate 🟡
8-9: Strong 🟢
10+: Very Strong 🟢

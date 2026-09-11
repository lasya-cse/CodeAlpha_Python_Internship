# Task 1 - Hangman Game
## 📌 Project Overview
The Hangman Game is a console-based word guessing game developed using Python as part of the CodeAlpha Python Programming Internship. The game randomly selects a word from a predefined list, and the player must guess the hidden word one letter at a time.
## 🎯 Objective
The objective of this project is to implement a simple and interactive Python game while demonstrating programming concepts such as random selection, loops, conditional statements, strings, lists, functions, input validation, and basic game logic.
## ✨ Features
- Random selection of a word from 5 predefined words
- Letter-by-letter word guessing
- Maximum of 6 incorrect guesses
- Visual Hangman stages displayed in the console
- Input validation for user guesses
- Prevents duplicate letter guesses
- Displays previously guessed letters
- Shows remaining attempts
- Score calculation based on performance
- Option to play the game again
- Simple and user-friendly console interface
## 🛠️ Technologies Used
- Python 3
- Random Module
- Strings
- Lists
- Functions
- While Loops
- For Loops
- If-Else Statements
- Input Validation
## 🎮 How the Game Works
1. The program contains 5 predefined words.
2. A word is randomly selected using the `random` module.
3. The selected word is displayed as hidden underscores.
4. The player enters one letter at a time.
5. If the guessed letter exists in the word, it is revealed.
6. If the guessed letter is incorrect, the wrong guess count increases.
7. The player can make a maximum of 6 incorrect guesses.
8. The Hangman figure is updated after each incorrect guess.
9. The player wins when all letters of the word are correctly guessed.
10. The game ends when the player reaches 6 incorrect guesses.
11. The player can choose to play another round.
## 📋 Game Rules
- Only one alphabet letter can be entered at a time.
- Repeated guesses are not counted again.
- Correct guesses reveal the corresponding letters.
- Incorrect guesses reduce the remaining attempts.
- A maximum of 6 incorrect guesses is allowed.
- Guess the complete word before all attempts are used to win.
## 📂 Project Structure
```text
Task1_Hangman_Game/
├── hangman.py
└── README.md

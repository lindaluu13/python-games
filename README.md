# 🎮 Python Games Collection

Welcome to **Python Games**, a beginner-friendly collection of interactive terminal games written in Python. Each game is designed to reinforce core programming concepts like control flow, functions, loops, conditionals, and basic I/O.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Games Included](#games-included)
  - [1. Number Guessing Game](#1-number-guessing-game)
  - [2. Rock, Paper, Scissors](#2-rock-paper-scissors)
  - [3. Hangman](#3-hangman)
  - [4. Word Guessing Game](#4-word-guessing-game)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Notes](#notes)
- [License](#license)

---

## Overview

This repository is a compilation of classic mini-games made using **pure Python**. It’s perfect for anyone looking to understand the fundamentals of game loops, input handling, basic error management, and structuring Python projects in a modular way.

---

## Games Included

### 1. Number Guessing Game
Guess a number between 1 and 100 within a limited number of attempts. The game gives hints like "too high" or "too low" after each guess.

- **Skills practiced:** Random number generation, input validation, loops.
- **Attempts limit:** 7

### 2. Rock, Paper, Scissors
Play Rock, Paper, Scissors against the computer. The winner is determined based on the classic rules.

- **Skills practiced:** Conditionals, custom exceptions, dictionaries.
- **Fun factor:** Emojis included for better visual feedback! 🪨 📄 ✂️

### 3. Hangman
A classic hangman game where you guess a word, one letter or word at a time. Lose a life for each wrong guess.

- **Skills practiced:** String manipulation, list indexing, game state control.
- **Visual feedback:** ASCII art hangman as you lose lives.

### 4. Word Guessing Game
Guess the letters of a hidden word, with unlimited attempts. A simplified version of Hangman with no life loss mechanic.

- **Skills practiced:** Loops, input filtering, list mutation.
- **Encouragement feedback:** Encourages correct guesses and avoids repeated ones.

---

## Getting Started

**Clone the repository**

   ```bash
   git clone https://github.com/your-username/python-games.git
   cd python-games
   ```

## Requirements

Python 3.7 or higher.

No external libraries are required (everything uses the Python standard library)

## How to Run

You can run the full game collection via the central launcher script:

1. **Navigate to the project directory**:
   ```bash
   cd python-games
   or
   cd ..
   ```

Run the launcher:
```bash
python3 main.py
```
Choose a game:
1. Number Guessing
2. Rock, Paper, Scissor
3. Hangman
4. Word Guessing

## Notes

The games use emojis and ASCII art for visual feedback. If you see weird characters, ensure your terminal supports UTF-8.

You can customize the word_list in hangman/words.py to increase difficulty.

Feel free to extend the games with levels, scoring systems, or graphical interfaces!

## License

This project is open-source and available under the MIT License.

***Happy coding and have fun playing! 🎉***
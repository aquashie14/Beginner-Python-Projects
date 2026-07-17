# Beginner Python Projects

A collection of beginner-friendly Python projects focused on core programming concepts like loops, conditionals, input handling, and randomness.

---

## Projects

### 🎲 Dice Roll Game (`Dice_roll_game.py`)
A simple interactive dice roller.

**Features:**
- Roll as many dice as you want per round
- Tracks the total number of individual dice rolled across all rounds
- Handles invalid input gracefully
- Exits cleanly and prints your total roll count

**How to run:**
```bash
python Dice_roll_game.py
```

**Sample interaction:**
```
Roll your dice ? (yes/no): yes
How many dice do you want to roll? 3
[4, 1, 6]
Roll your dice ? (yes/no): no
Okay, maybe next time!
You rolled the dice 3 times.
```

---

### 🔢 Number Guessing Game (`Number_guessing_game.py`)
Guess a randomly generated number within a custom range.

**Features:**
- Player sets their own min and max range
- Up to 10 attempts to guess the number
- Hints after each guess (Too low / Too high)
- Invalid input (non-numeric) doesn't count as an attempt
- Reveals the answer if all attempts are used

**How to run:**
```bash
python Number_guessing_game.py
```

**Sample interaction:**
```
Enter the minimum value for the guessing game: 1
Enter the maximum value for the guessing game: 100
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 63
Congratulations! You guessed the number!
It took you 3 guesses.
```


---

### ✊ Rock Paper Scissors (`rock_paper_scissors.py`)
A two-player Rock Paper Scissors game with emoji display and score tracking.

**Features:**
- Two players take turns entering their choices (r / p / s)
- Displays emoji for each choice (✊ ✋ ✌️)
- Determines the winner per round
- Tracks wins, losses, and ties across multiple rounds
- Shows full scoreboard when players quit

**How to run:**
```bash
python rock_paper_scissors.py
```

**Sample interaction:**
```
Player 1, choose Rock, Paper, or Scissors (r/p/s): r
Player 2, choose Rock, Paper, or Scissors (r/p/s): s
Player 1 chose: ✊
Player 2 chose: ✌️
Player 1 wins!
Do you want to play again? (yes/no): no
You played 1 rounds.
Player 1 wins: 1, Player 2 wins: 0, Ties: 0
```

---

### 📷 QR Code Generator (`qr_code_generator.py`)
Generates a QR code image from any URL or text and saves it as a PNG file.

**Features:**
- Accepts any URL or text as input
- Saves the QR code as a `.png` file with a custom filename
- Configurable error correction, box size, and border

**How to run:**
```bash
python qr_code_generator.py
```

**Sample interaction:**
```
Enter the data or URL to generate QR code: https://github.com/aquashie14
Enter the output file name to save the QR code image (with .png extension): my_qr.png
QR code generated and saved as my_qr.png.
```

---

## Requirements
- Python 3.x
- `qrcode[pil]` — for QR code generation (`pip install qrcode[pil]`)
- Built-in `random` module (no install needed)

## Author
**aquashie14** — [GitHub Profile](https://github.com/aquashie14)

# 🏝️ Journey to the Mysterious Island

A modular Python text-adventure game where players explore a mysterious island, make important decisions, survive dangerous encounters, and work toward escaping the island.

The game is divided into multiple chapters, with player choices affecting the story and game state as the adventure progresses.

## 🎮 Features

- Five-chapter interactive adventure
- Branching player choices
- Shared game state across chapters
- Checkpoint and restart system
- User input validation
- Multiple outcomes and escape paths
- Modular Python architecture

## 🛠️ Technologies & Concepts

- Python 3
- Functions
- Dictionaries
- Conditional statements
- Loops
- Modular programming
- User input handling
- State management

## 📁 Project Structure

```text
mysterious-island-adventure/
│
├── main.py
├── utils.py
├── chapter_1.py
├── chapter_2.py
├── chapter_3.py
├── chapter_4.py
├── chapter_5.py
└── README.md
```

`main.py` controls the overall game flow and chapter progression.

`utils.py` contains reusable functions for input validation, checkpoints, restart behavior, and displaying game banners.

Each chapter is stored in its own Python module and updates a shared state dictionary as the player progresses.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/divyang2163/mysterious-island-adventure.git
```

### 2. Open the project directory

```bash
cd mysterious-island-adventure
```

### 3. Run the game

```bash
python main.py
```

Python 3.8 or later is recommended.

## 🧠 What I Learned

Building this project helped me practice organizing a larger Python program across multiple files instead of keeping everything in one script.

I also gained experience with shared program state, functions, input validation, conditional logic, loops, checkpoints, and designing branching paths based on user decisions.

## 🔮 Future Improvements

- Add additional story branches and endings
- Add a scoring or achievement system
- Expand the inventory and clue system
- Improve checkpoint functionality
- Add automated tests
- Create a graphical or web-based version

## 👤 Author

**Divyang Parikh**

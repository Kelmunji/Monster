# Monster Collection CLI Game

Welcome to the **Monster Collection CLI Game** – a text-based adventure where you catch, train, and battle monsters in a terminal-based world inspired by Pokémon!

## 📦 Features
- 🎮 Start a player profile and choose your starter monster
- 🧭 Explore and encounter wild monsters
- 🎯 Attempt to catch monsters based on type rarity and your level
- 📚 View your growing monster collection
- ⚙️ CLI interface built with `typer`
- 🗃️ Persistent data storage with SQLAlchemy + SQLite

---

## 🗂️ Project Structure
```
monster_game/
├── __init__.py
├── database.py           # Database connection
├── models.py             # ORM models
├── seed_data.py          # Initial monster species
├── monster_system.py     # Core monster logic
├── cli.py                # CLI application
requirements.txt          # Dependencies
README.md                 # Project info
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Create a Virtual Environment and Install Requirements
```bash
pip install pipenv
pipenv install
pipenv shell
```

### 3. Initialize the Database
```bash
python -m monster_game.database
python -m monster_game.seed_data
```

### 4. Run the CLI Game
```bash
python -m monster_game.cli --help
```

---

## 🔧 CLI Commands

### Start a Player Profile
```bash
python -m monster_game.cli start --username "Ash"
```

### Explore the World and Catch Monsters
```bash
python -m monster_game.cli explore --player-id 1
```

### View Your Monster Collection
```bash
python -m monster_game.cli collection --player-id 1
```

---

## 💡 Future Features
- Turn-based battle system
- Monster evolution
- Gym challenges
- Trading and PvP features

---

## 🧠 Learning Objectives
- Practice with SQLAlchemy ORM and database relationships
- Build robust command-line interfaces with `typer`
- Learn modular software design using Python
- Implement game mechanics and persistent game state

---

## 🏁 License
This project is for educational use. Contributions are welcome!

---

Happy coding, Monster Trainer! 🐉⚡🌿
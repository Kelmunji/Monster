# 🐉 MonsterQuest: Terminal Adventure Game

Welcome to **MonsterQuest**, a terminal-based fantasy adventure game where players collect, battle, and trade creatures in a dynamic CLI environment. Powered by Python and SQLAlchemy, this project brings the magic of turn-based monster battles to your terminal window.

---

## 🚀 Features

- 🧙 Player profile system with experience and currency tracking  
- 🐾 Collect, level up, and manage a roster of creatures  
- ⚔️ Turn-based combat with skill and health logic  
- 🔁 Trade creatures between players  
- 🗃️ Persistent storage using SQLite and SQLAlchemy  
- 🧪 Includes seed data to jumpstart gameplay

---

## 📁 Project Structure

```bash
Monster-Game/
├── start.py             # Game entry point
├── launcher.py          # Command-line interface launcher
├── engine/              # Core game logic
│   ├── combat.py
│   ├── creature.py
│   ├── user.py
│   ├── trade.py
│   └── rules.py
├── core/                # Database models and connection handling
│   ├── connection.py
│   ├── models.py
│   └── manager.py
├── data/                # Game database and seeding
│   ├── monsters.db
│   └── seed.py
├── migrations/          # Alembic migrations
├── Pipfile              # Dependency definitions
├── Pipfile.lock
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/monster-quest.git
   cd monster-quest
   ```

2. **Create virtual environment with Pipenv**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Run seed script (optional)**
   ```bash
   python data/seed.py
   ```

4. **Start the game**
   ```bash
   python start.py
   ```

---

## 📚 Tech Stack

- Python 3.10+
- SQLAlchemy ORM
- SQLite for local storage
- Alembic for migrations

---

## 🧠 Game Flow Summary

- **Launcher**: Choose to create a player or start exploring
- **Battles**: Encounter wild creatures and fight turn-by-turn
- **Trading**: Exchange monsters with other players
- **Leveling Up**: Gain experience from wins and collect rewards

---

## 🛠️ Development Tips

- All database-related logic is in `core/`
- Game loop and logic live in `engine/`
- Use `seed.py` to populate basic monsters and players

---

## 📜 License

This project is released under the MIT License. Feel free to modify and expand!

---

## 👾 Credits

Built with imagination and code. Inspired by classic monster-collection games.
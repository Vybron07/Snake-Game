# Snake Game 🐍

A classic Snake game developed using Python and Pygame.

This project recreates the traditional Snake game with a clean interface, multiple difficulty levels, score tracking, and additional features to make the gameplay more enjoyable. It was built from scratch to understand basic game development concepts such as game loops, collision detection, user input handling, and game state management.

## Features

- Classic Snake gameplay
- Start menu system
- Multiple difficulty levels
- Smooth snake movement
- Random food generation
- Snake growth after eating food
- Score tracking
- High score saving
- Wall collision detection
- Self collision detection
- Game over screen
- Restart functionality
- Different game speeds based on difficulty

## Screenshots
<img width="1602" height="936" alt="Screenshot 2026-07-27 000320" src="https://github.com/user-attachments/assets/009edc41-0c39-49be-bb61-70d72b0b0c13" />
<img width="1602" height="952" alt="Screenshot 2026-07-27 000300" src="https://github.com/user-attachments/assets/7d3e6b9c-40a6-4e8b-a992-4a9d125ef3e0" />
<img width="1592" height="932" alt="Screenshot 2026-07-27 000239" src="https://github.com/user-attachments/assets/b86a37d9-8843-4592-8b64-edeb80e1c1c9" />


## Technologies Used

- Python 3.11
- Pygame

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/snake-game.git
```

### Move into the project folder

```bash
cd snake-game
```

### Install dependencies

```bash
pip install pygame
```

### Run the game

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |
| ← Arrow | Move Left |
| → Arrow | Move Right |
| R | Restart Game |
| ESC | Exit Game |

## Gameplay

The objective is simple: control the snake, collect food, and achieve the highest score possible.

Each time the snake eats food:

- The score increases
- The snake becomes longer
- Movement becomes more challenging

The game ends when the snake:

- Hits the boundary
- Collides with its own body

Try to survive as long as possible and beat your highest score.

## Difficulty Levels

The game contains three difficulty modes:

### Easy
- Slower snake movement
- Suitable for beginners

### Medium
- Balanced speed and difficulty

### Hard
- Faster snake movement
- Requires quick reactions

## Project Structure

```text
Snake-Game/
│
├── main.py              # Main game file
├── highscore.txt        # Stores highest score
├── assets/              # Game assets
│
└── README.md
```

## Development

This project was developed using Pygame and focuses on implementing important game development concepts:

- Creating a game loop
- Handling player input
- Updating game objects
- Managing game states
- Implementing collision detection
- Saving and loading game data


## Requirements

Before running the game, make sure you have:

- Python 3.11 or above
- Pygame installed
- A system capable of running Python applications

## Future Compatibility

The project structure allows further expansion while maintaining the current gameplay system.

## Author

**Vivek Raut**

## License

This project is open-source and available for personal and educational use.

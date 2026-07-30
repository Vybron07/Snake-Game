🐍 Snake Game

A classic Snake game built with Python and Pygame, with a modern UI, difficulty settings, high-score tracking, bonus food, animations, pause controls, and game-over handling.

🎮 Features
Classic Snake gameplay
Three difficulty levels:
Easy
Medium
Hard
Score tracking
Persistent high-score system using highscore.txt
Automatic speed increase as the score increases
Red pulsing normal food
Blue Mighty Berry bonus food
Mighty Berry:
Appears periodically
Stays for 5 seconds
Gives +5 score
Adds 5 segments to the snake
Snake head and eye animation
Snake turns red when killed
Immediate game-over screen
Restart with R
Pause/resume with ESC
Settings menu
Difficulty selection menu
Main menu
Bottom event/status bar
Bonus-food countdown
Collision detection with walls and the snake itself
Separate gameplay area below the HUD
No grid for a cleaner appearance
🕹️ Controls
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right
ESC	Pause / Resume
R	Restart after Game Over
🍓 Mighty Berry

The Mighty Berry is a special blue bonus food that appears during gameplay.

When collected:

Score increases by 5
Snake length increases by 5
The bonus event ends immediately

The bottom event bar shows information about the Mighty Berry, including when it will appear and how long it remains active.

📊 Scoring
Normal Food

Each normal food:

+1 Score
Mighty Berry

Each Mighty Berry:

+5 Score
+5 Snake Segments

The game also increases the snake's speed as the score reaches certain thresholds.

🏆 High Score

The highest score is stored in:

highscore.txt

This allows the high score to remain available even after closing the game.

A NEW HIGH SCORE message is displayed when the current score exceeds the previous high score.

💀 Game Over

The game ends when the snake:

Hits the wall
Hits its own body

When the snake dies:

The snake turns red.
The snake stops moving.
The Game Over message appears.
The restart prompt is displayed.
Press R to start a new game.

After restarting, the snake returns to its normal green appearance and the game state is reset.

🎚️ Difficulty

The game currently has three difficulty settings:

Easy   → Slower
Medium → Normal
Hard   → Faster

The difficulty can be changed through the Settings menu.

🖥️ Interface

The game is divided into three main areas:

HUD

The top section displays:

Current Score
High Score
Difficulty
Pause control
Gameplay Area

The main area contains:

Snake
Normal food
Mighty Berry
Snake movement and collisions
Event Bar

The bottom section displays Mighty Berry events and countdown information.

📁 Project Structure
Snake Game/
│
├── main.py
├── highscore.txt
└── README.md
🛠️ Requirements
Python 3.x
Pygame

Install Pygame with:

pip install pygame
▶️ Running the Game

Clone or download the project and open the project folder.

Run:

python main.py

The game will open with the main menu.

🔧 Built With
Python
Pygame
📌 Current Version

The game currently focuses on polishing the core gameplay experience with:

Improved HUD
Animated food
Bonus food system
High-score system
Difficulty system
Pause system
Game-over animation
Cleaner gameplay area
Persistent scoring
👨‍💻 Author

Vivek Raut

Built as a Python/Pygame project while learning game development and programming concepts.

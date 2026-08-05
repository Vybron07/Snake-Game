🐍 Snake Game

A classic Snake game built with Python and Pygame, enhanced with modern UI elements, difficulty levels, bonus food, high scores, death effects, and both keyboard and mouse controls.

🎮 Features
🐍 Classic Snake gameplay
🎯 Three difficulty levels:
Easy
Medium
Hard
🍎 Normal food with animated/pulsing effect
🔵 Mighty Berry bonus food
Appears periodically
Gives +5 score
Makes the snake grow by 5 segments
Automatically disappears after a limited time
🏆 Persistent high-score system using highscore.txt
⚡ Increasing snake speed as the score increases
💀 Game-over state with a red snake
🎬 Death animation/state
🔄 Game-over restart button
🏠 Main Menu button after Game Over
⌨️ Keyboard shortcuts
🖱️ Mouse-based direction control
⏸️ Pause/Resume system
⚙️ Settings and difficulty selection
🎨 Custom HUD and event bar
📊 Score and high-score display
🖥️ 1280×720 game resolution
🔴 Animated normal food
🔵 Animated Mighty Berry
🟢 Custom snake head, body and eyes
🕹️ Controls
Keyboard
Key	Action
↑	Move Up
↓	Move Down
←	Move Left
→	Move Right
ESC	Pause / Main Menu
R	Restart after Game Over
Mouse

During gameplay, click in the direction you want the snake to move.

The game determines whether the click is primarily:

Left
Right
Up
Down

and changes the snake's direction accordingly.

🍓 Mighty Berry

The Mighty Berry is a special bonus food.

Normal cycle
Appears periodically during gameplay
Remains available for a short period
Gives 5 points
Adds 5 segments to the snake
Uses a blue animated appearance

The bonus-food timer is designed to stop progressing when the game is paused or the snake has died.

📈 Difficulty

The game includes three difficulty settings:

Easy    → Slower
Medium  → Normal
Hard    → Faster

The difficulty can be changed from:

Main Menu
   ↓
Settings
   ↓
Difficulty
🏆 High Score

The game stores the highest score in:

highscore.txt

This allows the high score to remain even after closing and reopening the game.

💀 Game Over

The game ends when the snake:

Hits the wall
Hits its own body

The snake changes to a red death state, and a Game Over screen appears.

The Game Over screen provides:

Current score
Best score
RESTART button
MAIN MENU button

Keyboard shortcuts are also available:

R   → Restart
ESC → Main Menu
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

py -3.11 -m pip install pygame
▶️ Running the Game

Open a terminal inside the project directory and run:

py -3.11 main.py

Or:

python main.py
🔧 Technologies Used
Python
Pygame
Random
Math
File Handling
🚀 Future Improvements

Possible future additions include:

🎨 Multiple snake skins
🌈 Custom color themes
✨ Particle effects
🔊 Sound effects
🎵 Background music
🥇 Score leaderboard
🎮 Additional game modes
📱 Android APK version
🖼️ Custom sprites
💫 Better death animation
🎯 More power-ups
👨‍💻 Project

This project was created as a custom Python/Pygame Snake game with the goal of going beyond the basic Snake implementation by adding UI, difficulty, bonus mechanics, persistent scoring, mouse controls, and polished game states.

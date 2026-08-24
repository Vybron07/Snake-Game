# 🐍 Snake Game

A classic Snake Game built using **Python and Pygame**, featuring a modern menu system, multiple difficulty levels, high-score tracking, bonus food, pause functionality, mouse controls, keyboard controls, and game-over animations.

---

## 🎮 Features

### 🏠 Main Menu
- Play
- Settings
- Quit
- Modern dark-themed UI
- Hover effects on buttons
- Game version displayed

### ⚙️ Settings
- Difficulty selection
- Current difficulty is displayed directly on the Settings button
- Easy
- Medium
- Hard

### 🐍 Gameplay
- Classic Snake gameplay
- Snake grows when it eats normal food
- Collision detection with:
  - Walls
  - Snake's own body
- Score tracking
- High-score tracking
- Increasing difficulty as the score increases

### 🍓 Mighty Berry — Bonus Food
A special blue bonus food can appear during gameplay.

- Appears every **20 seconds**
- Remains active for **5 seconds**
- Gives **+5 score**
- Adds **5 segments** to the snake
- Has a pulsing animation
- Cannot spawn on the snake or normal food

### ⏸️ Pause Menu
Press `ESC` during gameplay to pause.

Pause menu includes:

- Resume
- Restart
- Main Menu
- Quit

### 💀 Game Over
When the snake collides with a wall or itself:

- Snake turns red
- Game Over screen appears
- Current score is displayed
- Best score is displayed
- Restart button
- Main Menu button

Keyboard shortcuts are also available.

### 🏆 High Score
The game saves the highest score in:

```text
highscore.txt

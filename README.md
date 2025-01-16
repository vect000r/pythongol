# Game Of Life

A Python project implementing Conway's Game of Life
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

## Table of Contents
- [Functionality](#functionality)
- [Intuition](#intuition)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Functionality

The game presents the user with a menu. If the user clicks play, the game starts paused. The user can click at cells to change their state. After using space, the game starts. If the user wishes to generate a random grid, the R key should be pressed. C key clears the grid (sets every cell's state to dead)
Pushing the ESC key returns to the menu.

## Intuition

A canvas consisting of cells was made with the help of the pygame library's classes. 
The app handles mouse and keyboard input. Clicking on a cell changes its state.
Basic game of life rules were implemented.

## Requirements
- Python 3.12 
- pygame 2.6.1

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vect000r/pythongol
cd pythongol
```
3. Run the application
```bash
python3 main.py
```

## Usage

1. Launch the application
2. Click the "Play" option
3. The canvas will be drawn on screen and the game will start paused
4. Change the state of chosen cells to alive by clicking on them or use the R key to fill the canvas randomly
5. Use space to start the game

## Project Structure

```plaintext
pythongol/
├── src/
│   ├── app.py
│   ├── canvas.py
│   ├── cell.py
│   ├── main.py
│   └── menu.py
└── README.md
```

## Contributing

Contributions/forks are welcome.


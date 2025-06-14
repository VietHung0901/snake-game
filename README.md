# Python Snake Game

A classic Snake game implementation built with Python and Pygame. This project recreates the nostalgic Snake game with modern graphics and smooth gameplay.

![Snake Game Screenshot](screenshots/gameplay.png)

## Features

- Smooth and responsive controls
- Progressive difficulty - snake speeds up as it grows
- Score tracking and high score saving
- Sound effects and background music
- Colorful graphics and animations
- Game over screen with restart option
- Pause functionality

## Requirements

- Python 3.6+
- Pygame 2.0.0+

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-snake-game.git
   cd python-snake-game
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## How to Run

Run the game using Python:

```
python snake_game.py
```

## How to Play

- Use arrow keys (↑, ↓, ←, →) to control the snake's direction
- Eat food to grow longer and increase your score
- Avoid hitting the walls or the snake's own body
- Press 'P' to pause the game
- Press 'R' to restart after game over
- Press 'ESC' to quit

## Project Structure

```
python-snake-game/
│
├── snake_game.py         # Main game file
├── assets/               # Game assets directory
│   ├── sounds/           # Sound effects and music
│   └── images/           # Game graphics
├── screenshots/          # Game screenshots
├── requirements.txt      # Required Python packages
└── README.md             # This file
```

## Customization

You can customize various aspects of the game by modifying the constants at the top of the `snake_game.py` file:

- `WINDOW_WIDTH` and `WINDOW_HEIGHT`: Change the game window size
- `SNAKE_SPEED`: Adjust the initial speed of the snake
- `GRID_SIZE`: Modify the size of the game grid
- `SNAKE_COLOR` and `FOOD_COLOR`: Change the colors of the snake and food

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original Snake game concept
- Pygame community for the excellent game development library
- Contributors and testers who helped improve this game

# Ping Pong

A simple Ping Pong (Pong) game implemented in Python using the Pygame library.

## Preview
![Ping Pong Preview](https://github.com/mihaiapostol14/pin_pong/blob/72c8aa860e662e24409fc4d3c439974c531867b1/assets/preview.gif)

## Purpose

This repository showcases a basic implementation of the classic Pong arcade game, where a player competes against a computer-controlled opponent. It is a fun example project for those learning Python or the Pygame library.

## Main Features

- **Single Player vs Computer**: Play against a simple AI opponent.
- **Keyboard Controls**: Use `W` and `S` keys to move your paddle up and down.
- **Score Display**: Real-time score is shown on the screen.
- **Smooth Graphics**: Uses Pygame for rendering paddles, ball, and dividing line.
- **Simple AI**: The computer paddle follows the ball with basic logic.
- **Reset on Score**: Ball and paddles reset their position after every point.

## Project Structure

```
pin_pong/
├── pin_pong.py
├── requirements.txt
```

- `pin_pong.py`: The main script containing the game logic, rendering, and controls.
- `requirements.txt`: Lists the Python dependencies needed to run the project.

## Usage

### Requirements

- Python 3.x
- All dependencies listed in `requirements.txt`

## Setup and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/mihaiapostol14/pin_pong.git
cd pin_pong
```

### 2. Create and Activate a Virtual Environment

**Install Python**

If you don't have Python installed, follow [this link](https://www.python.org/downloads/) and download the latest version of Python. Then you can check your version of Python using the command lines below:

```bash
# Create a virtual environment
python -m venv venv  

# Activate the virtual environment
source venv/bin/activate  # Linux/MacOS  
venv\Scripts\activate     # Windows  
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```
### 4. Run Game

```bash
python pin_pong.py
```

### Controls

- **Player (Left Paddle):**
  - `W`: Move paddle up
  - `S`: Move paddle down

The right paddle is controlled by the computer.

## License

No license specified. Please contact the repository owner for usage permissions.

## Author

[mihaiapostol14](https://github.com/mihaiapostol14)

---

*Enjoy a nostalgic game of Pong while learning Python and Pygame!*
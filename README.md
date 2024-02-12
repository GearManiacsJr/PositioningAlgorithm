## Gear Maniacs Jr Robot Positioning Algorithm

This is the GitHub repository for the Gear Maniacs Jr Robot Positioning Algorithm, a powerful algorithm designed to precisely control the movement and positioning of the Gear Maniacs Jr robot on the competition field.

### Features

* **Precise Movement:** The algorithm utilizes advanced calculations and sensor data to ensure the robot reaches its desired coordinates with unmatched accuracy.
* **Multiple Movement Options:** Move the robot forward, backward, or rotate to any specified location with the `MoveForward`, `MoveBackward` functions, all tailored for both blue and red courses.
* **Adjustable Lifting:** Precisely control the robot's arm using the `lift` function, allowing for strategic gear manipulation.
* **Gyro Integration:** The algorithm seamlessly integrates with the robot's gyro sensor for accurate angle measurements and precise rotations.
* **Easy to Use:** The provided functions offer a simple and intuitive interface for controlling the robot's movement, making it accessible for both experienced and beginner programmers.

### How it Works

The algorithm leverages a combination of mathematical calculations and sensor data to determine the optimal movement path for the robot. It employs trigonometric functions to calculate the required rotation angles based on the target coordinates and the robot's current position. The gyro sensor provides real-time feedback on the robot's orientation, ensuring accurate execution of the movement commands.

### Getting Started

1. **Clone this repository:** Use `git clone https://github.com/GearManiacsJr/PositioningAlgorithm.git` to clone this repository locally.
2. **Install dependencies:** Make sure you have all the necessary libraries installed (`math`, `time`, and the libraries for `EV3`).
3. **Update configuration:** Modify the `x` and `y` variables in the `main.py` file to match your robot's starting position.
4. **Run the code:** Execute the `main.py` file to test the algorithm.

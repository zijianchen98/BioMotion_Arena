
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Initial positions of points representing a happy man sitting down
# (simplified positions for demonstration)
initial_positions = np.array([
    [0, 3],  # head
    [-1, 2], [1, 2],  # shoulders
    [-2, 1], [0, 1], [2, 1],  # upper body
    [-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0],  # sitting area
    [-1, -1], [1, -1],  # thighs
    [-1, -2], [1, -2]   # legs
])

# Create function to update the positions
def update(frame):
    # Creating a smoother "sitting down" motion
    shift = np.array([0, -0.1 * frame])  # move downwards
    positions = initial_positions + shift

    # Clear the current plot
    plt.clf()
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.gca().set_facecolor('black')  # Set background to black
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)  # Plot points

# Set up the figure and animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 30), interval=100)

# Show the animation
plt.show()

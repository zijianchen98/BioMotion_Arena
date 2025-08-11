
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
num_points = 15
frames = 100
interval = 100  # milliseconds

# Initialize position of the point lights for lying down
# Here the Y-coordinates will be simulated to lie down (horizontal movement)
y_positions = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5])
x_positions = np.linspace(-1, 1, num_points)

# Function to update the animation
def update(frame):
    plt.clf()
    plt.xlim(-2, 2)
    plt.ylim(-1.5, 1.5)
    plt.gca().set_facecolor('black')
    for i in range(num_points):
        # Create a natural oscillation effect for lying down motion
        y_move = 0.1 * np.sin(2 * np.pi * (frame / frames) + (i * np.pi / 5))
        plt.plot(x_positions[i], y_positions[i] + y_move, 'o', color='white', markersize=10)
    
# Create the figure for the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval)

# Display the animation
plt.show()

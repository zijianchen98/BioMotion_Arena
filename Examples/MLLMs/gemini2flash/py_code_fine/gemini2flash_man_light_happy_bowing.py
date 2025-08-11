
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)

# Define the initial positions of the points (standing pose)
initial_positions = np.array([
    [0, 0.9],       # Head
    [-0.1, 0.75],    # Left Shoulder
    [0.1, 0.75],     # Right Shoulder
    [-0.25, 0.6],   # Left Elbow
    [0.25, 0.6],    # Right Elbow
    [-0.1, 0.45],    # Left Hand
    [0.1, 0.45],     # Right Hand
    [-0.05, 0.6],    # Left Hip
    [0.05, 0.6],     # Right Hip
    [-0.15, 0.3],    # Left Knee
    [0.15, 0.3],     # Right Knee
    [0, 0.5],     # Center
    [-0.05, 0.1],    # Left Ankle
    [0.05, 0.1],     # Right Ankle
    [0, -0.15]      # Foot
])


# Define the animation function
def animate(i):
    # Simulate bowing motion by varying the y-coordinates
    bow_angle = np.sin(i * 0.05) * 0.4  # Adjust amplitude and frequency as needed

    # Copy initial positions
    new_positions = initial_positions.copy()

    # Apply bowing effect
    new_positions[:, 1] -= bow_angle  # Reduce all y-coordinates to simulate bowing

    # Further adjustments to mimic realistic bowing motion
    new_positions[0, 1] -= bow_angle * 0.5  # Head moves more
    new_positions[7:9, 1] -= bow_angle * 0.75
    new_positions[11,1] -= bow_angle * 0.8

    # Update the positions of the points
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True, repeat=True)

plt.show()

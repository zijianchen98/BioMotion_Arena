
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for a person sitting down
# Each row represents a point-light, with the first column being the x-coordinate and the second column being the y-coordinate
point_lights = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.7],  # Left elbow
    [0.6, 0.7],  # Right elbow
    [0.4, 0.6],  # Left wrist
    [0.6, 0.6],  # Right wrist
    [0.5, 0.5],  # Hip
    [0.4, 0.4],  # Left knee
    [0.6, 0.4],  # Right knee
    [0.4, 0.3],  # Left ankle
    [0.6, 0.3],  # Right ankle
    [0.5, 0.8],  # Chest
    [0.5, 0.7],  # Abdomen
    [0.5, 0.6]   # Lower back
])

# Define the movement of each point-light over time
# Each row represents a time frame, with each column representing a point-light's x or y coordinate
movement = np.zeros((100, 15, 2))  # 100 time frames, 15 point-lights, 2 coordinates

# Initialize the movement array with the initial point-light locations
movement[:, :, :] = point_lights

# Define the movement of each point-light over time
for i in range(100):
    # Move the head down
    movement[i, 0, 1] = 0.9 - i * 0.005
    # Move the shoulders down and in
    movement[i, 1, 1] = 0.8 - i * 0.005
    movement[i, 1, 0] = 0.4 + i * 0.002
    movement[i, 2, 1] = 0.8 - i * 0.005
    movement[i, 2, 0] = 0.6 - i * 0.002
    # Move the elbows down
    movement[i, 3, 1] = 0.7 - i * 0.005
    movement[i, 4, 1] = 0.7 - i * 0.005
    # Move the wrists down
    movement[i, 5, 1] = 0.6 - i * 0.005
    movement[i, 6, 1] = 0.6 - i * 0.005
    # Move the hip down
    movement[i, 7, 1] = 0.5 - i * 0.005
    # Move the knees down
    movement[i, 8, 1] = 0.4 - i * 0.005
    movement[i, 9, 1] = 0.4 - i * 0.005
    # Move the ankles down
    movement[i, 10, 1] = 0.3 - i * 0.005
    movement[i, 11, 1] = 0.3 - i * 0.005
    # Move the chest down
    movement[i, 12, 1] = 0.8 - i * 0.005
    # Move the abdomen down
    movement[i, 13, 1] = 0.7 - i * 0.005
    # Move the lower back down
    movement[i, 14, 1] = 0.6 - i * 0.005

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the initial point-light locations
scatter = ax.scatter(movement[0, :, 0], movement[0, :, 1], s=50, c='white')

# Set the background color to black
ax.set_facecolor('black')

# Set the limits of the plot to the size of the person
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Function to update the plot for each frame of the animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.scatter(movement[frame, :, 0], movement[frame, :, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()

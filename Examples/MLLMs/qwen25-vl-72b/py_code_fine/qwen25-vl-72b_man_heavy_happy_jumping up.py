
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a heavy man jumping up
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, -0.5], [0.5, -0.5],  # Shoulders
    [-1, -1], [0, -1], [1, -1],  # Elbows
    [-1.5, -1.5], [0, -1.5], [1.5, -1.5],  # Hands
    [-0.5, -1], [0.5, -1],  # Hips
    [-1, -2], [0, -2], [1, -2],  # Knees
    [-1.5, -2.5], [0, -2.5], [1.5, -2.5]  # Feet
])

# Function to update the positions of the points for each frame
def update(frame):
    global initial_positions
    amplitude = 0.5 * np.sin(0.1 * frame)
    new_positions = initial_positions.copy()
    new_positions[:, 1] += amplitude
    scat.set_offsets(new_positions)
    return scat,

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(0, 200), interval=50, blit=True)

plt.show()

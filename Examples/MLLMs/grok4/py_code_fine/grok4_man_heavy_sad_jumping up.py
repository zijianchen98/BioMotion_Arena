
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15  # Total number of points (light)
DURATION = 5     # Duration of the animation in seconds
FRAMES = 100     # Number of frames in the animation
HEIGHT_JUMP = 1  # Maximum height of jump
WEIGHT_DROP = 0.1  # Weight drop effect in the y-axis

# Initial positions of the points representing the sadman
initial_positions = np.array([
    [0, 2],    # Top head
    [-0.5, 1.5], [0.5, 1.5],  # Shoulders
    [-0.6, 1], [0.6, 1],      # Elbows
    [-0.4, 0.6], [0.4, 0.6],  # Hands
    [-0.4, 0], [0.4, 0],      # Hips
    [-0.3, -1], [0.3, -1],    # Knees
    [-0.2, -1.5], [0.2, -1.5], # Feet
]) + np.array([0, 0])  # Initial y-offset based on stance

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create points
points = ax.plot([], [], 'wo', markersize=8)[0]

# Animation function
def animate(frame):
    # Calculate the current height of the jump
    t = frame / FRAMES
    height = HEIGHT_JUMP * np.sin(t * np.pi) * (1 - height * WEIGHT_DROP)
    
    # Update positions to create the jumping effect
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += height
    
    points.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=FRAMES, interval=DURATION*1000/FRAMES, blit=True)

# Show the animation
plt.show()

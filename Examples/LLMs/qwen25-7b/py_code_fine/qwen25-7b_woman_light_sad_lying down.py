
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the 15 points for the sad woman lying down
points = np.array([
    [0, 50],  # Head
    [ 45, 70],  # Left shoulder
    ( 55, 75),  # Right shoulder
    ( 30, 85),  # Left hip
    ( 65, 85),  # Right hip
    ( 25, 95),  # Left knee
    ( 55, 95),  # Right knee
    ( 35, 105),  # Left ankle
    ( 65, 115),  # Right ankle
    ( 45, 125),  # Chest
    ( 55, 125),  # Lower back
    ( 35, 135),  # Left elbow
    ( 65, 135),  # Right elbow
    ( 45, 145)   # Lower abdomen
])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(-10, 110)
ax.set_ylim(-10, 145)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the plot
dots, = ax.plot([], [], 'o', color='white')

def init():
    dots.set_data([], [])
    return dots,

def update(frame):
    # Update the positions of the points
    new_points = points + frame * 2 - 1
    new_points = np.clip(new_points, 0, 110)
    dots.set_data(new_points[:, 0], new_points[:, 1])
    return dots,

# Create the animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, 15, 150), init_func=init, blit=True)

# Show the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0/14 for t in range(15) ] for r in range(3)
])

# Define the movement pattern for each point-light
def update_positions(positions):
    # Update each point-light position based on a simple sine wave motion
    new_positions = np.zeros_like(positions)
    for i in range(15):
        new_positions[0, i] = positions[0, i] + np.sin(i * 0/14 + frame / 10) / 10
        new_positions[1, i] = positions[1, i] + np.cos(i * 3 * t/14 + frame / 10) / 10
    return new_positions

# Initialize the figure and axis
fig, ax = plt.subplots()
ax ax.set_xlim(-1, 1)
ax ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the point-lights
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    global initial_positions
    positions = update_positions(initial_positions)
    points.set_data(positions[0], positions[1])
    return points,

# Create the animation
animation = FuncAnimation(fig, animate, frames=range(100), init_func=init, blit=True, interval=30)

# Show the animation
plt.show()

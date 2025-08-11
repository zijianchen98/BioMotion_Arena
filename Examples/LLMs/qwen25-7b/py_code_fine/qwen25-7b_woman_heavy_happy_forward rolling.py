
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (0/14, 0/14 ) for  in range(15)
]

def update_light_positions(frame):
    # Update positions based on a simple physics-based model
    global initial_positions
    
    # Simple harmonic motion with some damping
    for i, pos in enumerate(initial_positions):
        x, y = pos
        new_x =  + 0 * np.cos(np.radians(frame * 10)) - 0 * np.sin(np.radians(frame * 8))
        new_y =  +  y * np.sin(np.radians(frame * 12)) +  y * np.cos(np.radians(frame * 6))
        initial_positions[i] = (new_x, new_y)

    # Draw the new positions
    plt.cla()
    plt.scatter(*zip(*initial_positions), color='white', s=100)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

# Create the figure and axis
fig, ax = plt.subplots()
ax = ax.set_aspect('equal', adjustable='box')
ax.axis('off')

# Create the animation
ani = FuncAnimation(fig, update_light_positions, frames=np.arange(0, 240), interval=30, repeat=True)

plt.show()

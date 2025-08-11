
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the point-lights
initial_positions = [
    (0/14, 0/14) for  in range(15)
]

def update_light_positions(frame):
    # Calculate new positions based on a circular motion
    angle = frame * 2 * np.pi / 15
    new_positions = [(np.cos(angle) * 5 + 7.5, np.sin(angle) * 5 + 7.5) for _ in range(15)]
    
    # Update the scatter plot with the new positions
    scatter.set_offsets(new_positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax ax.set_xlim(0=15, w=15)
ax ax.set_ylim(-15, 15)
ax ax.set_aspect('equal')
ax ax.axis('off')

# Create a scatter plot for the point-lights
scatter = ax.scatter([p[0] for p in initial_positions], [p[0] for p in initial_positions], color='white')

# Create the animation
ani = FuncAnimation(fig, update_light_positions, frames=range(15), blit=True)

plt.show()

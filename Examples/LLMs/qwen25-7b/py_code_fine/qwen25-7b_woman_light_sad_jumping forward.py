
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the sad woman's lights
initial_positions = [
    (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), # Head and upper body
    (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), # Lower body
    (12, 2), (13, 2), (14, 2), (15, 2) # Legs
]

# Function to update the positions of the lights
def update_positions(frame):
    positions = []
    for x, y in initial_positions:
        # Simple harmonic motion for the head and upper body
        if 1 <= x <= 5:
            x += int(2 * np.sin((frame / 10) + (x - 3) * np.pi))
        # Linear motion for the lower body and legs
        else:
            y += int(np.sin((frame / 10) + (x - 6) * np.pi))
            if y < 2:
                y = 2
        positions.append((x, y))
    return positions

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax, y = zip(*initial_positions)
ax.plot(x, y, 'o', color='white')

# Animation function
def animate(frame):
    x, y = zip(*update_positions(frame))
    ax.clear()
    ax.plot(x, y, 'o', color='white')
    ax.set_xlim(0, 15)
    ax.set_ylim(1, 5)
    ax.axis('off()

# Set up the animation
ani = FuncAnimation(fig, animate, frames=100, interval=30)

# Show the animation
plt.show()

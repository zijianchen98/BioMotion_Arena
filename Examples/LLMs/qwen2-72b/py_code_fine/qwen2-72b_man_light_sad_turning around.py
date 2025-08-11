
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create a scatter plot for the points
scatter = ax.scatter([], [], color='white')

def update(frame):
    # Generate random initial positions for the points
    if frame == 0:
        x = np.random.uniform(-10, 10, size=15)
        y = np.random.uniform(-10, 10, size=15)
    else:
        # Update positions based on circular motion
        angle = frame * np.pi / 60
        x = 5 * np.cos(angle) + np.random.normal(0, 1, size=15)
        y = 5 * np.sin(angle) + np.random.normal(0, 1, size=15)
    
    scatter.set_offsets(np.column_stack([x, y]))
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=120, interval=50)

plt.show()

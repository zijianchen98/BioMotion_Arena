
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')  # Hide axes

# Create initial data for 15 points
num_points = 15
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Create scatter plot
scatter = ax.scatter(x, y, c='white')

def update(frame):
    global x, y
    
    # Update positions (simulate waving motion)
    x += np.sin(frame / 50) * 0.05
    y += np.cos(frame / 40) * 0.05
    
    # Keep points within bounds
    x = np.clip(x, -1, 1)
    y = np.clip(y, -1, 1)
    
    # Update scatter plot
    scatter.set_offsets(np.column_stack((x, y)))
    
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 2*np.pi, 0.1),
                    blit=True, interval=30)

plt.show()

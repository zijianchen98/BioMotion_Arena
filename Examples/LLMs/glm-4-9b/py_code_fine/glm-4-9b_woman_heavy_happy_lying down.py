
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Define the points for the happy woman with heavy weight lying down
# These points will be moved to simulate the lying down action
points, = ax.plot([], [], 'o', markersize=5, color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Define the trajectory for each point
    # This is a simplified biomechanical model to simulate lying down
    t = frame / 100
    x = np.sin(2 * np.pi * t) * 5
    y = np.cos(2 * np.pi * t) * 3 + 2 * (1 - np.exp(-t))
    
    # Define the points positions
    # 15 points distributed on the body of the woman
    body_points_x = x + np.random.normal(0, 0.5, 15)
    body_points_y = y + np.random.normal(0, 0.5, 15)
    
    points.set_data(body_points_x, body_points_y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)

plt.axis('off')
plt.show()

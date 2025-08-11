
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
n_points = 15  # number of light points
duration = 200  # frames for animation
fps = 30  # frames per second
t = np.linspace(0, 2 * np.pi, duration)

# Define the sadman with heavy weight turning around in a biomimetic way
# This is a simplified representation to demonstrate the concept
def sadman_position(t):
    # Base body movement - turning around (circle)
    theta = t
    x_circle = 2 * np.cos(theta)
    y_circle = 2 * np.sin(theta)
    
    # Add some upper body movement to mimic turning (slightly offset to upper body)
    theta_upper = t + 0.2
    x_upper = 1.5 * np.cos(theta_upper)
    y_upper = 1.5 * np.sin(theta_upper)
    
    # Combine base and upper body positions
    x = np.concatenate((x_circle, x_upper))
    y = np.concatenate((y_circle, y_upper))
    
    return x, y

# Initialize the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
scat = ax.scatter([], [], s=100, color='white')

# Update function for the animation
def update(frame):
    x, y = sadman_position(frame / 10)
    scat.set_offsets(np.column_stack((x, y)))
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=duration, blit=True, interval=1000/fps)

# Display the animation
plt.axis('off')
plt.show()

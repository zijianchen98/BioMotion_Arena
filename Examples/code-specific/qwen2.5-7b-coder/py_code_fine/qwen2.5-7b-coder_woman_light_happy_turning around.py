
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
time_steps = 100
frame_rate = 30

# Initialize the positions of the points
theta = np.linspace(0, 2 * np.pi, num_points)
x = np.cos(theta)
y = np.sin(theta)

# Create the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot for the points
scatter = ax.scatter(x, y, color='white')

# Function to update the animation at each frame
def update(frame):
    # Update the angles based on the current frame
    theta += 2 * np.pi / time_steps
    x = np.cos(theta)
    y = np.sin(theta)
    
    # Update the positions of the points
    scatter.set_offsets(np.column_stack((x, y)))
    
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()

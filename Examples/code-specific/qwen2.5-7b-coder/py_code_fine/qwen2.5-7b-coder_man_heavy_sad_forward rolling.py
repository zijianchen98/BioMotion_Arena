
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the parameters for the animation
num_points = 15
frames = 60
frame_rate = 30
weight_factor = 0.5
sadman_radius = 10

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot([], [], 'o', color='white')

# Function to update the animation at each frame
def update(frame):
    # Calculate the angle of rotation based on the frame number
    angle = 2 * np.pi * frame / frames
    
    # Calculate the positions of the points
    x = np.cos(angle + np.linspace(0, 2 * np.pi, num_points)) * 40
    y = np.sin(angle + np.linspace(0, 2 * np.pi, num_points)) * 40
    
    # Apply the weight factor to simulate the sadman's motion
    x -= np.cos(angle) * weight_factor * sadman_radius
    y -= np.sin(angle) * weight_factor * sadman_radius
    
    # Update the positions of the points
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()

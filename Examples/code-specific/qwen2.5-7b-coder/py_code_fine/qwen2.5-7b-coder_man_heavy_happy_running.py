
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 60
num_points = 15

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create point lights
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Function to update the animation
def update(frame):
    # Clear the previous frame
    points.set_data([], [])
    
    # Calculate new positions for the point lights
    angles = np.linspace(0, 2 * np.pi, num_points + 1)[:-1]
    radius = 0.8 - 0.4 * np.sin(frame / num_frames * 2 * np.pi)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    
    # Apply some noise to make it more realistic
    x += np.random.normal(0, 0.05, num_points)
    y += np.random.normal(0, 0.05, num_points)
    
    # Update the point lights
    points.set_data(x, y)
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100)

# Show the animation
plt.show()

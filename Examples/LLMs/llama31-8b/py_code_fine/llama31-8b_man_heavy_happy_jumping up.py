
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
num_points = 15
num_frames = 100
background_color = 'black'
point_color = 'white'

# Define the points' initial positions
points = np.random.rand(num_points, 2) * 2 - 1  # Randomly initialize points within a 2x2 square

# Define the points' movement
def jumping_motion(points, frame):
    # Define the movement parameters
    amplitude = 0.5
    frequency = 1.0
    phase = np.linspace(0, 2*np.pi, num_frames, endpoint=False)
    
    # Update the points' positions based on the jumping motion
    points[:, 0] = np.cos(phase[frame]) * amplitude + points[:, 0]
    points[:, 1] = np.sin(phase[frame]) * amplitude + points[:, 1]
    
    # Apply a slight random jitter to the points
    points += np.random.randn(*points.shape) * 0.01
    
    return points

# Create the figure and axis
fig, ax = plt.subplots()

# Initialize the points on the axis
for point in points:
    ax.plot(point[0], point[1], 'o', markersize=10, color=point_color)

# Set the axis limits and background color
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_facecolor(background_color)

# Animate the points
def animate(frame):
    ax.clear()
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_facecolor(background_color)
    points = jumping_motion(points, frame)
    for point in points:
        ax.plot(point[0], point[1], 'o', markersize=10, color=point_color)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=20, repeat=False)

# Show the animation
plt.show()

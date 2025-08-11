
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_points = 15
total_frames = 200
duration = 2  # Duration of each frame in seconds

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initial positions of the points (15 points in a circle)
theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
radius = 5
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Create a scatter plot for the points
points, = ax.plot(x, y, 'o', color='white', markersize=8)

def update(frame):
    # Calculate the new positions of the points to simulate bowing
    t = frame / total_frames
    bowing_angle = np.pi * t * 0.5  # Max bowing angle of 90 degrees
    new_radius = radius - 2 * np.sin(bowing_angle)
    
    # Update the x and y coordinates
    new_x = new_radius * np.cos(theta + bowing_angle)
    new_y = new_radius * np.sin(theta + bowing_angle)
    
    # Update the scatter plot
    points.set_data(new_x, new_y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=duration*1000, blit=True)

# Show the animation
plt.show()

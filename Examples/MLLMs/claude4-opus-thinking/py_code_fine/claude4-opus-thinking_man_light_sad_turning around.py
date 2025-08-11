
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
radius = 1.0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize point positions (this could represent the skeletal positions)
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    # Create a turning motion
    theta = 2 * np.pi * frame / frames  # Full rotation
    angles = np.linspace(0, np.pi, num_points)  # Points distributed in half circle
    
    # Calculate x, y coordinates for each point
    x = radius * np.sin(angles) * np.cos(theta)
    y = radius * np.sin(angles) * np.sin(theta)

    # The vertical line at the center represents the sad man's spine
    y_spine = np.linspace(-1, 1, num_points)
    x_spine = np.zeros(num_points)
    
    # Update data
    points.set_data(np.concatenate((x, x_spine)), np.concatenate((y, y_spine)))
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()

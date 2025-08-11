
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15  # Number of point lights
frames = 60      # Number of frames in the animation
theta = np.linspace(0, 2 * np.pi, num_points)

# Point-light positions (representing a human turning around)
def get_positions(frame):
    angle = (2 * np.pi * frame / frames)  # Rotation angle
    dx = np.cos(theta + angle)
    dy = np.sin(theta + angle)

    # Simulating height to define the vertical position of point lights
    height = np.linspace(-1, 1, num_points)
    
    return dx, height, dy

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation update function
def update(frame):
    dx, height, dy = get_positions(frame)
    points.set_data(dx, height)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=100)

# Show the animation
plt.show()

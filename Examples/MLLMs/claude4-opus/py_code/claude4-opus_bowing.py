
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point lights
duration = 100  # Duration of the animation in frames
bowing_angle = 30  # Simulated angle for the bowing motion

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Function to initialize the points
def init():
    points.set_data([], [])
    return points,

# Function to update the points for each frame
def update(frame):
    # Simulate the bowing motion
    bowing_factor = np.sin(frame / duration * np.pi)  # Amount of bowing
    # Define fixed points positions for limbs and head
    x = np.array([-0.2, 0, 0.2,  # Shoulder points
                  -0.1, 0, 0.1,  # Hand points
                  0, 0,          # Head point (slightly down)
                  0, 0, 0, 0,   # Body points
                  -0.1, -0.3, 0.1, -0.3])  # Feet points
    y = np.array([0.5, 0.7, 0.5,  # Shoulders
                  0.3, 0.5, 0.3,  # Hands
                  0.1 - bowing_factor * 0.2,  # Head
                  0.0, 0.15, 0.0, 0.15,  # Body
                  -0.3, -0.5, -0.3, -0.5])  # Feet
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration,
                              init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()

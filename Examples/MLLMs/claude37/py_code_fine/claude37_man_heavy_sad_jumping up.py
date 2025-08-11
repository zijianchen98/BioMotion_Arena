
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 100
weight_position = (0, -3)  # Position for the weight relative to the figure
jump_height = 2  # Maximum height of the jump
ground_level = -5  # How low the subject starts

# Generate points for the point-light representation of the sad man
def generate_points(t):
    # Base positions of lights
    y_positions = np.array([
        0, 0.5, 1, 1.5, 2.5,  # Head and upper body
        2, 1.5, 1, 0.5,      # Arms
        0, -1, -1.5, -2,     # Legs
        -1, -2, -3           # Lower body
    ])
    
    # Calculate vertical position based on a simple jump trajectory
    jump_y = jump_height * np.sin(t * np.pi / (frames / 2))
    
    # Adjust positions to create the jump effect
    return y_positions + ground_level + jump_y

# Setup the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White points

# Initiation function for the animation
def init():
    points.set_data([], [])
    return points,

# Update function for the animation
def update(frame):
    y_data = generate_points(frame)
    x_data = np.zeros(num_points)  # x-coordinates are fixed (0 for vertical jump)
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init,
                              blit=True, interval=50)

# Show the animation
plt.show()

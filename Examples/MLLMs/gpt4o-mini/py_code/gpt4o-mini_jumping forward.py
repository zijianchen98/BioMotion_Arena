
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

# Initial positions of point lights representing body joints
# These values represent a man in jumping forward pose
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Elbows
    [-0.75, -0.5], [0.75, -0.5],  # Hands
    [-0.5, -1],[0.5, -1],  # Hips
    [-0.75, -1.5], [0.75, -1.5],  # Knees
    [-0.5, -2], [0.5, -2],  # Feet
    [0, -3],  # Lower body center
    [0, -2.5]  # Upper body center
])

# Function to initialize the plot
def init():
    point_lights.set_data([], [])
    return point_lights,

# Function to update the animation
def update(frame):
    # Define the jump motion
    jump_height = 3 * np.sin(np.pi * frame / 20)  # Simulate jump height
    forward_distance = frame / 10  # Forward movement
    updated_positions = initial_positions + [forward_distance, jump_height]
    point_lights.set_data(updated_positions[:, 0], updated_positions[:, 1])
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init,
                              blit=True, interval=50, repeat=True)

# Show the animation
plt.show()

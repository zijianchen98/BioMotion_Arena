
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15 # Total number of point-lights
frames = 60     # Number of frames in the animation

# Initialize point-light positions (15 points for the body and arms)
# The positions are based on a simple schematic representation of a person’s body
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.8], [0.5, 0.8],  # Shoulders
    [-0.5, 0.6], [0.5, 0.6],  # Elbows
    [-0.5, 0.4], [0.5, 0.4],  # Wrists
    [-0.2, 0.6], [0.2, 0.6],   # Hips
    [-0.3, 0.2], [0.3, 0.2],   # Knees
    [-0.5, 0], [0.5, 0],       # Feet
])

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize points
def init():
    points.set_data([], [])
    return points,

# Update function for animation
def update(frame):
    # Wave motion parameters
    arm_angle = np.sin(frame * 0.1) * np.pi / 4  # Waving arm
    wave_y_offset = 0.1 * np.sin(frame * 0.1)    # Up and down motion

    # Modify the arm positions for waving
    body = initial_positions.copy()
    body[3:5, 0] += np.sin(arm_angle) * 0.5        # Left wave
    body[6:8, 0] += np.cos(arm_angle) * 0.5        # Right wave
    body[1:3, 1] += wave_y_offset                   # Up and down movement

    # Set new data for the points
    points.set_data(body[:, 0], body[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=20)

# Display animation
plt.show()

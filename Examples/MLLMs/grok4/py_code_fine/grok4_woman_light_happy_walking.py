
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15  # Number of points
FPS = 30  # Frames per second
DURATION = 2  # Duration in seconds

# Generate initial positions for the point lights
# Example positions: Potentially these could represent joints of a walking figure
initial_positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5],  # Shoulder Left
    [0.5, 0.5],  # Shoulder Right
    [-0.5, 0],  # Elbow Left
    [0.5, 0],  # Elbow Right
    [-0.5, -0.5],  # Hip Left
    [0.5, -0.5],  # Hip Right
    [-0.5, -1],  # Knee Left
    [0.5, -1],  # Knee Right
    [-0.5, -1.5],  # Ankle Left
    [0.5, -1.5],  # Ankle Right
    [0, 0.5],  # Wrist Left
    [0, 0],  # Wrist Right
    [-0.5, -0.5],  # Foot Left
    [0.5, -0.5],  # Foot Right
])

# Walk motion generator
def walking_motion(frame):
    # Simple transformation to simulate walking
    step_length = 0.05
    x_offset = np.sin(frame * np.pi / (FPS / 2)) * step_length  # Side-to-side motion
    new_positions = initial_positions.copy()

    # Update positions for walking
    new_positions[:, 0] += x_offset
    new_positions[:, 1] += frame * 0.05 / FPS  # Forward motion

    return new_positions

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)

# Initialize function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    new_positions = walking_motion(frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(FPS * DURATION), init_func=init,
                              blit=True, interval=1000/FPS)

# Show the animation
plt.show()

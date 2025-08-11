
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
num_frames = 100

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8)  # white points

# Initialize point positions for the "happy woman"
# Create a simple structure for the points (e.g., head, arms, legs)
initial_positions = np.array([[0, 1],  # head
                             [-0.5, 0.5], [0.5, 0.5],  # arms
                             [-0.5, 0], [0.5, 0],  # torso
                             [-0.7, -0.5], [0.7, -0.5],  # legs
                             [-0.5, -1], [0.5, -1], [0, -1.5]])  # lower points

# Forward roll motion
def forward_roll(t):
    # Using a sine wave to simulate rolling
    angle = 2 * np.pi * (t / num_frames)
    offset_y = np.sin(angle) * 0.5  # rolling effect on y-axis
    offset_x = np.cos(angle) * 0.5  # slight side roll
    
    # New positions for the points
    return initial_positions + np.array([offset_x, offset_y])

# Animation update function
def update(frame):
    new_positions = forward_roll(frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()

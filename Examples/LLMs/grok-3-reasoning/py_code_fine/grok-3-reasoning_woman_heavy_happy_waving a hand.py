
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define base positions of the 15 points
base_positions = [
    (0, 9),    # head
    (0, 8),    # neck
    (-1, 8),   # left shoulder
    (1, 8),    # right shoulder
    (-1.5, 7), # left elbow
    (1.5, 7),  # right elbow
    (-2, 6),   # left wrist
    (2, 6),    # right wrist
    (0, 5),    # waist
    (-0.5, 4), # left hip
    (0.5, 4),  # right hip
    (-0.5, 2), # left knee
    (0.5, 2),  # right knee
    (-0.5, 0), # left ankle
    (0.5, 0)   # right ankle
]

# Parameters for motion
f = 0.5          # waving frequency in Hz
f_bounce = 1.0   # bouncing frequency in Hz
A_bounce = 0.5   # bouncing amplitude

# Set up the figure and axis with black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 10)

# Initial scatter plot for the points
x0 = [p[0] for p in base_positions]
y0 = [p[1] for p in base_positions]
scatter = ax.scatter(x0, y0, color='white', s=20)

# Update function for animation
def update(t):
    u = (1 - np.cos(2 * np.pi * f * t)) / 2
    y_elbow = 7 + (8.5 - 7) * u
    y_wrist = 6 + (9 - 6) * u
    bounce = A_bounce * np.sin(2 * np.pi * f_bounce * t)
    pos = []
    for i in range(15):
        if i == 5:  # right elbow
            pos.append((base_positions[5][0], y_elbow + bounce))
        elif i == 7:  # right wrist
            pos.append((base_positions[7][0], y_wrist + bounce))
        else:
            pos.append((base_positions[i][0], base_positions[i][1] + bounce))
    x = [p[0] for p in pos]
    y = [p[1] for p in pos]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 200), interval=50, blit=True)

plt.show()

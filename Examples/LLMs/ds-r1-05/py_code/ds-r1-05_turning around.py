
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define initial positions of 15 points relative to the pelvis (x, y, z)
points = np.array([
    [0, 0.8, 0],     # head
    [0, 0.6, 0],     # neck
    [-0.3, 0.5, 0],  # left shoulder
    [-0.5, 0.3, 0],  # left elbow
    [-0.7, 0.1, 0],  # left hand
    [0.3, 0.5, 0],   # right shoulder
    [0.5, 0.3, 0],   # right elbow
    [0.7, 0.1, 0],   # right hand
    [0, 0, 0],       # pelvis (root)
    [-0.2, 0, 0],    # left hip
    [0.2, 0, 0],     # right hip
    [-0.2, -0.5, 0], # left knee
    [0.2, -0.5, 0],  # right knee
    [-0.2, -1, 0],   # left foot
    [0.2, -1, 0]     # right foot
])

total_points = 15  # Total number of points

# Set up the figure and axis
fig = plt.figure(figsize=(6, 6), facecolor='black')
ax = fig.add_subplot(111, aspect='equal', xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), facecolor='black')
ax.set_axis_off()

# Create a scatter plot for the points
scatter = ax.scatter([], [], c='white', s=40)  # White points, size 40

# Animation parameters
T = 5.0  # Seconds for one full rotation
walk_frequency = 2  # Steps per second
pelvic_amp = 0.05   # Pelvic oscillation amplitude
foot_lift_amp = 0.2 # Foot lift amplitude

def animate(t):
    # Compute rotation angle in radians
    theta = math.radians(360 * (t / T))
    
    # Pelvic vertical oscillation
    pelvic_offset = pelvic_amp * math.sin(2 * math.pi * walk_frequency * t)
    phase = (walk_frequency * t) % 1  # For foot lifting phase

    # Initialize array for current positions
    current_positions = np.zeros((total_points, 3))
    for i in range(total_points):
        x0, y0, z0 = points[i]
        # Apply rotation around Y-axis
        x_rot = x0 * math.cos(theta) - z0 * math.sin(theta)
        z_rot = x0 * math.sin(theta) + z0 * math.cos(theta)
        y_new = y0 + pelvic_offset
        current_positions[i] = [x_rot, y_new, z_rot]

    # Apply foot lifting
    if phase < 0.5:
        left_lift = foot_lift_amp * math.sin(math.pi * phase * 2)
        current_positions[13, 1] += left_lift  # Lift left foot
    else:
        right_lift = foot_lift_amp * math.sin(math.pi * (phase - 0.5) * 2)
        current_positions[14, 1] += right_lift  # Lift right foot

    # Extract x and y for plotting
    data = np.zeros((15, 2))
    data[:, 0] = current_positions[:, 0]  # X coordinates
    data[:, 1] = current_positions[:, 1]  # Y coordinates
    
    scatter.set_offsets(data)
    return scatter,

# Create animation
anim = FuncAnimation(fig, animate, frames=np.linspace(0, T, 300), interval=40, blit=True)
plt.show()

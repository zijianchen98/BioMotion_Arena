
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights
NUM_LIGHTS = 15

# Define the skeleton structure for a bowing motion (simplified)
# Each light represents a joint or a body part
# Positions are relative to the center of the body
# We'll use a simplified 2D skeleton with 15 points

# Initial positions (centered at (0, 0))
initial_positions = np.array([
    [0, 0],        # Hip
    [0.5, -0.5],   # Knee
    [0.5, -1.0],   # Ankle
    [0.5, -1.5],   # Foot
    [-0.5, -0.5],  # Knee
    [-0.5, -1.0],  # Ankle
    [-0.5, -1.5],  # Foot
    [0, -2.0],     # Pelvis
    [0.7, -1.5],   # Shoulder
    [0.7, -2.0],   # Elbow
    [0.7, -2.5],   # Wrist
    [0.7, -3.0],   # Hand
    [-0.7, -1.5],  # Shoulder
    [-0.7, -2.0],  # Elbow
    [-0.7, -2.5],  # Wrist
    [-0.7, -3.0],  # Hand
])

# Define the motion path for bowing (simplified)
# Each light will move along a sine wave path with different amplitudes and phases
def motion_function(t, idx):
    # Amplitude and phase for each light
    amplitude = np.array([
        0.1, 0.15, 0.2, 0.25, 0.1, 0.15, 0.2, 0.25,
        0.1, 0.15, 0.2, 0.25, 0.1, 0.15, 0.2
    ])
    phase = np.linspace(0, 2 * np.pi, NUM_LIGHTS)
    return initial_positions[idx] + amplitude[idx] * np.sin(2 * np.pi * t + phase[idx])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Create circles for point lights
points = [ax.scatter([], [], color='white', s=50) for _ in range(NUM_LIGHTS)]

# Function to update the animation
def update(frame):
    for i in range(NUM_LIGHTS):
        x, y = motion_function(frame / 100, i)  # Normalize time to 0-1
        points[i].set_offsets([[x, y]])

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Show the animation
plt.show()

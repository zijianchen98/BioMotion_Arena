
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 points representing the body parts
# These are approximate positions of body joints during a forward roll
body_points = np.array([
    [0.0, 0.0],        # Head
    [0.1, 0.2],        # Neck
    [0.2, 0.3],        # Shoulder
    [0.3, 0.4],        # Elbow
    [0.4, 0.5],        # Wrist
    [0.5, 0.6],        # Hand
    [-0.2, 0.3],       # Shoulder
    [-0.3, 0.4],       # Elbow
    [-0.4, 0.5],       # Wrist
    [-0.5, 0.6],       # Hand
    [0.0, 0.8],        # Hip
    [0.1, 0.7],        # Knee
    [0.2, 0.6],        # Ankle
    [0.3, 0.5],        # Foot
    [-0.1, 0.7],       # Knee
    [-0.2, 0.6],       # Ankle
    [-0.3, 0.5],       # Foot
])

# Normalize to the plot limits
body_points = body_points / 2.0

# Create circles for each point-light
circles = [ax.add_patch(patches.Circle((body_points[i][0], body_points[i][1]), 0.02, color='white', zorder=5)) for i in range(15)]

# Define the forward roll motion function
def forward_roll(t):
    # Define a simple forward roll motion using sine waves for natural movement
    # We'll animate the body parts using a combination of sine and cosine functions
    # This is a simplified biomechanical model for demonstration purposes

    # Define the motion parameters
    amplitude = 0.2
    frequency = 0.1
    phase = 0.5 * t

    # Create a copy of the original positions
    positions = body_points.copy()

    # Apply motion to the head, shoulders, hips, and feet
    positions[0] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[1] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[2] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[3] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[4] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[5] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[6] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[7] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[8] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[9] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[10] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[11] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[12] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[13] += amplitude * np.sin(2 * np.pi * frequency * t + phase)
    positions[14] += amplitude * np.sin(2 * np.pi * frequency * t + phase)

    # Apply some phase shift to the lower body
    positions[10] += amplitude * np.sin(2 * np.pi * frequency * t + phase + np.pi / 2)
    positions[11] += amplitude * np.sin(2 * np.pi * frequency * t + phase + np.pi / 2)
    positions[12] += amplitude * np.sin(2 * np.pi * frequency * t + phase + np.pi / 2)
    positions[13] += amplitude * np.sin(2 * np.pi * frequency * t + phase + np.pi / 2)

    return positions

# Animation function
def animate(t):
    positions = forward_roll(t)
    for i, circle in enumerate(circles):
        circle.set_center((positions[i][0], positions[i][1]))

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()

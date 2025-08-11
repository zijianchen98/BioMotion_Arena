
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights and the action
NUM_LIGHTS = 15
ACTION = "walking"
BACKGROUND_COLOR = "black"
LIGHT_COLOR = "white"

# Define the positions of the body parts for a sad man with heavy weight
# Simplified as a skeleton with 15 points representing joints and weight
# Positions are relative to the center of the body
body_parts = {
    "head": (0, 1.5),
    "neck": (0, 1.0),
    "shoulder_left": (-0.5, 0.5),
    "elbow_left": (-0.8, 0.2),
    "wrist_left": (-1.0, 0.0),
    "hand_left": (-1.2, -0.2),
    "shoulder_right": (0.5, 0.5),
    "elbow_right": (0.8, 0.2),
    "wrist_right": (1.0, 0.0),
    "hand_right": (1.2, -0.2),
    "hip_left": (-0.5, -0.5),
    "knee_left": (-0.8, -0.8),
    "ankle_left": (-1.0, -1.0),
    "foot_left": (-1.2, -1.2),
    "hip_right": (0.5, -0.5),
    "knee_right": (0.8, -0.8),
    "ankle_right": (1.0, -1.0),
    "foot_right": (1.2, -1.2),
    "weight": (0, -2.0)
}

# Select 15 body parts to represent the point lights
point_light_positions = [
    body_parts["head"],
    body_parts["neck"],
    body_parts["shoulder_left"],
    body_parts["elbow_left"],
    body_parts["wrist_left"],
    body_parts["hand_left"],
    body_parts["shoulder_right"],
    body_parts["elbow_right"],
    body_parts["wrist_right"],
    body_parts["hand_right"],
    body_parts["hip_left"],
    body_parts["knee_left"],
    body_parts["ankle_left"],
    body_parts["foot_left"],
    body_parts["weight"]
]

# Define a function to simulate the walking motion
def walk(t):
    # Define a simple sinusoidal motion for the legs and arms
    # Add some phase shifts to simulate natural movement
    phase = t * 0.5
    positions = []
    for part in point_light_positions:
        x, y = part
        if "foot" in part or "ankle" in part or "knee" in part or "hip" in part:
            # Legs: up and down motion
            y += 0.5 * np.sin(2 * np.pi * t + np.pi / 2)
        elif "hand" in part or "wrist" in part or "elbow" in part or "shoulder" in part:
            # Arms: up and down motion
            y += 0.5 * np.sin(2 * np.pi * t + np.pi / 2 + np.pi)
        elif "head" in part or "neck" in part:
            # Head and neck: slight up and down motion
            y += 0.2 * np.sin(2 * np.pi * t + np.pi / 2 + np.pi * 2)
        elif "weight" in part:
            # Weight: slight vertical oscillation
            y += 0.3 * np.sin(2 * np.pi * t + np.pi / 2 + np.pi * 3)
        positions.append((x, y))
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axis('off')

# Create circles for the point lights
point_lights = [Circle((0, 0), 0.05, color=LIGHT_COLOR) for _ in range(NUM_LIGHTS)]
for light in point_lights:
    ax.add_patch(light)

# Function to update the animation
def update(frame):
    positions = walk(frame)
    for i, light in enumerate(point_lights):
        light.center = positions[i]
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

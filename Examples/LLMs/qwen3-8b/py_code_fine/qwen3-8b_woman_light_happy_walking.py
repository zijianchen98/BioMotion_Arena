
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Define the number of point lights
num_points = 15

# Define the body parts and their positions (simplified for a walking human)
# Each body part will have a position (x, y) and a radius
body_parts = [
    # Head
    {"name": "head", "position": np.array([0.0, 1.5]), "radius": 0.1},
    # Torso
    {"name": "torso", "position": np.array([0.0, 0.5]), "radius": 0.1},
    # Left shoulder
    {"name": "left_shoulder", "position": np.array([-0.5, 0.5]), "radius": 0.1},
    # Right shoulder
    {"name": "right_shoulder", "position": np.array([0.5, 0.5]), "radius": 0.1},
    # Left hip
    {"name": "left_hip", "position": np.array([-0.5, -0.5]), "radius": 0.1},
    # Right hip
    {"name": "right_hip", "position": np.array([0.5, -0.5]), "radius": 0.1},
    # Left knee
    {"name": "left_knee", "position": np.array([-0.5, -1.0]), "radius": 0.1},
    # Right knee
    {"name": "right_knee", "position": np.array([0.5, -1.0]), "radius": 0.1},
    # Left ankle
    {"name": "left_ankle", "position": np.array([-0.5, -1.5]), "radius": 0.1},
    # Right ankle
    {"name": "right_ankle", "position": np.array([0.5, -1.5]), "radius": 0.1},
    # Left hand
    {"name": "left_hand", "position": np.array([-0.8, 0.8]), "radius": 0.1},
    # Right hand
    {"name": "right_hand", "position": np.array([0.8, 0.8]), "radius": 0.1},
    # Left foot
    {"name": "left_foot", "position": np.array([-0.8, -1.3]), "radius": 0.1},
    # Right foot
    {"name": "right_foot", "position": np.array([0.8, -1.3]), "radius": 0.1},
    # Pelvis
    {"name": "pelvis", "position": np.array([0.0, -0.5]), "radius": 0.1}
]

# Create a list of point light positions
point_light_positions = [part["position"] for part in body_parts]

# Define a function to update the positions of the point lights
def update(frame):
    # Simulate a walking motion using a sine wave for periodic movement
    # Each point light has a different phase to simulate natural movement
    for i, part in enumerate(body_parts):
        # Define the amplitude and frequency for each body part
        amplitude = 0.2
        frequency = 0.05
        phase = i * 0.3  # Different phase for each point light

        # Calculate the vertical displacement based on sine wave
        displacement = amplitude * np.sin(frequency * frame + phase)

        # Update the position of the point light
        part["position"][1] += displacement

        # Limit the vertical movement to simulate realistic walking
        part["position"][1] = np.clip(part["position"][1], -1.5, 1.5)

    # Update the point light positions
    for i, point in enumerate(point_light_positions):
        point[1] = body_parts[i]["position"][1]

    # Update the scatter plot
    for i, point in enumerate(scatter_points):
        point.set_offsets([body_parts[i]["position"][0], body_parts[i]["position"][1]])

    return scatter_points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_facecolor("black")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.axis("off")

# Create scatter points for the point lights
scatter_points = [ax.scatter([], [], color="white", s=100) for _ in range(num_points)]

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

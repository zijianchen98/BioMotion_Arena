
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of point lights
num_points = 15

# Define the body parts and their positions (simplified for a sad woman in forward roll)
body_parts = {
    'head': np.array([0, 0.5]),
    'neck': np.array([0, 0.4]),
    'shoulder_left': np.array([-0.2, 0.2]),
    'elbow_left': np.array([-0.4, 0.0]),
    'wrist_left': np.array([-0.5, -0.1]),
    'hand_left': np.array([-0.5, -0.25]),
    'shoulder_right': np.array([0.2, 0.2]),
    'elbow_right': np.array([0.4, 0.0]),
    'wrist_right': np.array([0.5, -0.1]),
    'hand_right': np.array([0.5, -0.25]),
    'hip': np.array([0, -0.5]),
    'knee_left': np.array([-0.2, -0.8]),
    'ankle_left': np.array([-0.3, -1.0]),
    'foot_left': np.array([-0.3, -1.15]),
    'knee_right': np.array([0.2, -0.8]),
    'ankle_right': np.array([0.3, -1.0]),
    'foot_right': np.array([0.3, -1.15]),
}

# Define a function to simulate motion (forward roll)
def simulate_motion(t):
    # Simulate forward roll with rotation and translation
    # We will use sine and cosine to simulate circular motion
    angle = t * 0.1  # angular speed
    radius = 0.3
    center = np.array([0, -0.7])

    # Apply rotation and translation to each body part
    positions = {}
    for part, pos in body_parts.items():
        rotated = np.array([
            radius * np.cos(angle) + pos[0],
            radius * np.sin(angle) + pos[1]
        ])
        positions[part] = rotated + center

    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Create circles for point lights
points = [Circle((0, 0), 0.02, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Initialize positions
positions = simulate_motion(0)
point_positions = [positions[part] for part in body_parts.values()]

# Update function for animation
def update(frame):
    positions = simulate_motion(frame)
    for i, point in enumerate(points):
        point.set_center(point_positions[i])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()

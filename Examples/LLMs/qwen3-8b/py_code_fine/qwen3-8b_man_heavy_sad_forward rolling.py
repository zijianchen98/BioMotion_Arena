
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions (body joints)
# Positions are based on a simplified human body with 15 joints
# These positions are relative to a central point (e.g., the pelvis)
# We'll animate them to simulate a forward rolling motion

# Initial positions (approximate body joint coordinates)
initial_positions = np.array([
    [0.0, 0.0],    # pelvis
    [0.0, 0.3],    # waist
    [0.0, 0.6],    # torso
    [0.3, 0.8],    # right shoulder
    [0.3, 1.1],    # right elbow
    [0.1, 1.3],    # right wrist
    [-0.3, 1.1],   # left shoulder
    [-0.3, 0.8],   # left elbow
    [-0.1, 0.6],   # left wrist
    [0.2, 0.3],    # right hip
    [0.2, 0.0],    # right knee
    [0.2, -0.3],   # right ankle
    [-0.2, 0.0],   # left hip
    [-0.2, -0.3],  # left knee
    [-0.2, -0.6],  # left ankle
])

# Create the point-light circles
points = [Circle((x, y), 0.02, color='white') for x, y in initial_positions]
for point in points:
    ax.add_patch(point)

# Define the motion parameters for a forward rolling motion
# We'll simulate a rolling motion by rotating and translating the body
# over time, simulating a forward roll with a slight twist

def animate(frame):
    # Time parameter
    t = frame / 50.0  # Normalize time to 0-1

    # Define a rolling motion with rotation and translation
    angle = np.sin(t * 2 * np.pi) * 0.5  # Oscillating rotation
    translation = np.array([np.sin(t * 2 * np.pi * 2), np.cos(t * 2 * np.pi * 2)]) * 0.4  # Forward roll

    # Apply rotation and translation to each point
    for i, point in enumerate(points):
        # Apply rotation
        x, y = initial_positions[i]
        rotated = np.array([x * np.cos(angle) - y * np.sin(angle),
                            x * np.sin(angle) + y * np.cos(angle)])
        # Apply translation
        new_pos = rotated + translation
        point.center = new_pos

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()

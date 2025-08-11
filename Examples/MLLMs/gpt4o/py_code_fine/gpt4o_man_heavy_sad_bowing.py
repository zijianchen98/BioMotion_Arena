
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up animation parameters
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

# Generate initial positions for the 15 points representing the sadman
# These positions are biomechanically plausible and represent the head, torso, arms, and legs.
points = np.array([
    [0, 1.5],   # Head
    [0, 1.2],   # Neck
    [-0.2, 0.9], [0.2, 0.9],  # Shoulders
    [-0.5, 0.6], [0.5, 0.6],  # Elbows
    [-0.8, 0.3], [0.8, 0.3],  # Hands
    [0, 0.6],   # Mid-torso
    [-0.3, 0.3], [0.3, 0.3],  # Hips
    [-0.5, -0.4], [0.5, -0.4], # Knees
    [-0.7, -1], [0.7, -1]     # Feet
])

scat = ax.scatter(points[:, 0], points[:, 1], color="white")

# Define motion for bowing movement
def bowing_motion(frame_number):
    """Animate the sadman bowing."""
    global points
    
    # Bowing motion parameters
    bow_degree = np.sin(frame_number * 0.1) * 0.3  # Oscillate bowing angle
    torso_y_shift = np.sin(frame_number * 0.1) * 0.1  # Slight vertical motion (bending)

    # Apply bowing motion to relevant body parts (head, neck, torso)
    points[0, 1] = 1.5 + torso_y_shift  # Head moves slightly downward/upward
    points[1, 1] = 1.2 + torso_y_shift  # Neck follows head
    points[8, 1] = 0.6 - torso_y_shift  # Mid-torso

    # Rotate head and neck point around the torso (simulate bowing)
    torso_origin = points[8]
    for i in [0, 1]:  # Head and neck points
        dx, dy = points[i, 0] - torso_origin[0], points[i, 1] - torso_origin[1]
        angle = np.arctan2(dy, dx) - bow_degree
        radius = np.sqrt(dx**2 + dy**2)
        points[i, 0] = torso_origin[0] + radius * np.cos(angle)
        points[i, 1] = torso_origin[1] + radius * np.sin(angle)

    scat.set_offsets(points)
    return scat,

# Create animation
animation_func = animation.FuncAnimation(fig, bowing_motion, frames=100, interval=50, blit=True)

# Display animation
plt.show()

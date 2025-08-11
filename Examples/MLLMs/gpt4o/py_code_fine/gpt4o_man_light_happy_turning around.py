
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 points representing a simplified "stick figure".
# These points represent the body parts (e.g., head, shoulders, arms, legs, etc.)
# of a human figure. The points are connected to form the skeleton structure.
# Note: The coordinates and figure are normalized for a basic stick figure.
happyman_points = np.array([
    [0, 5],   # Head
    [-1, 4],  # Left shoulder
    [1, 4],   # Right shoulder
    [-1, 3],  # Left elbow
    [1, 3],   # Right elbow
    [-1, 2],  # Left wrist
    [1, 2],   # Right wrist
    [0, 3],   # Spine top
    [0, 2],   # Spine mid
    [0, 1],   # Spine base
    [-1, 0],  # Left hip
    [1, 0],   # Right hip
    [-1, -1], # Left knee
    [1, -1],  # Right knee
    [-1, -2], # Left ankle
    [1, -2],  # Right ankle
])

# Define connections between points to draw the skeleton.
connections = [
    (0, 1), (0, 2), # Head to shoulders
    (1, 3), (3, 5), # Left shoulder to left wrist
    (2, 4), (4, 6), # Right shoulder to right wrist
    (1, 7), (2, 7), # Shoulders to spine top
    (7, 8), (8, 9), # Spine top to spine base
    (9, 10), (9, 11), # Spine base to hips
    (10, 12), (12, 14), # Left hip to left ankle
    (11, 13), (13, 15)  # Right hip to right ankle
]

# Animation initialization and parameters.
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_facecolor('black')
points, = plt.plot([], [], 'wo', markersize=6)  # White point-lights for the animation
lines = [plt.plot([], [], 'w-')[0] for _ in connections]

# Function to rotate the points around the Y-axis to simulate turning motion.
def rotate_y(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)],
    ])
    points_3d = np.hstack([points, np.zeros((points.shape[0], 1))])  # Add z-dimension
    rotated_points = points_3d @ rotation_matrix.T
    return rotated_points[:, :2]  # Project back to 2D (x, y)

# Animation initialization function.
def init():
    points.set_data([], [])
    for line in lines:
        line.set_data([], [])
    return [points] + lines

# Animation updating function.
def update(frame):
    angle = np.radians(frame)  # Convert frame number to angle in radians
    rotated_points = rotate_y(happyman_points, angle)

    # Update point positions
    points.set_data(rotated_points[:, 0], rotated_points[:, 1])

    # Update connections
    for i, (start, end) in enumerate(connections):
        line_x = [rotated_points[start, 0], rotated_points[end, 0]]
        line_y = [rotated_points[start, 1], rotated_points[end, 1]]
        lines[i].set_data(line_x, line_y)

    return [points] + lines

# Create the animation object.
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=True, interval=50
)

# Display the animation.
plt.axis('off')  # Remove axes for clean animation on black background.
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Define the number of points and the action
NUM_POINTS = 15
ACTION = "sitting down"
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'
FPS = 30
DURATION = 5  # seconds

# Define the joints and their indices for a human body (simplified)
JOINTS = [
    ('hip', 0), ('left_knee', 1), ('left_ankle', 2),
    ('right_knee', 3), ('right_ankle', 4),
    ('spine', 5), ('torso', 6), ('neck', 7),
    ('left_shoulder', 8), ('left_elbow', 9), ('left_hand', 10),
    ('right_shoulder', 11), ('right_elbow', 12), ('right_hand', 13),
    ('head', 14)
]

# Define the positions of the joints for a person sitting down
def get_joint_positions(t):
    # Normalize time to [0, 1]
    t_norm = t / DURATION
    # Define a simple motion path for sitting down
    # We will simulate a smooth transition from standing to sitting
    # For simplicity, we use a sine wave to simulate smooth motion
    # Define positions for each joint over time
    positions = np.zeros((NUM_POINTS, 2))

    # Hip movement (downwards)
    positions[0, 1] = 100 * (1 - np.sin(np.pi * t_norm))
    # Left knee (bending)
    positions[1, 1] = 100 * (1 - 0.5 * np.sin(np.pi * t_norm))
    # Left ankle (moving down)
    positions[2, 1] = 100 * (1 - 0.75 * np.sin(np.pi * t_norm))
    # Right knee (bending)
    positions[3, 1] = 100 * (1 - 0.5 * np.sin(np.pi * t_norm))
    # Right ankle (moving down)
    positions[4, 1] = 100 * (1 - 0.75 * np.sin(np.pi * t_norm))
    # Spine (lowering)
    positions[5, 1] = 100 * (1 - 0.9 * np.sin(np.pi * t_norm))
    # Torso (lowering)
    positions[6, 1] = 100 * (1 - 0.95 * np.sin(np.pi * t_norm))
    # Neck (lowering)
    positions[7, 1] = 100 * (1 - 0.97 * np.sin(np.pi * t_norm))
    # Left shoulder (lowering)
    positions[8, 1] = 100 * (1 - 0.98 * np.sin(np.pi * t_norm))
    # Left elbow (bending)
    positions[9, 1] = 100 * (1 - 0.95 * np.sin(np.pi * t_norm))
    # Left hand (moving down)
    positions[10, 1] = 100 * (1 - 0.99 * np.sin(np.pi * t_norm))
    # Right shoulder (lowering)
    positions[11, 1] = 100 * (1 - 0.98 * np.sin(np.pi * t_norm))
    # Right elbow (bending)
    positions[12, 1] = 100 * (1 - 0.95 * np.sin(np.pi * t_norm))
    # Right hand (moving down)
    positions[13, 1] = 100 * (1 - 0.99 * np.sin(np.pi * t_norm))
    # Head (lowering)
    positions[14, 1] = 100 * (1 - 0.995 * np.sin(np.pi * t_norm))

    # X positions for a more natural pose
    positions[:, 0] = np.array([
        0, -30, -60, -30, -60, 0, 30, 60, 30, 60, 90, 60, 90, 120, 90
    ])

    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor(BACKGROUND_COLOR)
ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
points = [Circle((0, 0), 5, color=POINT_COLOR) for _ in range(NUM_POINTS)]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(t):
    positions = get_joint_positions(t)
    for i, point in enumerate(points):
        point.center = positions[i]

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(FPS * DURATION), interval=1000 / FPS, blit=False)

# Show the animation
plt.show()

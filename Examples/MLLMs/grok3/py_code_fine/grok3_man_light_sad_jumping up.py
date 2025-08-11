
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define 15 point-light positions for a human figure (head, torso, limbs)
# Initial positions for a standing sadman posture
points = np.array([
    [0, 0.8],    # Head
    [0, 0.5],    # Torso top
    [0, 0.2],    # Torso bottom
    [-0.2, 0.5], # Left shoulder
    [0.2, 0.5],  # Right shoulder
    [-0.3, 0.2], # Left hip
    [0.3, 0.2],  # Right hip
    [-0.4, 0],   # Left knee
    [0.4, 0],    # Right knee
    [-0.5, -0.3],# Left ankle
    [0.5, -0.3], # Right ankle
    [-0.1, 0.5], # Left elbow
    [0.1, 0.5],  # Right elbow
    [-0.2, 0.2], # Left wrist
    [0.2, 0.2]   # Right wrist
])

# Scatter plot for point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Animation function to simulate jumping motion
def update(frame):
    t = frame * 0.1  # Time parameter for smooth motion
    # Jumping motion: vertical oscillation with slight forward lean
    height = 0.2 * np.sin(t)  # Jump height
    lean = 0.1 * np.sin(t)    # Forward lean
    
    # Update positions with biomechanical constraints
    new_points = points.copy()
    new_points[0, 1] += height  # Head
    new_points[1:3, 1] += height * 0.8  # Torso
    new_points[3:5, 0] += lean * 0.5  # Shoulders
    new_points[3:5, 1] += height * 0.7  # Shoulders
    new_points[6:8, 0] += lean * 0.3  # Hips
    new_points[6:8, 1] += height * 0.5  # Hips
    new_points[8:10, 0] += lean * 0.2  # Knees
    new_points[8:10, 1] += height * 0.3  # Knees
    new_points[10:12, 1] += height * 0.1  # Ankles
    new_points[12:14, 0] += lean * 0.4  # Elbows
    new_points[12:14, 1] += height * 0.6  # Elbows
    new_points[14:, 0] += lean * 0.5  # Wrists
    new_points[14:, 1] += height * 0.5  # Wrists
    
    scatter.set_offsets(new_points)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()

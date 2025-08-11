
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'
FRAME_RATE = 30
DURATION = 5  # seconds

# Skeleton points configuration (simplified model)
skeleton_points = np.array([
    [0, 0],   # Hip
    [1, 0],   # Left Hip
    [1, 1],   # Left Knee
    [1, 2],   # Left Ankle
    [-1, 0],  # Right Hip
    [-1, 1],  # Right Knee
    [-1, 2],  # Right Ankle
    [0, -1],  # Shoulder
    [1, -1],  # Left Shoulder
    [1, -2],  # Left Elbow
    [1, -3],  # Left Wrist
    [-1, -1], # Right Shoulder
    [-1, -2], # Right Elbow
    [-1, -3], # Right Wrist
    [0, -2],  # Head
])

# Generate a rotation matrix
def rotation_matrix(angle):
    return np.array([[math.cos(angle), -math.sin(angle)],
                     [math.sin(angle), math.cos(angle)]])

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor(BACKGROUND_COLOR)
dots, = ax.plot([], [], 'o', color=POINT_COLOR)

# Update function for animation
def update(frame):
    # Calculate the rotation angle
    angle = 2 * math.pi * (frame / FRAME_RATE) / DURATION

    # Apply rotation
    rotated_points = np.dot(skeleton_points, rotation_matrix(angle))
    
    # Extract x and y coordinates
    x = rotated_points[:, 0]
    y = rotated_points[:, 1]
    
    # Update plot data
    dots.set_data(x, y)
    return dots,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=FRAME_RATE * DURATION, interval=1000 / FRAME_RATE, blit=True)

# Display plot
plt.axis('off')
plt.show()

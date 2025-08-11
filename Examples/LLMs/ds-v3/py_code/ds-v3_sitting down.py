
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Define the number of point-lights and frames
num_points = 15
num_frames = 60  # Number of frames for the animation

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
plt.axis('off')

# Initialize point-lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for sitting motion (simplified)
def get_position(frame, point_idx):
    t = frame / num_frames  # Normalized time [0, 1]
    
    # Define key positions for each point-light
    # This is a simplified model; real data would be more complex
    if point_idx == 0:  # Head
        x = 0.0
        y = 1.0 - 0.7 * t
    elif point_idx == 1:  # Neck
        x = 0.0
        y = 0.8 - 0.6 * t
    elif point_idx in [2, 3]:  # Shoulders
        x = (-0.2 if point_idx == 2 else 0.2)
        y = 0.7 - 0.5 * t
    elif point_idx in [4, 5]:  # Elbows
        x = (-0.3 if point_idx == 4 else 0.3)
        y = 0.5 - 0.4 * t
    elif point_idx in [6, 7]:  # Hands
        x = (-0.4 if point_idx == 6 else 0.4)
        y = 0.3 - 0.2 * t
    elif point_idx == 8:  # Torso (middle)
        x = 0.0
        y = 0.5 - 0.5 * t
    elif point_idx in [9, 10]:  # Hips
        x = (-0.15 if point_idx == 9 else 0.15)
        y = 0.3 - 0.3 * t
    elif point_idx in [11, 12]:  # Knees
        x = (-0.15 if point_idx == 11 else 0.15)
        y = 0.1 - 0.1 * t
    elif point_idx in [13, 14]:  # Feet
        x = (-0.2 if point_idx == 13 else 0.2)
        y = 0.0
    
    return x, y

# Update function for animation
def update(frame):
    for i, point in enumerate(points):
        x, y = get_position(frame, i)
        point.center = (x, y)
    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.tight_layout()
plt.show()

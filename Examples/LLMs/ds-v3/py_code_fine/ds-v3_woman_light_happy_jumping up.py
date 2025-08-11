
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
frames = 60
fps = 30

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for a jumping motion (simplified)
def get_position(t, point_idx):
    # t is in [0, 1], representing the jump cycle
    # point_idx is the index of the point (0-14)
    
    # Key body parts: head, shoulders, elbows, hands, hips, knees, feet
    # Simplified motion: up and down with some limb movement
    
    # Vertical motion (entire body jumps)
    jump_height = 1.5 * np.sin(np.pi * t)  # Sinusoidal jump
    
    # Horizontal positions (relative to center)
    if point_idx == 0:  # Head
        x = 0
        y = 0.8 + jump_height
    elif point_idx in [1, 2]:  # Shoulders
        x = -0.2 + 0.4 * (point_idx - 1)
        y = 0.5 + jump_height
    elif point_idx in [3, 4]:  # Elbows
        x = -0.3 + 0.6 * (point_idx - 3)
        y = 0.3 + jump_height + 0.1 * np.sin(2 * np.pi * t)
    elif point_idx in [5, 6]:  # Hands
        x = -0.4 + 0.8 * (point_idx - 5)
        y = 0.1 + jump_height + 0.2 * np.sin(2 * np.pi * t)
    elif point_idx in [7, 8]:  # Hips
        x = -0.15 + 0.3 * (point_idx - 7)
        y = 0.2 + jump_height
    elif point_idx in [9, 10]:  # Knees
        x = -0.2 + 0.4 * (point_idx - 9)
        y = -0.1 + jump_height + 0.1 * np.sin(2 * np.pi * t + np.pi/4)
    elif point_idx in [11, 12]:  # Feet
        x = -0.25 + 0.5 * (point_idx - 11)
        y = -0.4 + jump_height + 0.2 * np.sin(2 * np.pi * t + np.pi/2)
    elif point_idx in [13, 14]:  # Extra points for more natural motion (e.g., torso)
        x = -0.1 + 0.2 * (point_idx - 13)
        y = 0.35 + jump_height
    
    return x, y

# Animation update function
def update(frame):
    t = frame / frames
    for i, point in enumerate(points):
        x, y = get_position(t, i)
        point.center = (x, y)
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()

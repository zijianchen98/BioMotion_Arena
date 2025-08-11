
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse
import math

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights with initial positions (lying down position)
points = np.zeros((num_points, 2))

# Approximate positions for a person lying down (x, y)
# Head, shoulders, elbows, hands, hips, knees, feet
points[0] = [0, 0.8]    # Head
points[1] = [-0.2, 0.6]  # Left shoulder
points[2] = [0.2, 0.6]   # Right shoulder
points[3] = [-0.4, 0.4]  # Left elbow
points[4] = [0.4, 0.4]   # Right elbow
points[5] = [-0.6, 0.2]  # Left hand
points[6] = [0.6, 0.2]   # Right hand
points[7] = [-0.2, 0.2]  # Left hip
points[8] = [0.2, 0.2]   # Right hip
points[9] = [-0.3, -0.2] # Left knee
points[10] = [0.3, -0.2] # Right knee
points[11] = [-0.3, -0.6] # Left foot
points[12] = [0.3, -0.6]  # Right foot
points[13] = [0, 0.4]     # Torso middle
points[14] = [0, 0]       # Lower torso

# Create scatter plot for the point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white', s=50)

# Function to simulate slight movement (breathing and slight limb adjustments)
def update(frame):
    t = frame * 0.1
    
    # Breathing effect (vertical movement for torso points)
    breathing = 0.02 * math.sin(t * 2)
    
    # Slight movements for limbs
    for i in range(num_points):
        if i in [0]:  # Head
            points[i, 1] = 0.8 + 0.01 * math.sin(t * 1.5)
        elif i in [1, 2]:  # Shoulders
            points[i, 0] += 0.01 * math.sin(t * 1.2 + i)
            points[i, 1] = 0.6 + breathing * 0.5
        elif i in [3, 4]:  # Elbows
            points[i, 0] += 0.01 * math.sin(t * 1.3 + i)
            points[i, 1] = 0.4 + breathing * 0.3
        elif i in [5, 6]:  # Hands
            points[i, 0] += 0.01 * math.sin(t * 1.4 + i)
            points[i, 1] = 0.2 + breathing * 0.2
        elif i in [7, 8]:  # Hips
            points[i, 0] += 0.01 * math.sin(t * 1.1 + i)
            points[i, 1] = 0.2 + breathing * 0.4
        elif i in [9, 10]:  # Knees
            points[i, 0] += 0.01 * math.sin(t * 1.2 + i)
            points[i, 1] = -0.2 + breathing * 0.1
        elif i in [11, 12]:  # Feet
            points[i, 0] += 0.01 * math.sin(t * 1.3 + i)
            points[i, 1] = -0.6 + breathing * 0.05
        elif i in [13]:  # Torso middle
            points[i, 1] = 0.4 + breathing
        elif i in [14]:  # Lower torso
            points[i, 1] = 0 + breathing * 0.8
    
    # Update scatter plot
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.tight_layout()
plt.show()

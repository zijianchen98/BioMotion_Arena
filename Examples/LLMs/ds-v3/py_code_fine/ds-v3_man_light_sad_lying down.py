
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initial positions of the point-lights (lying down position)
# Approximate positions for a person lying down (x, y)
# Head, shoulders, elbows, hands, hips, knees, feet
initial_positions = np.array([
    [0.0, 0.8],    # head
    [0.0, 0.6],    # neck
    [-0.2, 0.5],   # left shoulder
    [0.2, 0.5],    # right shoulder
    [-0.3, 0.4],   # left elbow
    [0.3, 0.4],    # right elbow
    [-0.4, 0.3],   # left hand
    [0.4, 0.3],    # right hand
    [-0.2, 0.2],   # left hip
    [0.2, 0.2],    # right hip
    [-0.2, 0.0],   # left knee
    [0.2, 0.0],    # right knee
    [-0.2, -0.2],  # left foot
    [0.2, -0.2],   # right foot
    [0.0, 0.4]     # torso midpoint
])

points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'wo', markersize=8)

# Function to simulate slight movement (breathing or slight adjustment)
def update(frame):
    # Slight vertical movement for breathing effect
    breathing = 0.02 * np.sin(frame * 0.1)
    
    # Slight limb movement
    limb_movement = 0.03 * np.sin(frame * 0.2)
    
    new_positions = initial_positions.copy()
    
    # Apply vertical breathing to torso and head
    new_positions[0:2, 1] += breathing  # head and neck
    new_positions[-1, 1] += breathing   # torso midpoint
    
    # Apply slight limb movement
    new_positions[2:8, 0] += limb_movement * np.array([1, -1, 1, -1, 1, -1])  # arms
    new_positions[8:, 0] += limb_movement * np.array([1, -1, 1, -1, 1, -1])   # legs
    
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.title('Point-Light Animation: Lying Down', color='white')
plt.tight_layout()
plt.show()

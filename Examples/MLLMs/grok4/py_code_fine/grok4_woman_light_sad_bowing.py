
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FRAMES = 100
POINT_RADIUS = 50  # Size of the points
BACKGROUND_COLOR = 'black'
POINT_COLOR = 'white'

# Initialize figure
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(-100, 100)
ax.set_ylim(-170, 10)
ax.axis('off')  # Hide axes

# Point positions for a sad woman bowing (approximate model)
def generate_bowing_motion(frame):
    # Base positions for the 15 points (head, torso, arms, legs)
    points = np.array([
        [0, 0],    # Head
        [0, -20],  # Neck
        [20, -40], # Right shoulder
        [-20, -40],# Left shoulder
        [20, -80], # Right elbow
        [-20, -80],# Left elbow
        [20, -100],# Right wrist
        [-20, -100],# Left wrist
        [40, -120], # Right hip
        [-40, -120],# Left hip
        [40, -160], # Right knee
        [-40, -160],# Left knee
        [40, -180], # Right ankle
        [-40, -180],# Left ankle
        [0, -140],  # Spine center
        [0, -160]   # Center under bow
    ])
    
    # Modifying vertical positions to create a bowing motion
    bow_amount = np.clip(np.sin(frame / 10) * 10, 0, 10)
    points += np.array([0, -bow_amount])
    
    return points

# Animation function
def update(frame):
    ax.clear()
    ax.set_xlim(-100, 100)
    ax.set_ylim(-170, 10)
    ax.axis('off')
    
    points = generate_bowing_motion(frame)
    
    for i in range(NUM_POINTS):
        ax.scatter(points[i, 0], points[i, 1], s=POINT_RADIUS, color=POINT_COLOR)
    
# Create animation
ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=50)

# Show animation
plt.show()

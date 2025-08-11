
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 3  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points
points = np.zeros((NUM_POINTS, 2))
scat = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Function to update the position of points
def update(frame):
    t = frame / FPS
    
    # Define the motion for each point
    # These equations are simplified and may need adjustments for more realism
    points[0] = [0, -0.8 + 0.1 * np.sin(t)]  # Head
    points[1] = [-0.05, -0.7 + 0.05 * np.cos(2 * t)]  # Left eye
    points[2] = [0.05, -0.7 + 0.05 * np.cos(2 * t)]  # Right eye
    points[3] = [0, -0.65]  # Nose
    points[4] = [0, -0.6]  # Mouth
    points[5] = [-0.1, -0.5 + 0.05 * np.sin(t)]  # Left shoulder
    points[6] = [0.1, -0.5 + 0.05 * np.sin(t)]  # Right shoulder
    points[7] = [-0.2, -0.3 + 0.1 * np.sin(t)]  # Left elbow
    points[8] = [0.2, -0.3 + 0.1 * np.sin(t)]  # Right elbow
    points[9] = [-0.3, -0.1 + 0.2 * np.sin(t)]  # Left wrist
    points[10] = [0.3, -0.1 + 0.2 * np.sin(t)]  # Right wrist
    points[11] = [0, -0.4 + 0.3 * np.sin(t)]  # Chest
    points[12] = [-0.1, -0.7 + 0.3 * np.sin(t)]  # Left hip
    points[13] = [0.1, -0.7 + 0.3 * np.sin(t)]  # Right hip
    points[14] = [0, -0.9 + 0.5 * np.sin(t)]  # Bottom
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

plt.show()

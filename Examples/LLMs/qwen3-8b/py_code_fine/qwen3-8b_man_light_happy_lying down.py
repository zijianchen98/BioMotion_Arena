
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 body joints (simplified human skeleton)
# Coordinates are relative to the body center
body_joints = np.array([
    [0, 0],          # Hip center
    [0.3, 0],        # Right hip
    [0.6, 0.1],      # Right knee
    [0.4, 0.3],      # Right ankle
    [-0.3, 0],       # Left hip
    [-0.6, 0],       # Left knee
    [-0.4, 0.3],     # Left ankle
    [0, 0.3],        # Spine
    [0, 0.6],        # Chest
    [0.1, 0.7],      # Right shoulder
    [0.3, 0.5],      # Right elbow
    [0.1, 0.3],      # Right wrist
    [-0.1, 0.7],     # Left shoulder
    [-0.3, 0.5],     # Left elbow
    [-0.1, 0.3],     # Left wrist
])

# Normalize coordinates to fit within the plot
body_joints = body_joints / 2

# Create point lights
lights = [Circle((0, 0), 0.02, color='white') for _ in range(15)]
for light in lights:
    ax.add_patch(light)

# Define a function to simulate realistic motion (simplified)
def animate(frame):
    # Simulate a lying down motion
    # Use sine waves to create smooth, natural movement
    # Scale down the motion for realism
    motion = 0.1 * np.sin(2 * np.pi * frame / 100)
    for i, joint in enumerate(body_joints):
        x = joint[0] + motion * np.sin(2 * np.pi * frame / 100 + i * 0.5)
        y = joint[1] + motion * np.sin(2 * np.pi * frame / 100 + i * 0.3)
        lights[i].center = (x, y)

# Animate the stimulus
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

plt.show()

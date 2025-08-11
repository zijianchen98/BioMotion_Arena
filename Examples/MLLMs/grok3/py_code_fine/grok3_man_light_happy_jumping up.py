
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a "happy man" jumping
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-3, 6], [3, 6],  # elbows
    [-4, 4], [4, 4],  # wrists
    [-1, 2], [1, 2],  # hips
    [-1.5, 0], [1.5, 0],  # knees
    [-2, -2], [2, -2],  # ankles
    [0, 6], [0, 4], [0, 2]  # torso (3 points)
]) * 10  # Scale up for visibility

# Number of frames for one jump cycle
frames = 60
positions = np.zeros((frames, 15, 2))

# Simulate jumping motion (up and down with slight arm/leg swing)
for i in range(frames):
    t = i / frames * 2 * np.pi  # Cycle through one period
    height = 50 * np.sin(t) + 50  # Jump height (0 to 100 and back)
    leg_angle = 0.5 * np.sin(t)  # Leg swing
    arm_angle = 0.3 * np.sin(t + np.pi/2)  # Arm swing opposite to legs
    
    # Update positions based on biomechanical plausibility
    pos = initial_positions.copy()
    pos[:, 1] += height  # Vertical jump motion
    pos[6:8, 0] += 15 * np.sin(leg_angle)  # Knees swing
    pos[8:10, 0] += 15 * np.sin(leg_angle)  # Ankles swing
    pos[4:6, 0] += 10 * np.sin(arm_angle)  # Wrists swing
    pos[2:4, 0] += 10 * np.sin(arm_angle)  # Elbows swing
    positions[i] = pos

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-100, 100)
ax.set_ylim(-50, 150)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Define the initial positions of 15 point-lights (simplified human figure)
# Positions represent key joints: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-4, 6], [4, 6],  # elbows
    [-6, 4], [6, 4],  # wrists
    [0, 0],  # pelvis
    [-2, -2], [2, -2],  # hips
    [-3, -4], [3, -4],  # knees
    [-4, -6], [4, -6]   # ankles
])

# Number of frames for the animation (e.g., 60 frames for a smooth bowing cycle)
n_frames = 60

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update positions for each frame (simulating bowing motion)
def update(frame):
    # Parameterize bowing motion with a sine wave for smooth transition
    angle = np.pi * frame / n_frames  # Bowing angle increases over time
    bend = 0.5 * np.sin(angle)  # Depth of bowing (0 to 0.5 units)
    
    # Updated positions for bowing: head, arms, and legs move downward and forward
    positions = initial_positions.copy()
    positions[0, 1] -= bend * 8  # Head moves down
    positions[1:5, 1] -= bend * 6  # Upper body
    positions[5:7, 1] -= bend * 4  # Pelvis and hips
    positions[7:, 1] -= bend * 2  # Legs
    
    # Adjust forward lean
    lean = bend * 2
    positions[0:5, 0] += lean * 0.5  # Head and arms lean forward
    positions[5:, 0] += lean * 0.3   # Lower body leans less
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

# Save or display the animation
plt.show()
# To save: ani.save('bowing_animation.mp4', writer='ffmpeg')


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a running sadman (simplified biomechanical model)
# Positions represent key joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10],  # head
    [-1, 8], [-1, 6],  # left shoulder, elbow
    [-2, 4],  # left wrist
    [1, 8], [1, 6],   # right shoulder, elbow
    [2, 4],   # right wrist
    [0, 5],   # torso
    [-1, 3], [-1, 1],  # left hip, knee
    [-2, -1], # left ankle
    [1, 3], [1, 1],    # right hip, knee
    [2, -1]    # right ankle
]) * 10  # Scale for visibility

# Parameters for animation
frames = 100
fps = 20
dt = 1 / fps

# Function to update positions for realistic running motion
def update(frame):
    global initial_positions
    positions = initial_positions.copy()
    
    # Sinusoidal motion for legs and arms to simulate running
    t = frame * dt
    leg_phase = np.sin(2 * np.pi * t)
    arm_phase = np.cos(2 * np.pi * t)
    
    # Update leg positions
    positions[8, 1] = initial_positions[8, 1] + 20 * leg_phase  # left knee
    positions[9, 1] = initial_positions[9, 1] + 30 * leg_phase  # left ankle
    positions[10, 1] = initial_positions[10, 1] - 20 * leg_phase  # right knee
    positions[11, 1] = initial_positions[11, 1] - 30 * leg_phase  # right ankle
    
    # Update arm positions
    positions[2, 1] = initial_positions[2, 1] + 15 * arm_phase  # left elbow
    positions[3, 1] = initial_positions[3, 1] + 20 * arm_phase  # left wrist
    positions[4, 1] = initial_positions[4, 1] - 15 * arm_phase  # right elbow
    positions[5, 1] = initial_positions[5, 1] - 20 * arm_phase  # right wrist
    
    # Slight torso and head movement
    positions[0, 1] = initial_positions[0, 1] + 5 * np.sin(0.5 * np.pi * t)  # head
    positions[6, 1] = initial_positions[6, 1] + 3 * np.sin(0.5 * np.pi * t)  # torso
    
    # Forward motion
    positions[:, 0] += 5 * t  # Move rightward to simulate running
    
    scat.set_offsets(positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor('black')
ax.set_xlim(-50, 150)
ax.set_ylim(-50, 50)
ax.axis('off')

# Plot the point-lights
scat = ax.scatter([], [], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

plt.show()

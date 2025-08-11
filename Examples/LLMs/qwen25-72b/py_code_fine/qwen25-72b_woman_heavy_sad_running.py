
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the point-lights for the running woman
# These positions are simplified and should be adjusted for more realism
initial_positions = np.array([
    [0, 0],  # Head
    [0, -1],  # Neck
    [-1, -2],  # Left Shoulder
    [1, -2],  # Right Shoulder
    [-2, -4],  # Left Elbow
    [2, -4],  # Right Elbow
    [-3, -6],  # Left Hand
    [3, -6],  # Right Hand
    [0, -2],  # Spine
    [-1, -4],  # Left Hip
    [1, -4],  # Right Hip
    [-2, -6],  # Left Knee
    [2, -6],  # Right Knee
    [-3, -8],  # Left Foot
    [3, -8]   # Right Foot
])

# Function to update the positions of the point-lights
def update_positions(frame):
    # Adjust the positions for a running motion
    phase = frame / 10.0  # Frame rate adjustment
    positions = initial_positions.copy()
    
    # Head bobbing
    positions[0, 1] += 0.5 * np.sin(phase)
    
    # Arm swinging
    arm_swing = 0.5 * np.sin(phase)
    positions[4, 1] += arm_swing
    positions[5, 1] -= arm_swing
    positions[6, 1] += 2 * arm_swing
    positions[7, 1] -= 2 * arm_swing
    
    # Leg movement
    leg_swing = 0.5 * np.sin(phase + np.pi)
    positions[11, 1] += leg_swing
    positions[12, 1] -= leg_swing
    positions[13, 1] += 2 * leg_swing
    positions[14, 1] -= 2 * leg_swing
    
    # Body lean
    body_lean = 0.2 * np.sin(phase)
    positions[:, 0] += body_lean
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, color='white')

# Initialization function
def init():
    scat.set_offsets([])
    return scat,

# Animation update function
def animate(frame):
    positions = update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Show the animation
plt.show()

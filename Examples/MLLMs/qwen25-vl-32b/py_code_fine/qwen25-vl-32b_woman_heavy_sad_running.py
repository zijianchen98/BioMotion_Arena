
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (joints)
# These points represent:
# 0-Head, 1-Neck, 2-Spine, 3-Hips, 4-R Shoulder, 5-L Shoulder,
# 6-R Elbow, 7-L Elbow, 8-R Hand, 9-L Hand, 10-R Knee, 11-L Knee,
# 12-R Ankle, 13-L Ankle, 14-R Toe, 15-L Toe
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.5], # Neck
    [0, 0],   # Spine
    [0, -0.5],# Hips
    [-0.5, 0],# R Shoulder
    [0.5, 0], # L Shoulder
    [-0.7, -0.5],# R Elbow
    [0.7, -0.5],# L Elbow
    [-0.9, -1],# R Hand
    [0.9, -1], # L Hand
    [-0.5, -1.5],# R Knee
    [0.5, -1.5],# L Knee
    [-0.5, -2],# R Ankle
    [0.5, -2], # L Ankle
    [-0.5, -2.5],# R Toe
    [0.5, -2.5] # L Toe
])

# Function to update the positions for running motion
def update_positions(frame, positions):
    # Define the phase of the running cycle (0 to 1)
    phase = frame / 50.0  # 50 frames per cycle
    
    # Adjust the head position to show sadness (slightly tilted down)
    positions[0][1] = 1 + 0.1 * np.sin(2 * np.pi * phase) - 0.2
    
    # Adjust the spine position to show slouching
    positions[2][1] = 0 + 0.1 * np.sin(2 * np.pi * phase) - 0.2
    
    # Adjust the hip position to show heaviness
    positions[3][1] = -0.5 + 0.1 * np.sin(2 * np.pi * phase) - 0.2
    
    # Adjust the leg positions for running
    right_leg_phase = phase
    left_leg_phase = phase + 0.5  # Opposite phase for the other leg
    
    # Right leg
    positions[10][1] = -1.5 + 0.3 * np.sin(2 * np.pi * right_leg_phase)  # Knee
    positions[12][1] = -2 + 0.3 * np.sin(2 * np.pi * right_leg_phase)    # Ankle
    positions[14][1] = -2.5 + 0.3 * np.sin(2 * np.pi * right_leg_phase)  # Toe
    
    # Left leg
    positions[11][1] = -1.5 + 0.3 * np.sin(2 * np.pi * left_leg_phase)   # Knee
    positions[13][1] = -2 + 0.3 * np.sin(2 * np.pi * left_leg_phase)     # Ankle
    positions[15][1] = -2.5 + 0.3 * np.sin(2 * np.pi * left_leg_phase)   # Toe
    
    # Adjust arm positions for running (opposite phase to legs)
    right_arm_phase = phase + 0.5
    left_arm_phase = phase
    
    # Right arm
    positions[6][0] = -0.7 + 0.2 * np.cos(2 * np.pi * right_arm_phase)  # Elbow
    positions[8][0] = -0.9 + 0.2 * np.cos(2 * np.pi * right_arm_phase)  # Hand
    
    # Left arm
    positions[7][0] = 0.7 + 0.2 * np.cos(2 * np.pi * left_arm_phase)    # Elbow
    positions[9][0] = 0.9 + 0.2 * np.cos(2 * np.pi * left_arm_phase)    # Hand
    
    return positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 2)
ax.axis('off')  # Hide axes for a cleaner look
points = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    global initial_positions
    updated_positions = update_positions(frame, initial_positions.copy())
    points.set_offsets(updated_positions)
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()

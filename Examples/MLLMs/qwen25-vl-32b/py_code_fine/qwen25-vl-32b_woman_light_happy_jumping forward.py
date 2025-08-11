
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent:
# 0-Head, 1-Neck, 2-Spine, 3-Pelvis
# 4-R Shoulder, 5-L Shoulder, 6-R Elbow, 7-L Elbow, 8-R Hand, 9-L Hand
# 10-R Hip, 11-L Hip, 12-R Knee, 13-L Knee, 14-R Foot, 15-L Foot
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.8], # Neck
    [0, 0.6], # Spine
    [0, 0.4], # Pelvis
    [-0.3, 0.8], # R Shoulder
    [0.3, 0.8],  # L Shoulder
    [-0.5, 0.5], # R Elbow
    [0.5, 0.5],  # L Elbow
    [-0.7, 0.3], # R Hand
    [0.7, 0.3],  # L Hand
    [-0.3, 0.4], # R Hip
    [0.3, 0.4],  # L Hip
    [-0.5, 0.1], # R Knee
    [0.5, 0.1],  # L Knee
    [-0.7, -0.2], # R Foot
    [0.7, -0.2]   # L Foot
])

# Define the amplitude and frequency for the jump motion
amplitude = 0.3
frequency = 0.1

# Function to update the positions based on time
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Apply vertical oscillation for the jump
    vertical_offset = amplitude * np.sin(2 * np.pi * frequency * frame / num_frames)
    
    # Adjust head, neck, spine, pelvis, shoulders, hips, and hands
    positions[0:10, 1] += vertical_offset
    
    # Adjust knees and feet for landing
    if frame < num_frames // 2:
        # Rising phase: Knees bend, feet stay behind
        knee_bend = 0.2 * np.sin(2 * np.pi * frequency * frame / (num_frames // 2))
        foot_lift = 0.2 * np.sin(2 * np.pi * frequency * frame / (num_frames // 2))
        positions[12:16, 1] += vertical_offset + knee_bend
        positions[14:16, 1] += vertical_offset + foot_lift
    else:
        # Landing phase: Knees extend, feet move forward
        knee_extension = 0.2 * np.cos(2 * np.pi * frequency * (frame - num_frames // 2) / (num_frames // 2))
        foot_forward = 0.2 * np.cos(2 * np.pi * frequency * (frame - num_frames // 2) / (num_frames // 2))
        positions[12:16, 1] += vertical_offset + knee_extension
        positions[14:16, 0] += foot_forward  # Move feet forward horizontally
        positions[14:16, 1] += vertical_offset  # Keep feet at ground level
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def update(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()

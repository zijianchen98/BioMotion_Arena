
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the point-lights
# These coordinates are approximate and will be adjusted to simulate running
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left Shoulder
    [2, 8],  # Right Shoulder
    [-4, 6],  # Left Elbow
    [4, 6],  # Right Elbow
    [-6, 4],  # Left Wrist
    [6, 4],  # Right Wrist
    [-1, 6],  # Left Hip
    [1, 6],  # Right Hip
    [-3, 2],  # Left Knee
    [3, 2],  # Right Knee
    [-4, 0],  # Left Ankle
    [4, 0],  # Right Ankle
    [0, 4],   # Torso 1
    [0, 2]    # Torso 2
])

# Function to generate the animation data for each frame
def generate_frame(frame_num):
    # Adjust the positions of the point-lights to simulate running
    positions = initial_positions.copy()
    
    # Head bobs slightly
    positions[0, 1] += np.sin(frame_num * 0.1) * 0.2
    
    # Shoulders swing
    positions[1, 0] += np.sin(frame_num * 0.1 + np.pi/2) * 0.5
    positions[2, 0] += np.sin(frame_num * 0.1 - np.pi/2) * 0.5
    
    # Elbows follow shoulders
    positions[3, 0] += np.sin(frame_num * 0.1 + np.pi/2) * 0.5
    positions[4, 0] += np.sin(frame_num * 0.1 - np.pi/2) * 0.5
    
    # Hips sway slightly
    positions[7, 0] += np.sin(frame_num * 0.1 - np.pi/4) * 0.3
    positions[8, 0] += np.sin(frame_num * 0.1 + np.pi/4) * 0.3
    
    # Knees and ankles move in opposite directions
    positions[9, 1] += np.sin(frame_num * 0.2) * 0.7  # Left knee
    positions[11, 1] -= np.sin(frame_num * 0.2) * 0.7 # Left ankle
    
    positions[10, 1] -= np.sin(frame_num * 0.2) * 0.7 # Right knee
    positions[12, 1] += np.sin(frame_num * 0.2) * 0.7 # Right ankle
    
    # Slight forward movement
    positions[:, 0] += frame_num * 0.01  # Move slightly forward
    
    return positions

# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(-8, 8)
ax.set_ylim(-2, 12)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20)

# Animation function to update the positions of the point-lights in each frame
def animate(frame_num):
    positions = generate_frame(frame_num)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()

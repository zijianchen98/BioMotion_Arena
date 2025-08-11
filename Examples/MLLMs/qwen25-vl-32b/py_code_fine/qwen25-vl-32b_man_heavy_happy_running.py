
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These positions represent the limbs and body parts of the "happyman"
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.75],
    'right_elbow': [1, 0.75],
    'left_hand': [-1.5, 0.5],
    'right_hand': [1.5, 0.5],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5]
}

# Convert the dictionary to a list of coordinates
positions = np.array(list(initial_positions.values()))

# Define the animation parameters
num_frames = 100  # Number of frames in the animation
frame_rate = 30   # Frames per second
amplitude = 0.5   # Amplitude of the running motion
frequency = 0.1   # Frequency of the running motion

# Function to update the positions based on time
def update_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Normalize time to [0, 2π]

    # Update the positions for running motion
    updated_positions = positions.copy()
    
    # Head bobs up and down
    updated_positions[0][1] += amplitude * np.sin(t)
    
    # Torso sways side to side
    updated_positions[1][0] += amplitude * np.cos(t)
    
    # Left arm swings forward and backward
    updated_positions[2][0] -= amplitude * np.sin(t)  # Shoulder
    updated_positions[4][0] -= amplitude * np.sin(t)  # Elbow
    updated_positions[6][0] -= amplitude * np.sin(t)  # Hand
    
    # Right arm swings opposite to the left arm
    updated_positions[3][0] += amplitude * np.sin(t)  # Shoulder
    updated_positions[5][0] += amplitude * np.sin(t)  # Elbow
    updated_positions[7][0] += amplitude * np.sin(t)  # Hand
    
    # Left leg moves forward and backward
    updated_positions[8][0] -= amplitude * np.sin(t + np.pi / 2)  # Hip
    updated_positions[10][0] -= amplitude * np.sin(t + np.pi / 2)  # Knee
    updated_positions[12][0] -= amplitude * np.sin(t + np.pi / 2)  # Foot
    
    # Right leg moves opposite to the left leg
    updated_positions[9][0] += amplitude * np.sin(t + np.pi / 2)  # Hip
    updated_positions[11][0] += amplitude * np.sin(t + np.pi / 2)  # Knee
    updated_positions[13][0] += amplitude * np.sin(t + np.pi / 2)  # Foot
    
    return updated_positions

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    updated_positions = update_positions(frame)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, animate, frames=num_frames, interval=1000 / frame_rate, blit=True)

# Display the animation
plt.show()

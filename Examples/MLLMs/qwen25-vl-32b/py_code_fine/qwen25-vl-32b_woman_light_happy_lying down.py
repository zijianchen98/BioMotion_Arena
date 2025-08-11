
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are relative and can be adjusted for better visualization
initial_positions = {
    'head': [0, 0],
    'torso_top': [0, -1],
    'torso_bottom': [0, -2],
    'left_shoulder': [-0.5, -1],
    'right_shoulder': [0.5, -1],
    'left_elbow': [-1, -1.5],
    'right_elbow': [1, -1.5],
    'left_wrist': [-1.5, -2],
    'right_wrist': [1.5, -2],
    'left_hip': [-0.5, -2.5],
    'right_hip': [0.5, -2.5],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the animation parameters
num_frames = 100  # Number of frames in the animation
frame_rate = 30   # Frames per second

# Function to update the positions of the points for each frame
def update_points(frame):
    # Define the oscillation amplitude and frequency
    amplitude = 0.2
    frequency = 0.1
    
    # Apply sinusoidal motion to simulate lying down and subtle movements
    # Head remains relatively stable
    head_motion = np.zeros(2)
    
    # Torso sways slightly
    torso_motion = amplitude * np.sin(frequency * frame * 2 * np.pi) * np.array([0, -1])
    
    # Shoulders move subtly up and down
    shoulder_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 4) * np.array([0, -1])
    
    # Elbows and wrists move in a coordinated manner
    elbow_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 2) * np.array([0, -1])
    wrist_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 4) * np.array([0, -1])
    
    # Hips remain relatively stable but sway slightly
    hip_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 6) * np.array([0, -1])
    
    # Knees and ankles move in a coordinated manner
    knee_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 3) * np.array([0, -1])
    ankle_motion = amplitude * np.sin(frequency * frame * 2 * np.pi + np.pi / 6) * np.array([0, -1])
    
    # Combine all motions
    updated_coords = initial_coords.copy()
    updated_coords[0] += head_motion  # Head
    updated_coords[1] += torso_motion  # Torso top
    updated_coords[2] += torso_motion  # Torso bottom
    updated_coords[3] += shoulder_motion  # Left shoulder
    updated_coords[4] += shoulder_motion  # Right shoulder
    updated_coords[5] += elbow_motion  # Left elbow
    updated_coords[6] += elbow_motion  # Right elbow
    updated_coords[7] += wrist_motion  # Left wrist
    updated_coords[8] += wrist_motion  # Right wrist
    updated_coords[9] += hip_motion  # Left hip
    updated_coords[10] += hip_motion  # Right hip
    updated_coords[11] += knee_motion  # Left knee
    updated_coords[12] += knee_motion  # Right knee
    updated_coords[13] += ankle_motion  # Left ankle
    updated_coords[14] += ankle_motion  # Right ankle
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def animate(frame):
    updated_coords = update_points(frame)
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=num_frames,
    interval=1000 / frame_rate,  # Convert frame rate to milliseconds
    blit=True
)

# Display the animation
plt.show()

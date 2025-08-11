
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames for the animation
num_frames = 100
fps = 25  # Frames per second

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1.5],
    'left_shoulder': [-0.5, 1],
    'right_shoulder': [0.5, 1],
    'left_elbow': [-1, 0.5],
    'right_elbow': [1, 0.5],
    'left_wrist': [-1.5, 0],
    'right_wrist': [1.5, 0],
    'left_hip': [-0.5, 0],
    'right_hip': [0.5, 0],
    'left_knee': [-1, -0.5],
    'right_knee': [1, -0.5],
    'left_ankle': [-1.5, -1],
    'right_ankle': [1.5, -1],
}

# Convert to a list of (x, y) tuples
initial_points = [
    initial_positions['head'],
    initial_positions['left_shoulder'],
    initial_positions['right_shoulder'],
    initial_positions['left_elbow'],
    initial_positions['right_elbow'],
    initial_positions['left_wrist'],
    initial_positions['right_wrist'],
    initial_positions['left_hip'],
    initial_positions['right_hip'],
    initial_positions['left_knee'],
    initial_positions['right_knee'],
    initial_positions['left_ankle'],
    initial_positions['right_ankle']
]

# Function to update the positions based on time
def update_positions(frame):
    t = frame / fps  # Time in seconds
    
    # Define the base amplitude and frequency for the running motion
    amplitude = 0.8
    frequency = 2 * np.pi * 0.5  # Frequency in radians per second
    
    # Update the positions of the points
    updated_points = []
    
    # Head: Slightly swaying side-to-side
    head_x = initial_positions['head'][0] + 0.2 * np.sin(frequency * t)
    head_y = initial_positions['head'][1]
    updated_points.append((head_x, head_y))
    
    # Shoulders: Swaying side-to-side with a slight lean forward
    left_shoulder_x = initial_positions['left_shoulder'][0] + 0.3 * np.sin(frequency * t)
    right_shoulder_x = initial_positions['right_shoulder'][0] - 0.3 * np.sin(frequency * t)
    shoulder_y = initial_positions['left_shoulder'][1] - 0.1 * np.cos(frequency * t)
    updated_points.append((left_shoulder_x, shoulder_y))
    updated_points.append((right_shoulder_x, shoulder_y))
    
    # Elbows: Follow the shoulders with a slight delay
    left_elbow_x = initial_positions['left_elbow'][0] + 0.4 * np.sin(frequency * t - np.pi / 4)
    right_elbow_x = initial_positions['right_elbow'][0] - 0.4 * np.sin(frequency * t - np.pi / 4)
    elbow_y = initial_positions['left_elbow'][1] - 0.15 * np.cos(frequency * t)
    updated_points.append((left_elbow_x, elbow_y))
    updated_points.append((right_elbow_x, elbow_y))
    
    # Wrists: Follow the elbows
    left_wrist_x = initial_positions['left_wrist'][0] + 0.5 * np.sin(frequency * t - np.pi / 2)
    right_wrist_x = initial_positions['right_wrist'][0] - 0.5 * np.sin(frequency * t - np.pi / 2)
    wrist_y = initial_positions['left_wrist'][1] - 0.2 * np.cos(frequency * t)
    updated_points.append((left_wrist_x, wrist_y))
    updated_points.append((right_wrist_x, wrist_y))
    
    # Hips: Swaying side-to-side with a heavier amplitude
    left_hip_x = initial_positions['left_hip'][0] + 0.4 * np.sin(frequency * t + np.pi / 4)
    right_hip_x = initial_positions['right_hip'][0] - 0.4 * np.sin(frequency * t + np.pi / 4)
    hip_y = initial_positions['left_hip'][1] - 0.1 * np.cos(frequency * t)
    updated_points.append((left_hip_x, hip_y))
    updated_points.append((right_hip_x, hip_y))
    
    # Knees: Follow the hips with a slight delay
    left_knee_x = initial_positions['left_knee'][0] + 0.6 * np.sin(frequency * t + np.pi / 2)
    right_knee_x = initial_positions['right_knee'][0] - 0.6 * np.sin(frequency * t + np.pi / 2)
    knee_y = initial_positions['left_knee'][1] - 0.2 * np.cos(frequency * t)
    updated_points.append((left_knee_x, knee_y))
    updated_points.append((right_knee_x, knee_y))
    
    # Ankles: Follow the knees with a slight delay
    left_ankle_x = initial_positions['left_ankle'][0] + 0.7 * np.sin(frequency * t + np.pi)
    right_ankle_x = initial_positions['right_ankle'][0] - 0.7 * np.sin(frequency * t + np.pi)
    ankle_y = initial_positions['left_ankle'][1] - 0.3 * np.cos(frequency * t)
    updated_points.append((left_ankle_x, ankle_y))
    updated_points.append((right_ankle_x, ankle_y))
    
    return updated_points

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    points = update_positions(frame)
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()

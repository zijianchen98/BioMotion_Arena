
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 120

# Define the positions of the 15 point-lights for a bowing motion
# These positions are simplified and may need refinement for full realism
def get_bowing_positions(t):
    # Head
    head_x = 0.0
    head_y = 1.5 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    
    # Torso
    torso_x = 0.0
    torso_y = 1.0 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Shoulders
    shoulder_left_x = -0.4 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    shoulder_left_y = 1.0 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    shoulder_right_x = 0.4 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    shoulder_right_y = 1.0 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Elbows
    elbow_left_x = -0.8 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    elbow_left_y = 0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    elbow_right_x = 0.8 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    elbow_right_y = 0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Wrists
    wrist_left_x = -1.2 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    wrist_left_y = 0.0 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    wrist_right_x = 1.2 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    wrist_right_y = 0.0 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Hips
    hip_left_x = -0.3 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    hip_left_y = 0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    hip_right_x = 0.3 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    hip_right_y = 0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Knees
    knee_left_x = -0.6 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    knee_left_y = -0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    knee_right_x = 0.6 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    knee_right_y = -0.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Ankles
    ankle_left_x = -0.9 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    ankle_left_y = -1.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    ankle_right_x = 0.9 + 0.1 * np.sin(2 * np.pi * t / num_frames)
    ankle_right_y = -1.5 + 0.2 * np.sin(2 * np.pi * t / num_frames)
    
    # Combine all positions into a single array
    positions = np.array([
        [head_x, head_y],
        [torso_x, torso_y],
        [shoulder_left_x, shoulder_left_y],
        [shoulder_right_x, shoulder_right_y],
        [elbow_left_x, elbow_left_y],
        [elbow_right_x, elbow_right_y],
        [wrist_left_x, wrist_left_y],
        [wrist_right_x, wrist_right_y],
        [hip_left_x, hip_left_y],
        [hip_right_x, hip_right_y],
        [knee_left_x, knee_left_y],
        [knee_right_x, knee_right_y],
        [ankle_left_x, ankle_left_y],
        [ankle_right_x, ankle_right_y]
    ])
    
    # Apply a bowing motion transformation
    angle = np.pi * 0.2 * np.sin(2 * np.pi * t / num_frames)
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions[:, :2] = np.dot(positions[:, :2], rotation_matrix.T)
    
    return positions

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the initial scatter plot
points, = ax.plot([], [], 'o', markersize=10, color='white')

# Update function for the animation
def update(frame):
    positions = get_bowing_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()

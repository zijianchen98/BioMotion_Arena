
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These positions are based on a simplified model of a person bowing
initial_positions = np.array([
    [0.5, 0.5],  # Head
    [0.5, 0.4],  # Neck
    [0.5, 0.3],  # Chest
    [0.4, 0.2],  # Left Shoulder
    [0.6, 0.2],  # Right Shoulder
    [0.3, 0.1],  # Left Elbow
    [0.7, 0.1],  # Right Elbow
    [0.2, 0.0],  # Left Hand
    [0.8, 0.0],  # Right Hand
    [0.5, 0.2],  # Hips
    [0.4, 0.1],  # Left Knee
    [0.6, 0.1],  # Right Knee
    [0.3, 0.0],  # Left Foot
    [0.7, 0.0],  # Right Foot
    [0.5, 0.3]   # Center of mass
])

# Define the target positions for the bowing action
target_positions = np.array([
    [0.5, 0.5],  # Head
    [0.5, 0.4],  # Neck
    [0.5, 0.3],  # Chest
    [0.4, 0.2],  # Left Shoulder
    [0.6, 0.2],  # Right Shoulder
    [0.3, 0.1],  # Left Elbow
    [0.7, 0.1],  # Right Elbow
    [0.2, 0.0],  # Left Hand
    [0.8, 0.0],  # Right Hand
    [0.5, 0.2],  # Hips
    [0.4, 0.1],  # Left Knee
    [0.6, 0.1],  # Right Knee
    [0.3, 0.0],  # Left Foot
    [0.7, 0.0],  # Right Foot
    [0.5, 0.1]   # Center of mass (lowered for bowing)
])

# Define the number of frames in the animation
num_frames = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot([], [], 'o', color='white', markersize=5)

# Initialize the positions
positions = initial_positions.copy()

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Calculate the current position for each point light
    t = frame / num_frames
    positions = (1 - t) * initial_positions + t * target_positions
    
    # Update the positions of the point lights
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, repeat=False)

# Show the animation
plt.show()

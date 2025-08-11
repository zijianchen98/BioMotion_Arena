
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1.0],
    'torso': [0, 0.5],
    'left_shoulder': [-0.2, 0.7],
    'right_shoulder': [0.2, 0.7],
    'left_elbow': [-0.4, 0.4],
    'right_elbow': [0.4, 0.4],
    'left_wrist': [-0.6, 0.1],
    'right_wrist': [0.6, 0.1],
    'left_hip': [-0.2, 0.3],
    'right_hip': [0.2, 0.3],
    'left_knee': [-0.4, 0.0],
    'right_knee': [0.4, 0.0],
    'left_ankle': [-0.6, -0.3],
    'right_ankle': [0.6, -0.3],
    'center_of_mass': [0, 0.4]
}

# Convert the dictionary to a list of initial positions
initial_points = np.array(list(initial_positions.values()))

# Define the amplitude and frequency for the jumping motion
amplitude = 0.2  # Vertical displacement
frequency = 0.1  # Frequency of the jump (cycles per frame)

# Define the time array for the animation
t = np.linspace(0, 2 * np.pi, num_frames)

# Function to update the positions based on the jump motion
def update_positions(frame):
    # Apply vertical oscillation to the center of mass
    vertical_displacement = amplitude * np.sin(frequency * t[frame])
    
    # Update the positions of all points based on the center of mass
    updated_positions = initial_points.copy()
    updated_positions[:, 1] += vertical_displacement
    
    # Simulate sagging due to "heavy weight"
    updated_positions *= 0.95  # Slightly reduce the overall height
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()

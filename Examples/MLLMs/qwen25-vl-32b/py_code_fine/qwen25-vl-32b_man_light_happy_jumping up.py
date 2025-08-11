
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (happyman)
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
initial_coords = np.array(list(initial_positions.values()))

# Define the gravitational acceleration (m/s^2)
g = 9.81

# Define the jump parameters
jump_amplitude = 1.0  # Maximum height of the jump
jump_duration = 1.0   # Duration of the jump (seconds)
frame_rate = 30       # Frames per second
total_frames = int(jump_duration * frame_rate)

# Precompute the vertical displacement for each frame
time = np.linspace(0, jump_duration, total_frames)
vertical_displacement = jump_amplitude * (1 - (2 * time / jump_duration)**2)

# Function to update the positions based on the jump
def update_positions(frame):
    # Apply the vertical displacement to all points
    updated_coords = initial_coords.copy()
    updated_coords[:, 1] += vertical_displacement[frame]
    
    # Add some horizontal oscillation to simulate natural movement
    horizontal_oscillation = 0.1 * np.sin(2 * np.pi * frame / total_frames)
    updated_coords[:, 0] += horizontal_oscillation
    
    return updated_coords

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

def animate(frame):
    updated_coords = update_positions(frame)
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=total_frames, interval=1000 / frame_rate, blit=True
)

# Display the animation
plt.show()

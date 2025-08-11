
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.25],
    'right_elbow': [1, 0.25],
    'left_hand': [-1.5, -0.25],
    'right_hand': [1.5, -0.25],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the animation parameters
num_frames = 60  # Number of frames in the animation
frame_rate = 30  # Frames per second
amplitude = 0.8  # Amplitude of the jump
frequency = 1.0  # Frequency of the jump
weight_factor = 0.5  # Factor to simulate heaviness

# Function to update the positions based on time
def update_positions(frame):
    t = frame / frame_rate  # Current time in seconds
    
    # Vertical displacement for the jump (sinusoidal motion)
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Apply the vertical displacement to all points
    updated_coords = initial_coords.copy()
    updated_coords[:, 1] += vertical_displacement
    
    # Simulate forward motion (horizontal displacement)
    horizontal_displacement = 0.5 * np.sin(2 * np.pi * frequency * t)
    updated_coords[:, 0] += horizontal_displacement
    
    # Apply weight factor to slow down the movement
    updated_coords *= (1 - weight_factor * np.abs(np.sin(2 * np.pi * frequency * t)))
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initialize the scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    updated_coords = update_positions(frame)
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig,
    animate,
    frames=num_frames,
    interval=1000 / frame_rate,  # Interval between frames in milliseconds
    blit=True
)

# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a human figure
key_points = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_hand',
    'left_shoulder', 'left_elbow', 'left_hand', 'right_hip', 'right_knee',
    'right_foot', 'left_hip', 'left_knee', 'left_foot', 'center'
]

# Define the initial positions of the key points
initial_positions = {
    'head': np.array([0, 1.5]),
    'neck': np.array([0, 1.0]),
    'right_shoulder': np.array([-0.5, 0.8]),
    'right_elbow': np.array([-0.7, 0.6]),
    'right_hand': np.array([-0.9, 0.4]),
    'left_shoulder': np.array([0.5, 0.8]),
    'left_elbow': np.array([0.7, 0.6]),
    'left_hand': np.array([0.9, 0.4]),
    'right_hip': np.array([-0.4, 0.2]),
    'right_knee': np.array([-0.5, 0.0]),
    'right_foot': np.array([-0.6, -0.2]),
    'left_hip': np.array([0.4, 0.2]),
    'left_knee': np.array([0.5, 0.0]),
    'left_foot': np.array([0.6, -0.2]),
    'center': np.array([0, 0])
}

# Function to update the positions of the key points for each frame
def update_positions(frame):
    # Calculate the jumping motion
    t = frame / 100.0  # Time parameter
    y_offset = 0.5 * np.sin(2 * np.pi * t)  # Vertical displacement for jumping

    # Update the positions of the key points
    new_positions = {k: v + np.array([0, y_offset]) for k, v in initial_positions.items()}

    # Apply some subtle horizontal motion to make it look like she's jumping forward
    x_offset = 0.1 * t
    new_positions = {k: v + np.array([x_offset, 0]) for k, v in new_positions.items()}

    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter([], [], s=50, color='white')

# Function to initialize the animation
def init():
    scat.set_offsets([])
    return scat,

# Function to update the animation
def animate(frame):
    new_positions = update_positions(frame)
    positions = [new_positions[key] for key in key_points]
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the 15 point-lights
# These positions represent the body parts of the woman
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
    'right_foot': [1.5, -1.5],
}

# Define the trajectory for the jump
def get_position(frame):
    t = frame / num_frames  # Normalized time (0 to 1)
    
    # Define the vertical displacement for the jump
    vertical_displacement = 0.8 * np.sin(t * np.pi)  # Sinusoidal motion
    
    # Define the horizontal displacement for the jump
    horizontal_displacement = 0.5 * t  # Linear forward motion
    
    # Update positions based on the trajectory
    updated_positions = {}
    for key, pos in initial_positions.items():
        x, y = pos
        updated_positions[key] = [
            x + horizontal_displacement,  # Forward motion
            y + vertical_displacement     # Vertical jump
        ]
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def update(frame):
    positions = get_position(frame)
    x = [pos[0] for pos in positions.values()]
    y = [pos[1] for pos in positions.values()]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, interval=40, blit=True
)

# Display the animation
plt.show()

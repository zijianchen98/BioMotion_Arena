
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure
initial_positions = {
    'head': [0, 1],
    'torso_top': [0, 0],
    'torso_bottom': [0, -1],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0],
    'right_elbow': [1, 0],
    'left_wrist': [-1.5, -0.5],
    'right_wrist': [1.5, -0.5],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the range of motion for bowing
def get_bowing_positions(t, amplitude=0.5, frequency=0.1):
    """
    Generate positions for a bowing motion.
    t: time step
    amplitude: vertical displacement during bowing
    frequency: how fast the bowing occurs
    """
    # Bowing involves lowering the torso and head while keeping the legs relatively stable
    bowing_factor = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update positions for bowing
    updated_positions = initial_coords.copy()
    updated_positions[0] += [0, bowing_factor]  # Head
    updated_positions[1] += [0, bowing_factor]  # Torso top
    updated_positions[2] += [0, bowing_factor]  # Torso bottom
    
    # Add some sway to the shoulders and hips to simulate heaviness
    sway_factor = 0.2 * np.sin(2 * np.pi * frequency * t + np.pi / 4)
    updated_positions[3] += [sway_factor, 0]  # Left shoulder
    updated_positions[4] -= [sway_factor, 0]  # Right shoulder
    updated_positions[9] += [sway_factor, 0]  # Left hip
    updated_positions[10] -= [sway_factor, 0]  # Right hip
    
    return updated_positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

def init():
    """Initialize the scatter plot."""
    scat.set_offsets([])
    return scat,

def update(frame):
    """Update the scatter plot for each frame."""
    positions = get_bowing_positions(frame / 30)  # Assuming 30 frames per second
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=range(100), init_func=init, blit=True, interval=33, repeat=True
)

# Display the animation
plt.show()

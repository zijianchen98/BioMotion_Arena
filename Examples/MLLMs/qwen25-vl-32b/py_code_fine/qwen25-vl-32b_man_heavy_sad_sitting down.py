
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions represent the body parts of a person in a standing posture
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.25],
    'right_elbow': [1, 0.25],
    'left_wrist': [-1.5, -0.25],
    'right_wrist': [1.5, -0.25],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_ankle': [-1.5, -1.5],
    'right_ankle': [1.5, -1.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the trajectory for sitting down
def sitting_down_animation(t):
    """
    Simulate the motion of sitting down with a heavy weight.
    t: Time parameter (0 to 1)
    """
    # Smooth transition using a cubic easing function
    ease_in_out = 3 * t**2 - 2 * t**3
    
    # Define the final positions when sitting down
    sitting_positions = {
        'head': [0, 0.5],
        'torso': [0, 0],
        'left_shoulder': [-0.5, 0.25],
        'right_shoulder': [0.5, 0.25],
        'left_elbow': [-1, -0.25],
        'right_elbow': [1, -0.25],
        'left_wrist': [-1.5, -0.75],
        'right_wrist': [1.5, -0.75],
        'left_hip': [-0.5, -0.5],
        'right_hip': [0.5, -0.5],
        'left_knee': [-1, -1],
        'right_knee': [1, -1],
        'left_ankle': [-1.5, -1.5],
        'right_ankle': [1.5, -1.5],
    }
    
    # Interpolate between initial and final positions
    final_coords = np.array(list(sitting_positions.values()))
    interpolated_coords = (1 - ease_in_out) * initial_coords + ease_in_out * final_coords
    return interpolated_coords

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

def update(frame):
    # Update the positions of the point-lights
    coords = sitting_down_animation(frame / 100.0)
    scat.set_offsets(coords)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=40, blit=True)

# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 1],
    'torso_top': [0, 0],
    'torso_bottom': [0, -0.5],
    'left_shoulder': [-0.3, 0.2],
    'right_shoulder': [0.3, 0.2],
    'left_elbow': [-0.6, -0.2],
    'right_elbow': [0.6, -0.2],
    'left_wrist': [-0.9, -0.7],
    'right_wrist': [0.9, -0.7],
    'left_hip': [-0.3, -1],
    'right_hip': [0.3, -1],
    'left_knee': [-0.6, -1.5],
    'right_knee': [0.6, -1.5],
    'left_ankle': [-0.9, -2],
    'right_ankle': [0.9, -2]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the bowing motion
def bowing_motion(t, amplitude=0.5, frequency=0.2):
    """
    Simulate a bowing motion by applying a sinusoidal transformation.
    """
    # Bowing affects the torso and head primarily
    torso_amplitude = amplitude
    head_amplitude = amplitude * 1.2
    
    # Apply the bowing effect
    bow_angle = np.sin(2 * np.pi * frequency * t)
    
    # Transform the torso and head positions
    transformed_coords = initial_coords.copy()
    transformed_coords[0] += [0, head_amplitude * bow_angle]  # Head
    transformed_coords[1] += [0, torso_amplitude * bow_angle]  # Torso top
    transformed_coords[2] += [0, torso_amplitude * bow_angle]  # Torso bottom
    
    # Adjust the hip and knee positions to simulate bending
    hip_amplitude = amplitude * 0.8
    knee_amplitude = amplitude * 1.2
    ankle_amplitude = amplitude * 1.5
    
    transformed_coords[9] += [0, hip_amplitude * bow_angle]  # Left hip
    transformed_coords[10] += [0, hip_amplitude * bow_angle]  # Right hip
    transformed_coords[11] += [0, knee_amplitude * bow_angle]  # Left knee
    transformed_coords[12] += [0, knee_amplitude * bow_angle]  # Right knee
    transformed_coords[13] += [0, ankle_amplitude * bow_angle]  # Left ankle
    transformed_coords[14] += [0, ankle_amplitude * bow_angle]  # Right ankle
    
    return transformed_coords

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

def update(frame):
    coords = bowing_motion(frame / 30)  # Update based on frame number
    scat.set_offsets(coords)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=100, interval=30, blit=True)

# Display the animation
plt.show()

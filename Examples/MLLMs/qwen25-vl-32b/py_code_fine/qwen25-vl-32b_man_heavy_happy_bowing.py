
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions of the 15 points (head, shoulders, elbows, wrists, hips, knees, ankles)
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0], # Left shoulder
    [0.5, 0],  # Right shoulder
    [-1, -1],  # Left elbow
    [1, -1],   # Right elbow
    [-1, -2],  # Left wrist
    [1, -2],   # Right wrist
    [0, -3],   # Hips
    [-0.5, -4], # Left knee
    [0.5, -4],  # Right knee
    [-0.5, -5], # Left ankle
    [0.5, -5],  # Right ankle
])

# Define the bowing motion
def bowing_motion(t, amplitude=0.5, frequency=0.2):
    """
    Generate bowing motion for the upper body.
    t: time (in seconds)
    amplitude: vertical displacement during bowing
    frequency: how fast the bowing occurs
    """
    # Bowing involves lowering the upper body
    angle = np.sin(2 * np.pi * frequency * t) * amplitude
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply the rotation to the upper body joints (head, shoulders, elbows, wrists)
    upper_body_indices = [0, 1, 2, 3, 4, 5, 6]
    upper_body_points = initial_positions[upper_body_indices]
    rotated_upper_body = np.dot(upper_body_points, rotation_matrix.T)
    
    # Combine the rotated upper body with the lower body (hips, knees, ankles)
    new_positions = initial_positions.copy()
    new_positions[upper_body_indices] = rotated_upper_body
    
    return new_positions

# Setup the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-6, 2)
ax.axis('off')  # Hide axes for a cleaner look
points, = ax.plot([], [], 'wo', markersize=10)  # White points on black background

# Animation function
def animate(t):
    positions = bowing_motion(t)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.linspace(0, 10, 200), interval=50, blit=True)

# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize constants
num_points = 15
frames = 100
frequency = 2 * np.pi / frames

# Define the initial positions for the point-lights
# Body parts (x, y) coordinates approximate for a waving motion
body_parts = np.array([
    [0, 0],      # Center
    [-0.1, 0.5], # Left Hand
    [0.1, 0.5],  # Right Hand
    [-0.2, 0.3], # Left Elbow
    [0.2, 0.3],  # Right Elbow
    [-0.1, 0.1], # Left Shoulder
    [0.1, 0.1],  # Right Shoulder
    [-0.15, -0.3], # Left Knee
    [0.15, -0.3],  # Right Knee
    [-0.1, -0.5], # Left Foot
    [0.1, -0.5],  # Right Foot
    [0, 0.6],     # Head
    [-0.05, 0.55],# Hair
    [0.05, 0.55], # Hair
    [-0.05, 0.65],# Hat
    [0.05, 0.65]  # Hat
])

# Waving hand motion simulation
def update(frame):
    plt.clf()
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_facecolor('black')
    
    # Calculate new positions based on the waving motion
    angle = np.sin(frequency * frame) * np.pi / 6  # Wave angle
    right_hand_y = 0.5 + np.sin(angle) * 0.2  # Defines the waving motion
    
    # Update the hand position
    updated_body_parts = body_parts.copy()
    updated_body_parts[2, 1] = right_hand_y  # Update right hand position

    # Plot the points
    for point in updated_body_parts:
        plt.plot(point[0], point[1], 'wo', markersize=10)  # White points

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000 / 24)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the interval between frames
num_frames = 100
interval = 50  # ms

# Define the initial positions of the 15 points. These positions are just a starting point.
# Adjust these to reflect a person lying down, with a sad posture and heavy weight.
initial_positions = np.array([
    [0.0, 1.0],  # Head
    [-0.2, 0.8],  # Left shoulder
    [0.2, 0.8],   # Right shoulder
    [-0.4, 0.6],  # Left elbow
    [0.4, 0.6],   # Right elbow
    [-0.6, 0.4],  # Left wrist
    [0.6, 0.4],   # Right wrist
    [-0.1, 0.5],  # Hip
    [0.1, 0.5],   # Hip
    [-0.3, 0.3],  # Left knee
    [0.3, 0.3],   # Right knee
    [-0.5, 0.1],  # Left ankle
    [0.5, 0.1],   # Right ankle
    [-0.2, -0.1], # Left Foot
    [0.2, -0.1]  # Right Foot
])

# Scale the positions to fit the figure better
initial_positions *= 2

# Define the animation function
def update(frame):
    plt.clf()  # Clear the previous frame

    # Simulate the person lying down and slightly moving. This is a simplification
    # and you would need more complex calculations for realistic motion capture data.
    positions = initial_positions.copy()

    # Simulate movement, make it look like the person is shifting weight and sighing
    movement_scale = 0.05  # Adjust to control the intensity of the movements
    positions[0] += [0, np.sin(frame/10) * movement_scale] # Head
    positions[1] += [np.sin(frame/5) * movement_scale, 0]  # Left shoulder
    positions[2] += [-np.sin(frame/5) * movement_scale, 0]  # Right shoulder
    positions[3] += [np.cos(frame/7) * movement_scale, 0]  # Left elbow
    positions[4] += [-np.cos(frame/7) * movement_scale, 0]  # Right elbow
    positions[7] += [0, np.sin(frame/12) * movement_scale/2]  # Hip

    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

    # Set the plot limits
    plt.xlim([-3, 3])
    plt.ylim([-3, 3])
    plt.gca().set_aspect('equal', adjustable='box')

    # Set the background color to black
    plt.gca().set_facecolor('black')

    # Remove axes
    plt.axis('off')

# Create the animation
fig = plt.figure(facecolor='black') # Set figure background color to black
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=interval)

plt.show()

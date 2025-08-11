
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Total number of point-lights
frames = 60      # Number of frames in the animation
wave_amplitude = 0.2  # Amplitude of the wave motion

# Initial positions of point-lights (arranged in a simple humanoid shape)
# x and y coordinates for the points
base_positions = np.array([
    [0, 0.5],   # Head
    [-0.1, 0.4], # Left shoulder
    [0.1, 0.4],  # Right shoulder
    [-0.2, 0.3], # Left arm
    [0.2, 0.3],  # Right arm
    [-0.2, 0.2], # Left elbow
    [0.2, 0.2],  # Right elbow
    [0, 0.1],    # Body
    [0.0, 0.0],  # Waist
    [-0.1, -0.1],# Left leg
    [0.1, -0.1], # Right leg
    [-0.15, -0.2],# Left foot
    [0.15, -0.2], # Right foot
])

# Function to update the points for waving motion
def update(frame):
    plt.clf()  # Clear the current figure
    plt.xlim(-0.5, 0.5)  # Set x-axis limits
    plt.ylim(-0.5, 0.5)  # Set y-axis limits
    plt.axis('off')  # Turn off the axis

    # Calculate the waving motion for the right hand
    waving_hand_y = base_positions[5, 1] + wave_amplitude * np.sin(frame / 5) * np.cos(frame / 10)

    # Update positions of the point-lights
    positions = base_positions.copy()
    positions[5, 1] = waving_hand_y  # Update the y position of right hand

    # Plot all point-lights as white dots
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create a figure and set a black background
fig = plt.figure(figsize=(5, 5), facecolor='black')
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/30)

# Show the animation
plt.show()

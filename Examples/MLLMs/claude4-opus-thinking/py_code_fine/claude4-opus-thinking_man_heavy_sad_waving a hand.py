
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point lights
frames = 60      # Number of frames in the animation
wave_amplitude = 0.1  # Amplitude of movement for waving
time_unit = np.linspace(0, 2 * np.pi, frames)

# Initialize points representing the sad man and hand
base_positions = np.array([
    [0, 0],  # Core
    [-0.1, -0.5],  # Left foot
    [0.1, -0.5],   # Right foot
    [-0.2, -0.3],  # Left knee
    [0.2, -0.3],   # Right knee
    [-0.3, -0.1],  # Left hip
    [0.3, -0.1],   # Right hip
    [0, 0.2],      # Torso
    [-0.15, 0.4],  # Left shoulder
    [0.15, 0.4],   # Right shoulder
    [0, 0.5],      # Head
    [-0.2, 0.3],   # Left elbow
    [0.2, 0.3],    # Right elbow
    [-0.25, 0.5],  # Left hand
    [0.25, np.sin(time_unit) * wave_amplitude + 0.5],  # Right hand waving
])

def update(frame):
    # Clear the current figure
    plt.clf()
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_facecolor('black')  # Set background to black
    plt.axis('off')  # Turn off the axis

    # Update the right hand position to create a waving effect
    hand_wave_y = wave_amplitude * np.sin(frame * np.pi / frames) + (0.5)  # Smooth waving motion
    body_positions = np.copy(base_positions)
    body_positions[14, 1] = hand_wave_y  # Right hand
    
    # Plot the point lights
    plt.scatter(body_positions[:, 0], body_positions[:, 1], color='white', s=100)  # s is the size of the points

# Create the figure
fig = plt.figure()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50)

# Show the animation
plt.show()

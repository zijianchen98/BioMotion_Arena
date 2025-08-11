
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for the sad woman
def get_point_light_positions(t):
    # Define the initial positions of the 15 point-lights
    # These positions are based on the typical locations of joints in the human body
    # (e.g., shoulders, elbows, wrists, hips, knees, ankles)
    initial_positions = np.array([
        [0.5, 0.5],  # head
        [0.4, 0.6],  # left shoulder
        [0.3, 0.7],  # left elbow
        [0.2, 0.8],  # left wrist
        [0.6, 0.6],  # right shoulder
        [0.7, 0.7],  # right elbow
        [0.8, 0.8],  # right wrist
        [0.5, 0.4],  # left hip
        [0.4, 0.3],  # left knee
        [0.3, 0.2],  # left ankle
        [0.5, 0.4],  # right hip
        [0.6, 0.3],  # right knee
        [0.7, 0.2],  # right ankle
        [0.5, 0.1],  # left heel
        [0.5, 0.1],  # right heel
    ])

    # Define the movement of each point-light
    # These movements are based on the typical movements of the human body
    # when performing the specified action (waving a hand)
    movements = np.array([
        [0, 0],  # head
        [-0.05 * np.sin(t), 0.05 * np.sin(t)],  # left shoulder
        [-0.1 * np.sin(t), 0.1 * np.sin(t)],  # left elbow
        [-0.15 * np.sin(t), 0.15 * np.sin(t)],  # left wrist
        [0.05 * np.sin(t), 0.05 * np.sin(t)],  # right shoulder
        [0.1 * np.sin(t), 0.1 * np.sin(t)],  # right elbow
        [0.15 * np.sin(t), 0.15 * np.sin(t)],  # right wrist
        [0, 0],  # left hip
        [0, 0],  # left knee
        [0, 0],  # left ankle
        [0, 0],  # right hip
        [0, 0],  # right knee
        [0, 0],  # right ankle
        [0, -0.05 * np.sin(t)],  # left heel
        [0, -0.05 * np.sin(t)],  # right heel
    ])

    # Calculate the positions of the point-lights at time t
    positions = initial_positions + movements

    return positions

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Initialize the point-lights
point_lights = get_point_light_positions(0)

# Plot the point-lights
scatter = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white')

# Set the limits of the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Define the animation function
def animate(t):
    global point_lights
    point_lights = get_point_light_positions(t)
    scatter.set_offsets(point_lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 128), blit=True, interval=50)

# Show the animation
plt.show()

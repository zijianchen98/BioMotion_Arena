
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light positions for each frame
def get_point_light_positions(frame):
    # Define the 15 point-lights for the happy woman
    # The first column is the x-coordinate, the second column is the y-coordinate
    point_lights = np.array([
        [0.1, 0.1],  # Head
        [0.2, 0.2],  # Right shoulder
        [0.2, 0.8],  # Right elbow
        [0.2, 1.2],  # Right wrist
        [0.8, 0.2],  # Left shoulder
        [0.8, 0.8],  # Left elbow
        [0.8, 1.2],  # Left wrist
        [0.5, 0.5],  # Torso
        [0.4, 0.7],  # Right hip
        [0.4, 1.0],  # Right knee
        [0.4, 1.3],  # Right ankle
        [0.6, 0.7],  # Left hip
        [0.6, 1.0],  # Left knee
        [0.6, 1.3],  # Left ankle
        [0.5, 1.5]   # Weight
    ])

    # Define the walking motion
    # The motion is defined as a function of the frame number
    # The frame number is used to calculate the phase of the motion
    phase = frame / 10.0

    # Calculate the new positions of the point-lights
    new_positions = np.copy(point_lights)

    # Move the right arm
    new_positions[1, 0] = 0.2 + 0.1 * np.sin(phase)
    new_positions[2, 0] = 0.2 + 0.1 * np.sin(phase)
    new_positions[3, 0] = 0.2 + 0.1 * np.sin(phase)

    # Move the left arm
    new_positions[4, 0] = 0.8 + 0.1 * np.cos(phase)
    new_positions[5, 0] = 0.8 + 0.1 * np.cos(phase)
    new_positions[6, 0] = 0.8 + 0.1 * np.cos(phase)

    # Move the right leg
    new_positions[8, 1] = 0.7 + 0.3 * np.sin(phase)
    new_positions[9, 1] = 1.0 + 0.3 * np.sin(phase)
    new_positions[10, 1] = 1.3 + 0.3 * np.sin(phase)

    # Move the left leg
    new_positions[11, 1] = 0.7 + 0.3 * np.cos(phase)
    new_positions[12, 1] = 1.0 + 0.3 * np.cos(phase)
    new_positions[13, 1] = 1.3 + 0.3 * np.cos(phase)

    # Move the weight
    new_positions[14, 1] = 1.5 + 0.1 * np.sin(phase)

    return new_positions

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
point_lights = get_point_light_positions(0)
scat = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, color='white')

# Animation function
def animate(frame):
    global point_lights, scat
    new_positions = get_point_light_positions(frame)
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()

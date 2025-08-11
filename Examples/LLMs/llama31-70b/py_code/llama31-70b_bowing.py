
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights positions at each frame of the animation
def get_point_lights_positions(frame):
    # Define the point-lights positions for the bowing action
    # The positions are defined in a 3D space (x, y, z)
    # We will project the 3D positions to 2D for the animation
    point_lights = np.array([
        # Head
        [0, 0, 0],
        # Torso
        [0, -1, 0],
        [0, -2, 0],
        # Left arm
        [-1, -1, 0],
        [-2, -1, 0],
        [-2, 0, 0],
        # Right arm
        [1, -1, 0],
        [2, -1, 0],
        [2, 0, 0],
        # Left leg
        [-1, -3, 0],
        [-2, -3, 0],
        [-2, -4, 0],
        # Right leg
        [1, -3, 0],
        [2, -3, 0],
        [2, -4, 0],
    ])

    # Define the rotation angles for the bowing action
    angle_head = np.radians(30 * np.sin(frame / 10.0))
    angle_torso = np.radians(30 * np.sin(frame / 10.0))
    angle_left_arm = np.radians(60 * np.sin(frame / 10.0))
    angle_right_arm = np.radians(-60 * np.sin(frame / 10.0))
    angle_left_leg = np.radians(30 * np.sin(frame / 10.0))
    angle_right_leg = np.radians(-30 * np.sin(frame / 10.0))

    # Rotate the point-lights positions based on the rotation angles
    rotated_point_lights = np.array([
        # Head
        [point_lights[0, 0], point_lights[0, 1] * np.cos(angle_head) - point_lights[0, 2] * np.sin(angle_head), point_lights[0, 1] * np.sin(angle_head) + point_lights[0, 2] * np.cos(angle_head)],
        # Torso
        [point_lights[1, 0], point_lights[1, 1] * np.cos(angle_torso) - point_lights[1, 2] * np.sin(angle_torso), point_lights[1, 1] * np.sin(angle_torso) + point_lights[1, 2] * np.cos(angle_torso)],
        [point_lights[2, 0], point_lights[2, 1] * np.cos(angle_torso) - point_lights[2, 2] * np.sin(angle_torso), point_lights[2, 1] * np.sin(angle_torso) + point_lights[2, 2] * np.cos(angle_torso)],
        # Left arm
        [point_lights[3, 0] * np.cos(angle_left_arm) - point_lights[3, 2] * np.sin(angle_left_arm), point_lights[3, 1], point_lights[3, 0] * np.sin(angle_left_arm) + point_lights[3, 2] * np.cos(angle_left_arm)],
        [point_lights[4, 0] * np.cos(angle_left_arm) - point_lights[4, 2] * np.sin(angle_left_arm), point_lights[4, 1], point_lights[4, 0] * np.sin(angle_left_arm) + point_lights[4, 2] * np.cos(angle_left_arm)],
        [point_lights[5, 0] * np.cos(angle_left_arm) - point_lights[5, 2] * np.sin(angle_left_arm), point_lights[5, 1], point_lights[5, 0] * np.sin(angle_left_arm) + point_lights[5, 2] * np.cos(angle_left_arm)],
        # Right arm
        [point_lights[6, 0] * np.cos(angle_right_arm) - point_lights[6, 2] * np.sin(angle_right_arm), point_lights[6, 1], point_lights[6, 0] * np.sin(angle_right_arm) + point_lights[6, 2] * np.cos(angle_right_arm)],
        [point_lights[7, 0] * np.cos(angle_right_arm) - point_lights[7, 2] * np.sin(angle_right_arm), point_lights[7, 1], point_lights[7, 0] * np.sin(angle_right_arm) + point_lights[7, 2] * np.cos(angle_right_arm)],
        [point_lights[8, 0] * np.cos(angle_right_arm) - point_lights[8, 2] * np.sin(angle_right_arm), point_lights[8, 1], point_lights[8, 0] * np.sin(angle_right_arm) + point_lights[8, 2] * np.cos(angle_right_arm)],
        # Left leg
        [point_lights[9, 0] * np.cos(angle_left_leg) - point_lights[9, 2] * np.sin(angle_left_leg), point_lights[9, 1], point_lights[9, 0] * np.sin(angle_left_leg) + point_lights[9, 2] * np.cos(angle_left_leg)],
        [point_lights[10, 0] * np.cos(angle_left_leg) - point_lights[10, 2] * np.sin(angle_left_leg), point_lights[10, 1], point_lights[10, 0] * np.sin(angle_left_leg) + point_lights[10, 2] * np.cos(angle_left_leg)],
        [point_lights[11, 0] * np.cos(angle_left_leg) - point_lights[11, 2] * np.sin(angle_left_leg), point_lights[11, 1], point_lights[11, 0] * np.sin(angle_left_leg) + point_lights[11, 2] * np.cos(angle_left_leg)],
        # Right leg
        [point_lights[12, 0] * np.cos(angle_right_leg) - point_lights[12, 2] * np.sin(angle_right_leg), point_lights[12, 1], point_lights[12, 0] * np.sin(angle_right_leg) + point_lights[12, 2] * np.cos(angle_right_leg)],
        [point_lights[13, 0] * np.cos(angle_right_leg) - point_lights[13, 2] * np.sin(angle_right_leg), point_lights[13, 1], point_lights[13, 0] * np.sin(angle_right_leg) + point_lights[13, 2] * np.cos(angle_right_leg)],
        [point_lights[14, 0] * np.cos(angle_right_leg) - point_lights[14, 2] * np.sin(angle_right_leg), point_lights[14, 1], point_lights[14, 0] * np.sin(angle_right_leg) + point_lights[14, 2] * np.cos(angle_right_leg)],
    ])

    # Project the 3D positions to 2D
    projected_point_lights = np.array([[point_light[0], point_light[1]] for point_light in rotated_point_lights])

    return projected_point_lights

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the first frame
point_lights_positions = get_point_lights_positions(0)
scatter = ax.scatter(point_lights_positions[:, 0], point_lights_positions[:, 1], color='white')

# Set the background color to black
ax.set_facecolor('black')

# Set the limits of the plot
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Hide the axes
plt.axis('off')

# Define the animation function
def animate(frame):
    point_lights_positions = get_point_lights_positions(frame)
    scatter.set_offsets(point_lights_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()

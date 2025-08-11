
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (adjust as needed)
initial_positions = np.array([
    [0, 4],   # head
    [-1, 3],   # left shoulder
    [1, 3],    # right shoulder
    [-1.5, 2], # left elbow
    [1.5, 2],  # right elbow
    [-2, 1],   # left hand
    [2, 1],    # right hand
    [0, 2],    # torso top
    [0, 1],    # torso middle
    [0, 0],    # torso bottom
    [-0.5, -1], # left hip
    [0.5, -1],  # right hip
    [-1, -2],  # left knee
    [1, -2],   # right knee
    [0, -3]   # foot
]) * 1.0  # Scale the positions

# Define the animation function
def animate(i):
    # Clear the previous frame
    plt.cla()

    # Define bowing motion (adjust parameters for realistic motion)
    angle = np.sin(i * 0.1) * 0.8 # Angle varies over time
    angle2 = np.sin(i * 0.1 - 0.5) * 0.3 # Angle varies over time
    angle3 = np.sin(i * 0.1 + 0.3) * 0.2 # Angle varies over time

    # Define bowing motion (adjust parameters for realistic motion)
    torso_bend_angle = np.sin(i * 0.05) * 0.4 # Angle varies over time

    # Create a copy of the initial positions
    positions = initial_positions.copy()

    # Apply bowing motion
    # Rotate arms (shoulders as origin)
    positions[3] = rotate_point(positions[3], positions[1], angle)
    positions[5] = rotate_point(positions[5], positions[3], angle2)

    positions[4] = rotate_point(positions[4], positions[2], -angle)
    positions[6] = rotate_point(positions[6], positions[4], -angle2)

    # Rotate legs (hip as origin)
    positions[12] = rotate_point(positions[12], positions[10], angle3)

    positions[13] = rotate_point(positions[13], positions[11], -angle3)

    # Apply bending motion to the torso
    torso_rotation_center = positions[7]  # Rotate around torso top

    # Rotate torso points
    positions[8] = rotate_point(positions[8], torso_rotation_center, torso_bend_angle)
    positions[9] = rotate_point(positions[9], torso_rotation_center, torso_bend_angle)
    positions[10] = rotate_point(positions[10], torso_rotation_center, torso_bend_angle)
    positions[11] = rotate_point(positions[11], torso_rotation_center, torso_bend_angle)

    # Plot the points
    plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

    # Set plot limits and appearance
    plt.xlim(-4, 4)
    plt.ylim(-4, 5)
    plt.gca().set_facecolor('black')
    plt.axis('off')
    plt.title("Sadman Bowing")

    return plt.gca(),

def rotate_point(point, origin, angle):
    """Rotates a point around an origin by a given angle in radians."""
    ox, oy = origin
    px, py = point

    qx = ox + np.cos(angle) * (px - ox) - np.sin(angle) * (py - oy)
    qy = oy + np.sin(angle) * (px - ox) + np.cos(angle) * (py - oy)
    return np.array([qx, qy])

# Create the animation
fig = plt.figure(facecolor='black')
ani = animation.FuncAnimation(fig, animate, frames=200, blit=False, repeat=True)

# Show the animation
plt.show()

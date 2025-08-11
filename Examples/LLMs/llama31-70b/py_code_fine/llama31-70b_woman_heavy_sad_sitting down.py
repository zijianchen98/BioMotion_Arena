
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights positions for the sad woman with heavy weight sitting down
# These positions are based on the biological motion stimuli literature
# and have been adjusted to represent the specified action

# Initial positions (frame 1)
joints = np.array([
    [0.1, 0.5],  # Head
    [0.2, 0.6],  # Right shoulder
    [0.1, 0.4],  # Left shoulder
    [0.3, 0.5],  # Right elbow
    [0.0, 0.4],  # Left elbow
    [0.3, 0.3],  # Right hand
    [0.0, 0.2],  # Left hand
    [0.1, 0.2],  # Right hip
    [0.1, 0.1],  # Left hip
    [0.2, 0.0],  # Right knee
    [0.0, 0.0],  # Left knee
    [0.2, -0.1],  # Right ankle
    [0.0, -0.1],  # Left ankle
    [0.1, -0.2],  # Right foot
    [0.1, -0.2],  # Left foot
])

# Define the movement for each frame
def animate(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.7)
    ax.set_facecolor('black')
    ax.set_aspect('equal')

    # Calculate new positions for each joint based on the frame number
    # This is a simplified example and real biological motion stimuli would require more complex calculations
    new_joints = joints.copy()
    if frame < 20:
        new_joints[8] += [0, -0.01 * frame]  # Right hip
        new_joints[9] += [0, -0.01 * frame]  # Left hip
        new_joints[10] += [0, -0.02 * frame]  # Right knee
        new_joints[11] += [0, -0.02 * frame]  # Left knee
    elif frame < 40:
        new_joints[2] += [0.01 * (frame - 20), 0]  # Right shoulder
        new_joints[3] += [-0.01 * (frame - 20), 0]  # Left shoulder
        new_joints[4] += [0.02 * (frame - 20), 0]  # Right elbow
        new_joints[5] += [-0.02 * (frame - 20), 0]  # Left elbow
    elif frame < 60:
        new_joints[0] += [0, -0.01 * (frame - 40)]  # Head
        new_joints[1] += [0, -0.01 * (frame - 40)]  # Right shoulder
        new_joints[6] += [0, -0.02 * (frame - 40)]  # Right hand
        new_joints[7] += [0, -0.02 * (frame - 40)]  # Left hand

    # Plot the new positions
    ax.scatter(new_joints[:, 0], new_joints[:, 1], color='white', s=50)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=80, interval=50)

plt.show()

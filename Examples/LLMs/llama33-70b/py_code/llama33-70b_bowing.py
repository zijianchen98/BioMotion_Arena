
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 joints of the human body
joints = [
    'head', 'neck', 'right_shoulder', 'right_elbow', 'right_wrist',
    'left_shoulder', 'left_elbow', 'left_wrist', 'right_hip', 'right_knee',
    'right_ankle', 'left_hip', 'left_knee', 'left_ankle', 'torso'
]

# Define the initial positions of the joints
initial_positions = np.array([
    [0, 0],  # head
    [0, -0.1],  # neck
    [0.2, -0.2],  # right_shoulder
    [0.3, -0.4],  # right_elbow
    [0.4, -0.6],  # right_wrist
    [-0.2, -0.2],  # left_shoulder
    [-0.3, -0.4],  # left_elbow
    [-0.4, -0.6],  # left_wrist
    [0.1, -0.5],  # right_hip
    [0.1, -0.8],  # right_knee
    [0.1, -1.1],  # right_ankle
    [-0.1, -0.5],  # left_hip
    [-0.1, -0.8],  # left_knee
    [-0.1, -1.1],  # left_ankle
    [0, -0.3]  # torso
])

# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-1.2, 0.2)
    ax.set_facecolor('black')

    # Calculate the new positions of the joints based on the bowing action
    positions = initial_positions.copy()
    if frame < 30:
        # Start bowing
        positions[0, 1] -= frame * 0.01  # head
        positions[1, 1] -= frame * 0.01  # neck
        positions[12, 1] -= frame * 0.01  # left_knee
        positions[13, 1] -= frame * 0.01  # left_ankle
    elif frame < 60:
        # Continue bowing
        positions[0, 1] -= 0.3  # head
        positions[1, 1] -= 0.3  # neck
        positions[12, 1] -= 0.3  # left_knee
        positions[13, 1] -= 0.3  # left_ankle
    elif frame < 90:
        # Start standing up
        positions[0, 1] += (frame - 60) * 0.01  # head
        positions[1, 1] += (frame - 60) * 0.01  # neck
        positions[12, 1] += (frame - 60) * 0.01  # left_knee
        positions[13, 1] += (frame - 60) * 0.01  # left_ankle

    # Plot the joints
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50)

plt.show()

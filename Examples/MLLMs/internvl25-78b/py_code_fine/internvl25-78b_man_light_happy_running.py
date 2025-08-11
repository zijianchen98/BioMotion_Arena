
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the joints of the running figure
def get_joint_positions(frame):
    angle = 2 * np.pi * frame / 60
    radius = 20
    center = [50, 50]
    
    joints = np.array([
        # Head
        [50, 30],
        # Upper body
        [50, 40],
        # Right upper arm
        [60, 40],
        # Right lower arm
        [70, 40],
        # Left upper arm
        [40, 40],
        # Left lower arm
        [30, 40],
        # Pelvis
        [50, 60],
        # Right upper leg
        [60, 60],
        # Right lower leg
        [70 + 10 * np.sin(angle), 70 - 10 * np.cos(angle)],
        # Left upper leg
        [40, 60],
        # Left lower leg
        [30 - 10 * np.sin(angle), 70 - 10 * np.cos(angle)],
        # Additional points for smooth motion
        [55, 55],
        [45, 55],
        [50, 50],
        [50, 55],
        [50, 65]
    ])
    
    return joints

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
scat = ax.scatter([], [], s=100, color='white')

# Animation update function
def update(frame):
    ax.cla()
    ax.set_facecolor('black')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    joint_positions = get_joint_positions(frame)
    scat = ax.scatter(joint_positions[:, 0], joint_positions[:, 1], s=100, color='white')
    
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50)

plt.show()

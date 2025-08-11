
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the positions of the 15 joints in the first frame
joints_positions = np.array([
    [0, 0],   # head
    [0, 20],  # neck
    [-10, 40],# left shoulder
    [-20, 60],# left elbow
    [-20, 80],# left wrist
    [10, 40], # right shoulder
    [20, 60], # right elbow
    [20, 80], # right wrist
    [0, 100], # waist
    [-10, 120],# left hip
    [-20, 140],# left knee
    [-20, 160],# left ankle
    [10, 120], # right hip
    [20, 140], # right knee
    [20, 160]  # right ankle
])

# Define the initial velocity vector for each joint
velocities = np.zeros_like(joints_positions)

# Define the acceleration vector for each joint
accelerations = np.zeros_like(joints_positions)

# Define the function to update the joint positions for each frame
def update_joint_positions(frame):
    global joints_positions, velocities, accelerations
    
    # Update the joint positions based on the current velocities and accelerations
    joints_positions += velocities
    velocities += accelerations
    
    # Introduce some randomness in the accelerations to simulate a natural movement
    accelerations += np.random.normal(0, 0.1, size=accelerations.shape)
    
    # Ensure the movements are biomechanically plausible by constraining the accelerations
    accelerations = np.clip(accelerations, -1, 1)
    
    # Update the scatter plot with the new joint positions
    scat.set_offsets(joints_positions)
    
    return scat,

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 200)
ax.set_facecolor('black')

# Create a scatter plot for the joints
scat = ax.scatter(joints_positions[:, 0], joints_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_joint_positions, frames=num_frames, interval=50)

# Show the animation
plt.show()

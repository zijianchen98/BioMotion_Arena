
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions over time (example data - replace with actual motion capture data)
# Each frame contains the (x, y) coordinates of 15 joints
num_frames = 30
joint_positions = np.zeros((num_frames, 15, 2))

# Example jump motion (replace with realistic data)
for frame in range(num_frames):
    t = frame / (num_frames - 1)  # Normalized time 0 to 1
    
    # Head (1 joint)
    joint_positions[frame, 0] = [0.5 + 0.1 * np.sin(2 * np.pi * t), 0.9 + 0.2 * np.sin(2 * np.pi * t)]
    
    # Shoulders (2 joints)
    joint_positions[frame, 1] = [0.3 + 0.1 * np.sin(2 * np.pi * t), 0.7 + 0.15 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 2] = [0.7 + 0.1 * np.sin(2 * np.pi * t), 0.7 + 0.15 * np.sin(2 * np.pi * t)]
    
    # Elbows (2 joints)
    joint_positions[frame, 3] = [0.2 + 0.15 * np.sin(2 * np.pi * t), 0.5 + 0.1 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 4] = [0.8 + 0.15 * np.sin(2 * np.pi * t), 0.5 + 0.1 * np.sin(2 * np.pi * t)]

    # Hips (2 joints)
    joint_positions[frame, 5] = [0.35 + 0.05 * np.sin(2 * np.pi * t), 0.4 + 0.1 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 6] = [0.65 + 0.05 * np.sin(2 * np.pi * t), 0.4 + 0.1 * np.sin(2 * np.pi * t)]

    # Knees (2 joints)
    joint_positions[frame, 7] = [0.3 + 0.1 * np.sin(2 * np.pi * t), 0.2 + 0.2 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 8] = [0.7 + 0.1 * np.sin(2 * np.pi * t), 0.2 + 0.2 * np.sin(2 * np.pi * t)]
    
     # Ankles (2 joints)
    joint_positions[frame, 9] = [0.3 + 0.15 * np.sin(2 * np.pi * t), 0.05 + 0.05 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 10] = [0.7 + 0.15* np.sin(2 * np.pi * t), 0.05 + 0.05 * np.sin(2 * np.pi * t)]
    
    # Wrists
    joint_positions[frame, 11] = [0.1 + 0.15 * np.sin(2 * np.pi * t), 0.45 + 0.05 * np.sin(2 * np.pi * t)]
    joint_positions[frame, 12] = [0.9 + 0.15 * np.sin(2 * np.pi * t), 0.45 + 0.05 * np.sin(2 * np.pi * t)]
    
    # Feet
    joint_positions[frame, 13] = [0.2 + 0.05 * np.sin(2* np.pi *t), 0]
    joint_positions[frame, 14] = [0.8 + 0.05 * np.sin(2* np.pi *t), 0]

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 1]) # Adjust limits as needed
ax.set_ylim([0, 1])
ax.set_aspect('equal')  # Maintain aspect ratio
ax.set_facecolor('black')

# Initialize the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')



# Animation update function
def update(frame):
    x = joint_positions[frame, :, 0]
    y = joint_positions[frame, :, 1]
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)


plt.show()

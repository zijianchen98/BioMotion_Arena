
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights representing the bowing happyman
initial_positions = {
    'head': [0, 1],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, -0.5],
    'right_elbow': [1, -0.5],
    'left_wrist': [-1.5, -1.5],
    'right_wrist': [1.5, -1.5],
    'left_hip': [-0.5, -1],
    'right_hip': [0.5, -1],
    'left_knee': [-0.75, -2],
    'right_knee': [0.75, -2],
    'left_ankle': [-1, -3],
    'right_ankle': [1, -3],
}

# Convert the dictionary to a list of positions
positions = np.array(list(initial_positions.values()))

# Define the angles for the bowing motion
angles = np.linspace(0, np.pi/4, 100)

# Function to update the positions of the point-lights based on the angle
def update_bowing(angle):
    global positions
    # Bowing motion mainly affects the upper body
    positions[0] = [0, 1 - 0.2 * np.sin(angle)]  # head
    positions[1] = [-0.5 + 0.2 * np.cos(angle), 0.5 - 0.2 * np.sin(angle)]  # left shoulder
    positions[2] = [0.5 - 0.2 * np.cos(angle), 0.5 - 0.2 * np.sin(angle)]  # right shoulder
    positions[3] = [-1 + 0.4 * np.cos(angle), -0.5 - 0.4 * np.sin(angle)]  # left elbow
    positions[4] = [1 - 0.4 * np.cos(angle), -0.5 - 0.4 * np.sin(angle)]  # right elbow
    positions[5] = [-1.5 + 0.6 * np.cos(angle), -1.5 - 0.6 * np.sin(angle)]  # left wrist
    positions[6] = [1.5 - 0.6 * np.cos(angle), -1.5 - 0.6 * np.sin(angle)]  # right wrist
    
def animate(i):
    ax.clear()
    update_bowing(angles[i])
    ax.scatter(positions[:, 0], positions[:, 1], c='white', s=10)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-4, 2)
    ax.axis('off')

fig, ax = plt.subplots(figsize=(5, 8))
ani = animation.FuncAnimation(fig, animate, frames=len(angles), interval=50, repeat=True)
plt.show()

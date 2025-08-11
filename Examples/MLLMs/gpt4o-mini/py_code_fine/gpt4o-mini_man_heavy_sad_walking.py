
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sadman_walk(frame):
    plt.clf()
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.gca().set_facecolor('black')

    # Simulate the positions of point lights
    # Initial position of the joints
    base_height = 0
    move_y = np.sin(frame / 10.0) * 0.2   # up and down motion
    move_x = (frame % 60) / 10.0 - 3      # forward motion
    
    # Define the skeleton joint locations
    joints = np.array([
        [0, base_height + 2 + move_y],     # Head
        [-0.5, base_height + 1.5],         # Left shoulder
        [0.5, base_height + 1.5],          # Right shoulder
        [0, base_height + 1],               # Chest
        [-1, base_height],                   # Left hand
        [1, base_height],                    # Right hand
        [-0.5, base_height - 1.5],         # Left hip
        [0.5, base_height - 1.5],          # Right hip
        [-1, base_height - 3],              # Left leg
        [1, base_height - 3],               # Right leg
        [0, base_height - 4],               # Feet
        [-1.5, base_height - 1.5 + move_y], # Rolling weight
        [1.5, base_height - 1.5 + move_y]  # Phantom of the weight
    ])

    # Draw the points
    for joint in joints:
        plt.plot(joint[0] + move_x, joint[1], 'o', color='white', markersize=8)

# Create a figure for animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, sadman_walk, frames=100, interval=50)
plt.show()

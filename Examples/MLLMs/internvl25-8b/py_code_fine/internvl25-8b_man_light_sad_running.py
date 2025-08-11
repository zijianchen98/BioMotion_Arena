
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize a figure with a black background
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Hide the axis

# Define the joints and their starting positions
joints = [(1, 5), (5, 4), (4, 3), (3, 2), (6, 4), (7, 5), (8, 5), (9, 5), (10, 4), (11, 3), (12, 2)]
positions = [(j, 0) for j in joints]

# Create the point-light patches
patches = [plt.Circle(position, 0.15, facecolor='white', edgecolor='none') for position in positions]

# Function to update the positions of the joints
def update_positions(i):
    global positions
    
    # Define the running motion parameters
    timing = [0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.25, 0.2, 0.2, 0.1, -0.05, 0, 0]
    
    # Update positions based on timing
    new_positions = []
    for j, pos in zip(joints, positions):
        for t in range(len(joints)):
            if i % (len(joints) // len(timing)) == t:
                if timing[i % len(timing)] > 0:
                    dx = np.sin(joints.index(j) * 2 * np.pi * timing[i % len(timing)] / len(timing)) * 0.1
                else:
                    dx = 0
                new_pos = pos[0] + dx, pos[1]
                new_positions.append(new_pos)
                break
        else:
            # If no relevant timing parameter is found, stay at current position
            new_positions.append(pos)
    
    positions = new_positions
    
    # Update the positions of the patches
    for patch, (x, y) in zip(patches, positions):
        patch.center = (x, y)
    
    return patches

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=250, interval=50)
plt.show()

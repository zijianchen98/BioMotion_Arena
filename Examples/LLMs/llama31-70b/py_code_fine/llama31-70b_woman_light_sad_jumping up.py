
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
n_points = 15
n_frames = 100

# Define the initial positions of the point-lights
# These positions are chosen to represent a woman with a lightweight
# The points are ordered to represent the following body parts:
#   1-2: head
#   3-4: torso
#   5-6: left arm
#   7-8: right arm
#   9-10: left leg
#   11-12: right leg
#   13-14: left foot
#   15: right foot
initial_positions = np.array([
    [0, 0.5],  # head
    [0, 0.4],
    [-0.1, 0.3],  # torso
    [0.1, 0.3],
    [-0.2, 0.2],  # left arm
    [-0.3, 0.1],
    [0.2, 0.2],  # right arm
    [0.3, 0.1],
    [-0.1, 0.0],  # left leg
    [-0.2, -0.1],
    [0.1, 0.0],  # right leg
    [0.2, -0.1],
    [-0.2, -0.3],  # left foot
    [-0.3, -0.4],
    [0.2, -0.3],  # right foot
])

# Define the movement of each point-light
# The movement is defined as a function of time (frame number)
def move_points(frame):
    positions = initial_positions.copy()
    
    # Move the head up and down
    positions[0, 1] += 0.1 * np.sin(frame / 10.0)
    positions[1, 1] += 0.1 * np.sin(frame / 10.0)
    
    # Move the torso up and down
    positions[2, 1] += 0.05 * np.sin(frame / 10.0)
    positions[3, 1] += 0.05 * np.sin(frame / 10.0)
    
    # Move the arms up and down
    positions[4, 1] += 0.1 * np.sin(frame / 10.0)
    positions[5, 1] += 0.1 * np.sin(frame / 10.0)
    positions[6, 1] += 0.1 * np.sin(frame / 10.0)
    positions[7, 1] += 0.1 * np.sin(frame / 10.0)
    
    # Move the legs up and down
    positions[8, 1] += 0.2 * np.sin(frame / 10.0)
    positions[9, 1] += 0.2 * np.sin(frame / 10.0)
    positions[10, 1] += 0.2 * np.sin(frame / 10.0)
    positions[11, 1] += 0.2 * np.sin(frame / 10.0)
    
    # Move the feet up and down
    positions[12, 1] += 0.1 * np.sin(frame / 10.0)
    positions[13, 1] += 0.1 * np.sin(frame / 10.0)
    positions[14, 1] += 0.1 * np.sin(frame / 10.0)
    
    return positions

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=10, c='white')

# Define the animation function
def animate(frame):
    positions = move_points(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, blit=True, interval=50)

plt.show()

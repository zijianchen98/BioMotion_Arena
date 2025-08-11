
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
width, height = 10, 6
frames = 100

# Function to create point positions for lying down action
def get_positions(frame):
    # Center the position of the sadman
    positions = np.zeros((num_points, 2))

    # Define coordinates for the point lights representing limbs and head
    head = np.array([5, 5])
    torso = np.array([5, 4])
    left_arm = np.array([4, 4])
    right_arm = np.array([6, 4])
    left_leg = np.array([4.5, 2])
    right_leg = np.array([5.5, 2])
    
    # Add slight vertical movement for realism
    vertical_movement = 0.1 * np.sin(2 * np.pi * frame / frames)

    # Assign calculated positions
    positions[0] = head + [0, vertical_movement]
    positions[1] = torso + [0, vertical_movement]
    positions[2] = left_arm + [0, vertical_movement]
    positions[3] = right_arm + [0, vertical_movement]
    positions[4] = left_leg + [0, vertical_movement]
    positions[5] = right_leg + [0, vertical_movement]

    # Additional points for more detail (e.g., knees, feet)
    positions[6:] = np.array([
        [4, 4], [5, 4], [4, 5], [6, 5], [6, 3],
        [5, 3], [4, 3], [6, 2], [4, 2]
    ]) + [0, vertical_movement]

    return positions

# Create a figure and axes
fig, ax = plt.subplots(figsize=(width, height))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Create point lights
points, = ax.plot([], [], 'o', color='white', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    positions = get_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=100)

# Display the animation
plt.show()

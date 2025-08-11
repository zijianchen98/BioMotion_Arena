
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point-light coordinates for "sitting down" action
def get_sitting_down_positions(frame):
    # Initial positions of the point-lights
    base_positions = np.array([
        [0, 1],    # Head
        [-0.5, 0.5], [0.5, 0.5],  # Shoulders
        [-0.5, 0], [0.5, 0],  # Hips
        [-0.4, -0.5], [0.4, -0.5],  # Knees
        [-0.2, -1], [0.2, -1],  # Feet
        [0.3, 0.5], [-0.3, 0.5],  # Elbows
        [0.3, 0], [-0.3, 0]  # Wrists
    ])

    # Adjust the y-coordinates to simulate the sitting motion
    sitting_motion_offset = np.clip(frame / 20, 0, 1)  # Normalize to range [0,1]
    
    # Apply offset to create a smooth movement
    for i in range(len(base_positions)):
        base_positions[i][1] -= sitting_motion_offset * 0.5  # Half the sitting down motion

    return base_positions

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create a scatter plot for point-lights
point_lights, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    point_lights.set_data([], [])
    return point_lights,

# Animation function
def animate(frame):
    positions = get_sitting_down_positions(frame)
    point_lights.set_data(positions[:, 0], positions[:, 1])
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 40), init_func=init,
                              interval=100, blit=True)

# Display the animation
plt.show()

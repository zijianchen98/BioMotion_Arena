
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4],
    [-1, 3], [1, 3],
    [-2, 2], [-1, 2], [0, 2], [1, 2], [2, 2],
    [-1, 0], [1, 0],
    [-1, -2], [1, -2],
    [0, -4]
])

# Number of frames in the animation
num_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 7)
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background color to black
points, = ax.plot([], [], 'wo', markersize=8)

# Function to update the positions of the point lights for each frame
def update(frame):
    y_offset = 2 * np.sin(frame * np.pi / 30)  # Simulate jumping motion
    
    # Simulate head movement, it moves slower when going up.
    head_y_offset = np.sin(frame * np.pi / 40) * 0.5 if frame<30 else np.sin(frame * np.pi / 10) * 0.5
    
    # Simulate arm movement
    arm_y_offset = np.sin(frame * np.pi / 20)
    
    new_positions = initial_positions.copy()

    # Apply the jump offset
    new_positions[:, 1] = initial_positions[:, 1] + y_offset
    
    # Apply head offset
    new_positions[0:3, 1] = initial_positions[0:3, 1] + head_y_offset
    
    # Apply the arm offset to shoulders, elbows, and hands
    new_positions[3:5, 1] = initial_positions[3:5, 1] + arm_y_offset
    new_positions[5:10, 1] = initial_positions[5:10, 1] + arm_y_offset

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval=40, repeat=False)

# Display or save the animation
plt.show()


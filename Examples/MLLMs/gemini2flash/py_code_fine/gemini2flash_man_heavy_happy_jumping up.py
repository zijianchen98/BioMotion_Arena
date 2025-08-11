
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the duration of the animation (in frames)
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left shoulder
    [2, 8],  # Right shoulder
    [-4, 6],  # Left elbow
    [4, 6],  # Right elbow
    [-5, 4],  # Left hand
    [5, 4],  # Right hand
    [-1, 6],  # Left hip
    [1, 6],  # Right hip
    [-2, 4],  # Left knee
    [2, 4],  # Right knee
    [-2, 2],  # Left foot
    [2, 2],  # Right foot
    [0, 6.5],  # Torso top
    [0, 3.5]   # Torso bottom
])

# Define the jumping motion of the point-lights
def update_points(frame_num, points):
    # Scale the jump height based on the frame number
    jump_height = np.sin(frame_num / num_frames * np.pi) * 3

    # Update the positions of the point-lights
    new_positions = initial_positions.copy()
    new_positions[:, 1] += jump_height

    # Add a slight swaying motion
    sway_amount = np.sin(frame_num / num_frames * 2 * np.pi) * 0.5
    new_positions[:, 0] += sway_amount

    # Update the positions of the point-lights
    points.set_offsets(new_positions)

    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(0, 15)
ax.set_aspect('equal')
plt.axis('off')

# Create the point-lights
points = ax.plot([], [], 'wo', markersize=8)[0]
points.set_data(initial_positions[:, 0], initial_positions[:, 1])

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,),
                              interval=50, blit=True, save_count=num_frames)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 50
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [0, 5],  # Head
    [-1, 4], [1, 4],  # Shoulders
    [-1.5, 3], [1.5, 3], # Elbows
    [-2, 2], [2, 2], # Wrists
    [-0.5, 3], [0.5, 3],  # Hips
    [-0.75, 1], [0.75, 1],  # Knees
    [-1, 0], [1, 0], # Ankles
    [-0.5, 0], [0.5, 0]   # Feet
])


# Define the animation function
def update_points(frame_num, points):
    # Define the motion of the points
    x_motion = np.array([
        0,        0,      0,
        0,       0,       0,    0,
        0,      0,
        0,     0,
        0,    0,
        0,     0
    ])
    
    
    y_motion = np.array([
        0.3 * np.sin(frame_num * 0.1), 0.1 * np.sin(frame_num * 0.1), 0.1 * np.sin(frame_num * 0.1),
        0.2 * np.sin(frame_num * 0.1 + 0.5), 0.2 * np.sin(frame_num * 0.1 + 0.5),
        0.1 * np.sin(frame_num * 0.1 + 1), 0.1 * np.sin(frame_num * 0.1 + 1),
        0.6 * np.sin(frame_num * 0.1), 0.6 * np.sin(frame_num * 0.1),
        0.8 * np.sin(frame_num * 0.1 + 0.5), 0.8 * np.sin(frame_num * 0.1 + 0.5),
        1.0 * np.sin(frame_num * 0.1 + 1), 1.0 * np.sin(frame_num * 0.1 + 1),
        1.0 * np.sin(frame_num * 0.1 + 1), 1.0 * np.sin(frame_num * 0.1 + 1)
    ])
    
    new_positions = initial_positions + np.stack([x_motion, y_motion], axis=1)
    
    # Update the positions of the points
    points.set_offsets(new_positions)
    return points,


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
plt.axis('off')

# Create the points
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), frames=num_frames, interval=50, blit=False, repeat=True)

# Show the animation
plt.show()

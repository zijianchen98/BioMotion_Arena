
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-1, 1], [0, 1], [0, 0]
])


# Function to update the positions of the point-lights for each frame
def update(frame_num, data, points):
    # Simple forward rolling animation (replace with more sophisticated model if needed)
    x_shift = 0.1 * frame_num
    y_shift = 0.05 * frame_num
    rotated_positions = np.copy(initial_positions)
    rotated_positions[:,0] += x_shift
    rotated_positions[:,1] += y_shift

    # Adjust positions based on the frame number to simulate rolling
    for i, pos in enumerate(rotated_positions):
        angle = 0.1*frame_num  # adjust rotation speed here.
        if i in [1, 2, 3, 5, 6, 7, 9, 10, 11]: #these should rotate
            rotated_pos = np.array([pos[0],pos[1]])
            rotated_pos = np.array([pos[0]*np.cos(angle) - pos[1]*np.sin(angle),
                                     pos[0]*np.sin(angle) + pos[1]*np.cos(angle)])
            rotated_positions[i] = rotated_pos
        

    # Keep the point-lights within bounds (adjust as needed)
    rotated_positions[:, 0] = np.clip(rotated_positions[:, 0], -5, 5)
    rotated_positions[:, 1] = np.clip(rotated_positions[:, 1], -5, 5)
    

    points.set_data(rotated_positions[:, 0], rotated_positions[:, 1])
    return points,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')  # Ensure circles are round
ax.set_facecolor('black')  # Set background color to black

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(initial_positions, points), frames=range(100), interval=50)  # Adjust frames and interval as needed

# Show the animation
plt.show()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the duration of the animation
num_frames = 10
frame_duration = 0

# Define the number of points and their initial positions
num_points = 15
initial_positions = np.array([
    [0,  5], [ 5, -5], (-5, -5], (-5,  5],
    [ 3,  7], ( 7,  3], (-3,  7], (-7,  3],
    ( 1,  9], ( 9,  1], (-1,  9], (-9,  1],
    ( 0, 11], (11,   )
])

# Define the function to update the positions of the points
def update_points(num, points, angles):
    for i in range(num_points):
        angle = angles[i]
        points[i].set_data(initial_positions[i, 0] * np.cos(angle), initial_positions[i, 1] * np.sin(angle))
    return points

# Generate the angles for the points to follow a circular path
angles = np.linspace(0, 2 * np.pi * num_frames, num_frames, endpoint=False)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.fill([0, 15, 15, 1, 1], [15, 15, 1, 1, 15], 'k')  # Solid black background

# Create the point objects
points = [plt.plot([], [], 'w.', ms=10)[0] for _ in range(num_points)]

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, fargs=(points, angles), interval=int(frame_duration * 1000), blit=True)

# Show the animation
plt.show()

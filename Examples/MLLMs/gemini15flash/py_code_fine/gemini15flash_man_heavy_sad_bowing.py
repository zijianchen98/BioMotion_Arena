
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 5], [ -1, 4], [0, 4], [1, 4], [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2], [-0.5, 1], [0.5, 1], [0, 0]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Function to update the positions of the point lights
def update_positions(frame_num, points, positions):
    # Simulate bowing motion (adjust parameters for desired effect)
    for i in range(len(positions)):
        angle = frame_num * dt * 0.2 # Adjust speed here
        x_offset = 0.5 * np.sin(angle)  # Adjust amplitude here
        y_offset = 0.5 + 0.5 * np.cos(angle) # Adjust amplitude here

        if i<5: #upper body
            positions[i,0] += x_offset * 0.7
            positions[i,1] += y_offset *0.7

        elif i>=5 and i<10: #lower body
            positions[i,0] += x_offset *0.5
            positions[i,1] += y_offset * 0.5
        else:#legs
            positions[i,0] += x_offset *0.3
            positions[i,1] += y_offset * 0.3

    points.set_offsets(positions)
    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-4, 4])
ax.set_ylim([-1, 6])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
points, = ax.plot(initial_positions[:, 0], initial_positions[:, 1], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(points, initial_positions.copy()),
                              frames=num_frames, interval=50, blit=True)


# Save the animation (optional)
#ani.save('bowing_animation.gif', writer='imagemagick', fps=20)

plt.show()


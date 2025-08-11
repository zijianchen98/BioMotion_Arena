
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialize point locations
num_points = 15
point_positions = np.zeros((2, num_points))  # Shape (2, num_points)

# Initialize positions for a waving hand animation
def init():
    points.set_data([], [])
    return points,

# function to update the points for each frame
def update(frame):
    # Adjust the Y position to simulate waving
    wave_amplitude = 0.5 * np.sin(frame * 0.1)
    
    # Points for the body
    point_positions[:, 0:10] = [[0, 0], [-0.5 + wave_amplitude, 0]]  # head and body
    point_positions[:, 10] = [0.5, -0.5 + wave_amplitude]  # right hand
    point_positions[:, 11:] = [[-0.5, -0.7], [0.5, -0.7]]    # legs
    return points.set_data(point_positions[0], point_positions[1])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

plt.show()

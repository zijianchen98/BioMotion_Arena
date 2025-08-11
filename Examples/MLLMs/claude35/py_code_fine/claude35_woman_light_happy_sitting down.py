
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
frames = 60
point_positions = np.zeros((frames, num_points, 2))

# Base positions for a 'sitting down' motion
# Configuring the positions of point-lights for the sitting action
for i in range(num_points):
    if i < 5:  # Head area
        point_positions[:, i, 0] = 0  # X position stays constant
        point_positions[:, i, 1] = 5 - i  # Y positions decrease for 'head'
    elif 5 <= i < 10:  # Shoulder to waist area
        point_positions[:, i, 0] = -(i-5) / 2  # Moving outward slightly
        point_positions[:, i, 1] = 3  # Constant height for 'waist'
    else:  # Legs area
        point_positions[:, i, 0] = -(i-10) / 2  # Leg positions
        point_positions[:, i, 1] = 1 - (i-10) * 0.5  # Moving down

# Creating a black background
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 6)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)  # White point-lights

def init():
    points.set_data([], [])
    return points,

def animate(i):
    points.set_data(point_positions[i, :, 0], point_positions[i, :, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=100, blit=True)

# Display the animation
plt.show()

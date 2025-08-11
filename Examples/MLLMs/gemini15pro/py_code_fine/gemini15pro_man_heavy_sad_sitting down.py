
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4],  # Head
    [-2, 3], [2, 3], [-1, 3], [1, 3],  # Shoulders, Neck
    [-3, 2], [3, 2], [-2, 2], [2, 2], # Elbows, Chest
    [-2, 0], [2, 0], # Hips
    [-2,-2], [2, -2]   # Knees
])


# Define the movement function for sitting down
def sit_down(t):
    positions = initial_positions.copy()
    # Adjust vertical positions to simulate sitting
    sit_amount = -2 * (1 - np.cos(np.pi * t / 20)) if t < 20 else -4  # smooth sitting motion
    positions[:, 1] += sit_amount 
    
    return positions

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 8)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the point lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the animation function
def animate(i):
    positions = sit_down(i)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=40, interval=50, blit=True)


# To save the animation, uncomment the following lines
# writer = animation.FFMpegWriter(fps=20) # Adjust fps as needed
# ani.save('sitting_animation.mp4', writer=writer)


plt.show()



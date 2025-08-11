
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the positions of the point-lights
def get_point_positions(frame):
    # Initial static positions of the point-lights (15 in total)
    initial_positions = np.array([
        [0, 5], [1, 6], [-1, 6], 
        [0, 7], [1, 8], [-1, 8], 
        [0, 8.5], [0.5, 9], [-0.5, 9],
        [0, 9.5], [1, 10.5], [-1, 10.5], 
        [0, 11], [0.5, 12], [-0.5, 12], 
        [0, 13]
    ])
    
    # Calculate the jumping motion (a simple parabola for jumping)
    t = frame / 20.0  # normalized time
    jump_height = -4 * (t - 0.5)**2 + 4  # parabola for arc of jump
    height_adjusted_positions = initial_positions + np.array([[0, jump_height]] * len(initial_positions))

    return height_adjusted_positions

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(0, 15)
ax.set_facecolor('black')

# Create a scatter plot for the point-lights
points, = ax.plot([], [], 'o', color='white')

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(frame):
    positions = get_point_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Display the animation
plt.show()

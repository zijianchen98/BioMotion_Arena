
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the figure and axis
fig, ax = plt.subplots()

# Set the background to black and remove axes
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Define number of points
num_points = 15

# Define positions of each point (representing body joints)
point_positions = np.array([
    [5, 8],   # Head
    [4.5, 7], [5.5, 7],  # Shoulders
    [4, 6], [6, 6],  # Elbows
    [3.5, 5], [6.5, 5],  # Hands
    [4, 3], [6, 3],  # Hips
    [4, 1], [6, 1],  # Knees
    [4, 0], [6, 0],  # Feet end position
])

# Create scatter points on the plot
points, = ax.plot([], [], 'wo', markersize=10)

# Initialization function for the animation
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    # Create a wave motion effect for the points
    # Oscillate y-coordinates
    y_offsets = 0.2 * np.sin(0.1 * frame + np.linspace(0, num_points-1, num_points))
    new_positions = point_positions + np.column_stack((np.zeros(num_points), y_offsets))
    
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), init_func=init,
                              interval=50, blit=True)

# Show the animation
plt.show()

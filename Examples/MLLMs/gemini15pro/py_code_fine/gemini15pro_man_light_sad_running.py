
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point lights.
# These coordinates are just placeholders and need to be adjusted 
# to accurately represent the running motion.
points = np.array([
    [0, 100], [10, 90], [20, 100],  # Head
    [-10, 80], [30, 80],               # Shoulders
    [-20, 60], [40, 60],               # Elbows
    [-30, 40], [50, 40],               # Wrists
    [0, 60],                           # Center of body
    [0, 30],                           # Hip
    [-10, 0], [20, 0],                 # Knees
    [-20, -20], [30, -20]             # Ankles
])

# Number of frames in the animation
num_frames = 50

# Create figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-50, 100])
ax.set_ylim([-50, 120])
ax.set_facecolor('black')

# Create the point light scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], s=20, c='white')

# Initialize animation function
def animate(i):
    # Update the coordinates of the point lights for each frame.
    # This example provides a simple up and down movement.
    # Replace this with your actual running motion logic.
    y_offset = 10 * np.sin(2 * np.pi * i / num_frames)
    new_points = points.copy()
    new_points[:, 1] += y_offset
    scatter.set_offsets(new_points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation (or save it)
plt.show()

# To save the animation as a gif, uncomment the following line
# ani.save('running_animation.gif', writer='imagemagick', fps=20) 

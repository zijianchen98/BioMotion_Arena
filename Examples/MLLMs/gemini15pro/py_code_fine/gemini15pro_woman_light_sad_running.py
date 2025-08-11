
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights for a single frame
# (Replace these with actual coordinates from motion capture data or other sources)
# This example creates a static pose, you'll need to update these for animation
points = np.array([
    [0, 10], [1, 8], [2, 10],  # Head points
    [-1, 5], [1, 5],  # Shoulder points
    [-2, 2], [2, 2], # Elbow points
    [-2, -1], [2, -1],  # Hand points
    [0, 2],  # Body center point
    [-1, -3], [1, -3],  # Hip points
    [-1, -7], [1, -7],  # Knee points
    [-1, -10], [1, -10]  # Ankle points
])



fig, ax = plt.subplots()

# Initialize the scatter plot for the point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Set plot limits and background color
ax.set_xlim(-5, 5)
ax.set_ylim(-12, 12)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])



# Animation update function (currently does nothing, needs implementation)

def animate(i):
    # Placeholder for updating point coordinates
    # Example: Move points slightly to the right 
    # In a real application, you would calculate the position of points based on the frame number 'i' and the action 
    updated_points = points.copy()
    return scatter,



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(30), blit=True, interval=50) #frames=range(30) means that there would be 30 frames in the animation
#ani.save('running_animation.gif', writer='pillow', fps=15) #uncomment to save the file

# Or to display it in a jupyter notebook

from IPython.display import HTML

# Show animation in Jupyter notebook
HTML(ani.to_jshtml())

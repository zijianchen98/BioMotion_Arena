
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or a more sophisticated animation model
num_frames = 60  # Number of frames in the animation
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Head movement (point 0) - subtle nodding
x[0, :] = 0 + np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 2
y[0, :] = 100 + np.cos(np.linspace(0, 2 * np.pi, num_frames)) * 2
# ... similar definitions for other 14 points based on motion



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-50, 50)  # Adjust limits as needed
ax.set_ylim(0, 150)  # Adjust limits as needed
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black

# Create the point-light scatter plot
points = ax.scatter([], [], s=20, c='white')

# Define the animation update function
def update(frame):
    points.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True) #20ms = 50fps

# Display the animation or save it to a file
plt.show()
# To save as a gif:
# ani.save('sadman_turning_around.gif', writer='pillow')



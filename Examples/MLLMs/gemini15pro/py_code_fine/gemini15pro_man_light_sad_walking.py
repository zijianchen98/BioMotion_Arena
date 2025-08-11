
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be replaced with actual motion capture data or a more sophisticated animation model
# for realistic biological motion.
# The structure of this data is: frames x point-lights x coordinates (x, y)

num_frames = 60
num_points = 15

# Initialize data with some random movement for demonstration
data = np.random.rand(num_frames, num_points, 2) * 400

# Center the data around the middle of the figure
data[:,:,0] += 100 
data[:,:,1] += 200

# Create the figure and axes
fig, ax = plt.subplots()

# Set the limits of the plot to encompass the motion
ax.set_xlim([0, 600])  # Adjust as needed based on your data range
ax.set_ylim([0, 800])  # Adjust as needed based on your data range
ax.set_aspect('equal')  # Ensure equal aspect ratio so the motion isn't distorted
ax.set_facecolor('black')


# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')


# Define the animation update function
def update(frame):
    scatter.set_offsets(data[frame])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True) # interval controls the speed, blit=True optimizes for performance


# Display the animation (for notebooks or interactive environments)
plt.show()


# Save the animation (optional - uncomment to save as a gif or mp4)
# ani.save('sadman_walking.gif', writer='pillow', fps=30) # Requires pillow library
#ani.save('sadman_walking.mp4', writer='ffmpeg', fps=30) # Requires ffmpeg




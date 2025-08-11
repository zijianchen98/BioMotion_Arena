
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point lights over time
# This is a simplified example and would need to be refined for realistic motion
num_frames = 60  # Number of frames in the animation

# Initialize point coordinates for each frame
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))


# Example: Head (point 0) moving slightly during bowing
x[0, :] = 0  # Head x stays constant
y[0, :] = 20 - 2 * np.sin(np.linspace(0, np.pi / 2, num_frames)) # Head dips slightly



# Example: Shoulders (points 1, 2)
x[1, :] = -5
y[1, :] = 15 - np.sin(np.linspace(0, np.pi / 2, num_frames)) # Shoulders move down
x[2, :] = 5
y[2, :] = 15 - np.sin(np.linspace(0, np.pi / 2, num_frames))


# Torso
x[3, :] = -3
y[3, :] = 10 
x[4, :] = 3
y[4, :] = 10
x[5, :] = 0
y[5, :] = 12

# Hips
x[6, :] = -3
y[6, :] = 5
x[7, :] = 0
y[7, :] = 7
x[8, :] = 3
y[8, :] = 5

# Knees
x[9, :] = -2
y[9, :] = 0
x[10, :] = 2
y[10, :] = 0

# Feet
x[11, :] = -2
y[11, :] = -5
x[12, :] = 2
y[12, :] = -5

# Hands: moving down and a bit forward during bowing
x[13, :] = -7 + np.sin(np.linspace(0, np.pi / 2, num_frames))
y[13, :] = 10 - 2 * np.sin(np.linspace(0, np.pi / 2, num_frames))

x[14, :] = 7 - np.sin(np.linspace(0, np.pi / 2, num_frames))
y[14, :] = 10 - 2 * np.sin(np.linspace(0, np.pi / 2, num_frames))



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 25)
ax.set_aspect('equal')  # Ensure correct aspect ratio
ax.set_facecolor('black') # Set background to black
ax.set_xticks([])
ax.set_yticks([])

# Initialize the point light scatter plot
scatter = ax.scatter([], [], s=20, c='white')  # Larger marker size


# Animation update function
def update(frame):
    scatter.set_offsets(np.c_[x[:, frame], y[:, frame]])
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval=30)  # Adjust interval for speed

# For saving
writer = animation.PillowWriter(fps=25) # adjust fps here
ani.save('bowing_animation.gif', writer=writer)


# For displaying (uncomment the next line if you want a display window)
#plt.show()



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint positions over time (replace with your actual motion data)
# This is a simplified example, you'll need to adjust these values
# to achieve the desired "bowing" motion

num_frames = 60  # Number of frames in the animation
t = np.linspace(0, 2 * np.pi, num_frames)  # Time variable

# Initialize joint positions
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Head
x[0, :] = 0  # Example: Head stays still
y[0, :] = 5

# Shoulders and elbows (Simplified bowing motion)
shoulder_y_offset = 0.5 * np.sin(t)
elbow_y_offset = 0.3 * np.sin(t + np.pi/4)

x[[1, 2], :] = [-1, 1]
y[[1, 2], :] = 4 + shoulder_y_offset


x[[3, 4], :] = [-1.5, 1.5]
y[[3, 4], :] = 3 + elbow_y_offset



# Hips, knees and ankles

x[[5,6],:] = [-0.6,0.6]
y[[5,6],:] = 2.5


x[[7,8],:] = [-0.8,0.8]
y[[7,8],:] = 1



x[[9,10],:] = [-0.4,0.4]
y[[9,10],:] = 0.0



# Feet
x[[11, 12], :] = [-0.8, 0.8]  # Example: Feet stay relatively still
y[[11, 12], :] = -0.5



x[[13, 14], :] = [-0.4, 0.4]  # Example: Feet stay relatively still
y[[13, 14], :] = -0.5



# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim([-2, 2])
ax.set_ylim([-1, 6])
ax.set_aspect('equal')
ax.set_xticks([])  # Remove x-axis ticks
ax.set_yticks([])  # Remove y-axis ticks


# Initialize the points
points, = ax.plot([], [], 'wo', markersize=8)


# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)  # 30ms interval for smoother motion

# For displaying in Jupyter Notebook (optional)
# from IPython.display import HTML
# HTML(ani.to_jshtml())

plt.show()



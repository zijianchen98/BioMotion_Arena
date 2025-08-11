
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generaterunning_motion(num_points, num_frames, weight=1):
    # This function generates the running motion for the point-lights.
    t = np.linspace(0, 10, num_frames)
    x = 5 * np.sin(t)  # Simulate running in place
    y = 0.5 * np.sin(2 * t)  # Simulate a slight bounce

    # Adding the effect of heavy weight on the shoulders
    x += 0.1 * weight * np.sin(t + np.pi/4)
    y -= 0.1 * weight * np.sin(t + np.pi/4)

    # Generating positions for multiple light points
    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x_rotated = x[:, np.newaxis] + np.cos(angles) * np.linspace(0, 2, num_points)
    y_rotated = y[:, np.newaxis] + np.sin(angles) * np.linspace(0, 2, num_points)

    return x_rotated, y_rotated

def update(frame):
    global scat
    scat.set_offsets(np.column_stack((pos_x[frame], pos_y[frame])))
    return scat,

# Parameters
num_points = 15  # Number of point-lights
num_frames = 200  # Number of frames in the animation
weight = 2  # Heaviness of the weight

# Generate the motion
pos_x, pos_y = generaterunning_motion(num_points, num_frames, weight)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.set_title('Running Sadman with Heavy Weight')
ax.axis('off')

# Create the scatter plot
scat = ax.scatter(pos_x[0], pos_y[0], c='white', s=50)

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

plt.show()

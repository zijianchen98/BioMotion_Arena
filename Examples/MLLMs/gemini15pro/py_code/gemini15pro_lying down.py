
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Head (top point) remains stationary
x[0, :] = 200
y[0, :] = 450

# Example: Other points move slightly
for i in range(1, 15):
    x[i, :] = 200 + 20 * np.sin(2 * np.pi * i / 15 + np.linspace(0, 2 * np.pi, num_frames))
    y[i, :] = 400 - 50 * i / 15 + 10 * np.cos(2 * np.pi * i / 15 + np.linspace(0, 2 * np.pi, num_frames))


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 400)  # Set limits so points are visible
ax.set_ylim(0, 500)
ax.set_aspect('equal')  # Maintain aspect ratio
ax.set_facecolor('black')  # Set background to black
points, = ax.plot([], [], 'wo')


# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save or display the animation
# ani.save('lying_down.gif', writer='pillow') # Uncomment to save as gif
plt.show()


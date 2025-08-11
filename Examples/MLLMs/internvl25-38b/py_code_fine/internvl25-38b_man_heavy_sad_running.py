
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Function to update the position of the points
def update(frame, points):
    time = frame * 0.1  # Time for the animation
    x = np.array([
        np.sin(time),
        np.cos(time),
        np.sin(time + np.pi/4),
        np.cos(time + np.pi/4),
        np.sin(time + np.pi/2),
        np.cos(time + np.pi/2),
        np.sin(time + 3*np.pi/4),
        np.cos(time + 3*np.pi/4),
        np.sin(time + np.pi),
        np.cos(time + np.pi),
        np.sin(time + 5*np.pi/4),
        np.cos(time + 5*np.pi/4),
        np.sin(time + 3*np.pi/2),
        np.cos(time + 3*np.pi/2),
        np.sin(time + 7*np.pi/4),
        np.cos(time + 7*np.pi/4),
    ])

    y = np.array([
        np.cos(time),
        np.sin(time),
        np.cos(time + np.pi/4),
        np.sin(time + np.pi/4),
        np.cos(time + np.pi/2),
        np.sin(time + np.pi/2),
        np.cos(time + 3*np.pi/4),
        np.sin(time + 3*np.pi/4),
        np.cos(time + np.pi),
        np.sin(time + np.pi),
        np.cos(time + 5*np.pi/4),
        np.sin(time + 5*np.pi/4),
        np.cos(time + 3*np.pi/2),
        np.sin(time + 3*np.pi/2),
        np.cos(time + 7*np.pi/4),
        np.sin(time + 7*np.pi/4),
    ])

    points.set_data(x, y)
    return points,

# Initial positions of the points
initial_x = np.array([0, 0.3, 0.5, 0.7, 1, 0.7, 0.5, 0.3, 0, -0.3, -0.5, -0.7, -1, -0.7, -0.5])
initial_y = np.array([1, 1, 1, 1, 1, 0.5, 0, -0.5, -1, -1, -1, -1, -1, -0.5, 0])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Create the scatter plot
points = ax.scatter(initial_x, initial_y, c='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, fargs=(points,), interval=50, blit=True)

# Display the animation
plt.show()

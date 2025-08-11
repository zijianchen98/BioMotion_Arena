
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Define the points for the stick figure in the bowing posture
body_points = np.array([
    [0, 1],   # Head
    [0, 0.8], # Neck
    [0, 0.5], # Upper body
    [-0.1, 0.3], [0.1, 0.3],  # Shoulders
    [-0.2, 0.1], [0.2, 0.1],  # Elbows
    [-0.3, 0],  [0.3, 0],    # Hands
    [0, 0],   # Waist
    [-0.1, -0.3], [0.1, -0.3], # Thighs
    [-0.1, -0.6], [0.1, -0.6], # Knees
    [-0.1, -0.8], [0.1, -0.8], # Feet
])

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=10)  # White dots

# Animation function
def update(frame):
    # Simulate the bowing motion
    bend_angle = np.sin(frame * 0.1) * 0.2  # Bending effect
    bow = np.copy(body_points)
    bow[2:, 1] -= bend_angle  # Move the lower body points down
    bow[0:2, 1] += bend_angle  # Move the head and neck up to create a bow effect
    points.set_data(bow[:, 0], bow[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

plt.axis('off')  # Turn off the axis
plt.show()

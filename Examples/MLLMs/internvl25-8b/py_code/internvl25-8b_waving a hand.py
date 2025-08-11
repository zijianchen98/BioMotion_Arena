
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15
# Time step (in seconds)
dt = 0.05

# The initial state of the points
points = np.zeros((num_points, 3))

# Warming up
points[0] = np.array([0.0, 0.0, 0.0])
points[1] = np.array([0.3, -0.3, 0.0])
points[2] = np.array([0.4, -0.2, 0.0])
points[3] = np.array([0.5, -0.2, 0.0])
points[4] = np.array([0.6, -0.1, 0.0])
points[5] = np.array([0.7, -0.1, 0.0])
points[6] = np.array([0.8, -0.1, -0.1])
points[7] = np.array([0.9, -0.2, -0.1])
points[8] = np.array([1.0, -0.2, -0.1])
points[9] = np.array([1.0, -0.2, -0.2])
points[10] = np.array([0.9, -0.3, -0.2])
points[11] = np.array([0.8, -0.3, -0.2])
points[12] = np.array([0.7, -0.3, -0.1])
points[13] = np.array([0.6, -0.3, 0.0])
points[14] = np.array([0.5, -0.3, 0.0])

# Function to update the positions
def update(frame):
    points[:, 0] = 0.5 * np.sin(2 * np.pi * frame * 0.5 + np.random.randn(num_points) * 0.1)
    points[:, 1] = 0.5 * np.sin(2 * np.pi * frame * 0.4 + np.random.randn(num_points) * 0.1)
    return [plt.Line2D([0, p[0]], [0, p[1]]) for p in points]

# Animation setup
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, color='white')
sm = animation.ArtistAnimation(fig, line, frames=range(int(1/(dt*60)*150)), interval=dt*60, blit=True, init_func=lambda: line.set_data([], []))

# Display with animation
plt.axis('off')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the sadman's skeleton parameters (simplified)
num_points = 15
x = np.linspace(-1, 1, num_points)
y = np.linspace(-1, 1, num_points)
X, Y = np.meshgrid(x, y)

# Define motion parameters
duration = 100  # Frames
frame_rate = 30
dt = 1 / frame_rate

# Define motion for sitting down
# This is a simplified representation - real biomechanics are complex
# The animation represents a subtle movement downwards and slightly inwards
for i in range(duration):
    t = i * dt
    for j in range(num_points):
        # Movement downwards (adjust amplitude for realism)
        Y[j, :] = 1 - (0.2 + 0.4 * np.sin(t))
        # Movement inwards (adjust amplitude for realism)
        X[j, :] = 1 - (0.1 + 0.2 * np.cos(t))

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create the point-lights
points = ax.scatter(X, Y, s=50, color='white')

# Animation function
def animate(i):
    points.set_offsets(X[i, :], Y[i, :])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("sadman_sitting_down.gif", writer='pillow', fps=frame_rate)

plt.show()

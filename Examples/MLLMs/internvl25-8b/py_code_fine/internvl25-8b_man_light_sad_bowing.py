
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
diameter = 5
frame_duration = 0.1  # in seconds

# Define the initial positions of the points
positions = np.zeros((num_points, 2))
angles = np.linspace(0, 4 * np.pi, num_points)
positions[:, 0] = diam * np.sin(angles)  # x positions
positions[:, 1] = diam * np.cos(angles)  # y positions

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_facecolor('black')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Update function for the animation
def update(t):
    angles = (t % (2 * np.pi)) + angles  # update angles
    positions[:, 0] = diam * np.sin(angles)  # update x positions
    positions[:, 1] = diam * np.cos(angles)  # update y positions
    for i, pos in enumerate(positions):
        circle = plt.Circle(pos, diameter, color='white', lw=3)
        ax.add_patch(circle)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100, 1/fps), interval=frame_duration * 1000, repeat=False)
plt.show()

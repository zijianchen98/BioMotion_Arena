
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define initial positions of the 15 point-lights
n_points = 15
angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
x = np.cos(angles)
y = np.sin(angles)
positions = np.array([x, y]).T

# Scale positions for visibility
scale = 0.15
positions *= scale

def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')
    
    # Update positions to simulate turning motion
    angle = frame / 50.0 * 2 * np.pi
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    
    rotated_positions = np.dot(positions, rotation_matrix.T)
    ax.scatter(rotated_positions[:, 0], rotated_positions[:, 1], color='white', s=50)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.show()

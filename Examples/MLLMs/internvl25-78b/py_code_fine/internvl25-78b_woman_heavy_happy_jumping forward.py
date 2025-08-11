
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the happy woman jumping forward
def get_points(t):
    return np.array([
        [0, 1.7 * np.sin(t)],  # Head
        [-0.3, 1.5 * np.sin(t)],  # Upper body left
        [0.3, 1.5 * np.sin(t)],  # Upper body right
        [-0.4, 1.3 * np.sin(t)],  # Left arm
        [0.4, 1.3 * np.sin(t)],  # Right arm
        [0, 1.2 * np.sin(t)],  # Waist
        [-0.2, 1.1 * np.sin(t)],  # Left hip
        [0.2, 1.1 * np.sin(t)],  # Right hip
        [-0.35, 0.9 * np.sin(t)],  # Left knee
        [0.35, 0.9 * np.sin(t)],  # Right knee
        [-0.4, 0.6 * np.sin(t)],  # Left foot
        [0.4, 0.6 * np.sin(t)],  # Right foot
        [0.2, 1.6 * np.sin(t)],  # Shoulder
        [-0.2, 1.6 * np.sin(t)],  # Opposite shoulder
        [0, 1.8 * np.sin(t)]  # Top of head
    ]) + [0.2 * t, 0]  # Forward motion

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 2)
points, = ax.plot([], [], 'wo')

# Animation update function
def update(t):
    pts = get_points(t)
    points.set_data(pts[:, 0], pts[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 4 * np.pi, 120), interval=50, blit=True)

plt.axis('off')
plt.show()

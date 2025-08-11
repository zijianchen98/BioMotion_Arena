
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a forward roll
def forward_roll(t):
    # Define the positions of the 15 points at time t
    # These points are simplified and may need to be adjusted for more realism
    points = np.array([
        [0.5 * np.sin(t), 0.5 * np.cos(t)],  # Head
        [0.4 * np.sin(t + 0.1), 0.4 * np.cos(t + 0.1)],  # Neck
        [0.3 * np.sin(t + 0.2), 0.3 * np.cos(t + 0.2)],  # Shoulder left
        [0.3 * np.sin(t + 0.3), 0.3 * np.cos(t + 0.3)],  # Shoulder right
        [0.2 * np.sin(t + 0.4), 0.2 * np.cos(t + 0.4)],  # Elbow left
        [0.2 * np.sin(t + 0.5), 0.2 * np.cos(t + 0.5)],  # Elbow right
        [0.1 * np.sin(t + 0.6), 0.1 * np.cos(t + 0.6)],  # Wrist left
        [0.1 * np.sin(t + 0.7), 0.1 * np.cos(t + 0.7)],  # Wrist right
        [0.4 * np.sin(t + 0.8), 0.4 * np.cos(t + 0.8)],  # Hip left
        [0.4 * np.sin(t + 0.9), 0.4 * np.cos(t + 0.9)],  # Hip right
        [0.3 * np.sin(t + 1.0), 0.3 * np.cos(t + 1.0)],  # Knee left
        [0.3 * np.sin(t + 1.1), 0.3 * np.cos(t + 1.1)],  # Knee right
        [0.2 * np.sin(t + 1.2), 0.2 * np.cos(t + 1.2)],  # Ankle left
        [0.2 * np.sin(t + 1.3), 0.2 * np.cos(t + 1.3)],  # Ankle right
        [0.1 * np.sin(t + 1.4), 0.1 * np.cos(t + 1.4)]   # Foot left
    ])
    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scatter = ax.scatter([], [], c='white', s=50)

# Initialization function
def init():
    scatter.set_offsets([])
    return scatter,

# Animation update function
def update(frame):
    points = forward_roll(frame)
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 200),
                              init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()

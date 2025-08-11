
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Define Constants**
NUM_POINTS = 15
FRAME_COUNT = 60
MOTION_AMPLITUDE = 0.1  # Variation in 'sitting down' movement

# **Initialize Point Light Positions**
# Manually setting points to represent body parts (e.g., head, shoulders, hips)
points_start = np.array([
    (0, 1),  # Head
    (-0.5, 0.8), (0.5, 0.8),  # Shoulders
    (-0.4, 0.5), (0.4, 0.5),  # Elbows
    (-0.2, 0.3), (0.2, 0.3),  # Hands
    (-0.3, 0), (0.3, 0),  # Hips
    (-0.4, -0.5), (0.4, -0.5),  # Knees
    (-0.2, -1), (0.2, -1),  # Feet
    (-0.6, 0.5), (0.6, 0.5),  # Additional points to enhance the silhouette
    (-0.6, 0), (0.6, 0)
])

# **Set Up Figure**
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# **Initialization Function**
def init():
    points.set_data([], [])
    return points,

# **Update Function for Animation**
def update(frame):
    # Simulate the motion of 'sitting down'
    motion = np.sin(frame / 10) * MOTION_AMPLITUDE

    # Calculate new positions based on the 'sitting down' movement
    new_positions = points_start + np.array([[0, motion]] * NUM_POINTS)

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# **Create Animation**
ani = animation.FuncAnimation(fig, update, frames=FRAME_COUNT, init_func=init, blit=True, interval=50)

# **Show Animation**
plt.show()

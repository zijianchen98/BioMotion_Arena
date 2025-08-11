
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Set Up Parameters**
num_points = 15
frames = 60
fps = 30

# **Initialize Point-light Positions**
# Structure: [x, y] for each point-light representing body parts
positions = np.array([
    [0, 2], [0.5, 3], [-0.5, 3],  # Head
    [0, 1.5], [0.5, 2], [-0.5, 2],  # Shoulders
    [0, 1], [0.6, 0.5], [-0.6, 0.5],  # Hips
    [0, 0], [0.5, -1], [-0.5, -1],  # Knees
    [0, -1.5], [0.5, -2], [-0.5, -2]  # Feet
])

# **Running Motion Function**
def running_motion(frame):
    global positions
    # Basic running motion; Adjust y-axis for leg and arm movements
    leg_movement = np.sin(np.linspace(0, 2 * np.pi, num_points) + frame * 0.3) * 0.1
    positions[8:11, 1] = -1 + leg_movement[8:11]  # Knee movement

    positions[4:7, 1] = 1 + leg_movement[4:7] * 0.5  # Shoulder movement
    return positions

# **Create a Figure**
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')

# **Initialize Points**
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

# **Animation Update Function**
def update(frame):
    pos = running_motion(frame)
    point_lights.set_data(pos[:, 0], pos[:, 1])
    return point_lights,

# **Create Animation**
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# **Show Animation**
plt.show()

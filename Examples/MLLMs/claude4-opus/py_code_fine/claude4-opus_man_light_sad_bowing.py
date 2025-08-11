
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Parameters**
num_points = 15  # Number of point-lights
duration = 2000  # Duration of the animation in milliseconds 
fps = 30         # Frames per second
frames = int(duration / 1000 * fps)  # Total number of frames

# **Creating the figure and axes**
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# **Initialize Points for a Sadman Bowing**
# Initial positions of the points (15 points representing key joints)
point_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Elbows
    [-0.5, -0.5], [0.5, -0.5],  # Wrists
    [0, -1], # Torso
    [-0.8, -1.5], [0.8, -1.5],  # Knees
    [-0.5, -2], [0.5, -2],  # Ankles
    [-0.6, -1.5], [0.6, -1.5],  # Feet
    [-0.3, -1], [0.3, -1]   # Feet Extra Points
])

# **Creating a scatter plot for points**
points, = ax.plot([], [], 'wo', markersize=8)

# **Update Function**
def update(frame):
    # Modify point_positions to simulate bowing
    # Bowing action: lowering the upper body and moving the head down
    bow_angle = (frame / frames) * np.pi * 0.5  # Adjust angle of bowing
    point_positions[0][1] -= 0.01  # Head moving down
    point_positions[7][1] -= 0.01 * np.sin(bow_angle) # Torso bends
    for i in range(1, 5):
        point_positions[i][1] -= 0.005  # Shoulders and elbows lower slightly
    points.set_data(point_positions[:, 0], point_positions[:, 1])
    return points,

# **Animation**
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=1000/fps)

plt.title('Point-Light Animation of a Sadman Bowing')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sad woman with heavy weight
# Each row represents a point-light, and each column represents a joint (x, y)
point_lights = np.array([
    [0.5, 0.5],  # Head
    [0.5, 0.6],  # Shoulder R
    [0.5, 0.4],  # Shoulder L
    [0.6, 0.7],  # Elbow R
    [0.4, 0.7],  # Elbow L
    [0.7, 0.8],  # Wrist R
    [0.3, 0.8],  # Wrist L
    [0.5, 0.3],  # Hip R
    [0.5, 0.2],  # Hip L
    [0.6, 0.1],  # Knee R
    [0.4, 0.1],  # Knee L
    [0.7, 0.0],  # Ankle R
    [0.3, 0.0],  # Ankle L
    [0.5, 0.9],  # Heavy weight
    [0.5, 0.1]   # Ground
])

# Define the movement parameters for the bowing action
# Each row represents a frame, and each column represents a point-light (x, y)
movement = np.zeros((100, 15, 2))  # 100 frames, 15 point-lights, 2D movement
for i in range(100):
    # Move the head and shoulders down
    movement[i, 0, 1] = 0.5 - 0.1 * np.sin(i / 10.0)
    movement[i, 1, 1] = 0.6 - 0.1 * np.sin(i / 10.0)
    movement[i, 2, 1] = 0.4 - 0.1 * np.sin(i / 10.0)
    
    # Move the elbows and wrists down
    movement[i, 3, 1] = 0.7 - 0.2 * np.sin(i / 10.0)
    movement[i, 4, 1] = 0.7 - 0.2 * np.sin(i / 10.0)
    movement[i, 5, 1] = 0.8 - 0.3 * np.sin(i / 10.0)
    movement[i, 6, 1] = 0.8 - 0.3 * np.sin(i / 10.0)
    
    # Move the hips and knees down
    movement[i, 7, 1] = 0.3 - 0.1 * np.sin(i / 10.0)
    movement[i, 8, 1] = 0.2 - 0.1 * np.sin(i / 10.0)
    movement[i, 9, 1] = 0.1 - 0.2 * np.sin(i / 10.0)
    movement[i, 10, 1] = 0.1 - 0.2 * np.sin(i / 10.0)
    
    # Move the ankles down
    movement[i, 11, 1] = 0.0 - 0.1 * np.sin(i / 10.0)
    movement[i, 12, 1] = 0.0 - 0.1 * np.sin(i / 10.0)
    
    # Move the heavy weight down
    movement[i, 13, 1] = 0.9 - 0.5 * np.sin(i / 10.0)

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the first frame
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_axis_off()
points = ax.scatter(point_lights[:, 0], point_lights[:, 1], s=50, c='w')

# Define the update function for the animation
def update(frame):
    points.set_offsets(point_lights + movement[frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(movement), interval=50)

# Show the animation
plt.show()

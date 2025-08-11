
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the points for the sadman's body
body_points = np.array([
    [0, 0],  # head
    [0, 1],  # left ear
    [0, -1],  # right ear
    [1, 2],  # left shoulder
    [-1, 2],  # right shoulder
    [2, 3],  # left hip
    [-2, 3],  # right hip
    [0, 4],  # left knee
    [0, -4],  # right knee
    [0, 5],  # left ankle
    [0, -5],  # right ankle
    [1, 6],  # left elbow
    [-1, 6],  # right elbow
    [1, 7],  # left wrist
    [-1, 7]   # right wrist
])

# Define the points for the sadman's light sources
light_points = np.array([
    [0, 0],  # head
    [0.2, 1],  # left ear
    [0.2, -1],  # right ear
    [1.2, 2],  # left shoulder
    [-1.2, 2],  # right shoulder
    [2.2, 3],  # left hip
    [-2.2, 3],  # right hip
    [0.5, 4],  # left knee
    [0.5, -4],  # right knee
    [0.5, 5],  # left ankle
    [0.5, -5],  # right ankle
    [1.5, 6],  # left elbow
    [-1.5, 6],  # right elbow
    [1.5, 7],  # left wrist
    [-1.5, 7]   # right wrist
])

# Create a new figure
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Create a black background
ax.set_facecolor('black')

# Initialize the body points
body_lines = []
for i in range(len(body_points) - 1):
    body_lines.append(ax.plot(body_points[i, 0], body_points[i, 1], body_points[i+1, 0], body_points[i+1, 1], 'b-')[0])

# Initialize the light sources
light_patches = []
for point in light_points:
    light_patches.append(ax.scatter(point[0], point[1], s=200, c='white', marker='o'))

# Function to update the animation
def update(frame):
    # Update the body points
    for i, line in enumerate(body_lines):
        if i == 0:
            line.set_xdata([body_points[i, 0] + np.sin(frame * 0.1) * 0.5, body_points[i+1, 0] + np.sin(frame * 0.1)])
            line.set_ydata([body_points[i, 1], body_points[i+1, 1]])
        elif i == len(body_points) - 2:
            line.set_xdata([body_points[i, 0], body_points[i-1, 0] + np.sin(frame * 0.1) * 0.5])
            line.set_ydata([body_points[i, 1], body_points[i-1, 1]])
        else:
            line.set_xdata([body_points[i, 0], body_points[i+1, 0]])
            line.set_ydata([body_points[i, 1], body_points[i+1, 1]])

    # Update the light sources
    for i, patch in enumerate(light_patches):
        patch.set_offsets([light_points[i, 0] + np.sin(frame * 0.1) * 0.2, light_points[i, 1]])

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20, blit=False)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = np.array([
    [0, 0],  # head
    [-0.5, 0.5],  # left shoulder
    [0.5, 0.5],  # right shoulder
    [-0.5, 0],  # left elbow
    [0.5, 0],  # right elbow
    [-0.5, -0.5],  # left wrist
    [0.5, -0.5],  # right wrist
    [0, 0.5],  # torso
    [0, -0.5],  # hip
    [-0.5, -1],  # left knee
    [0.5, -1],  # right knee
    [-0.5, -1.5],  # left ankle
    [0.5, -1.5],  # right ankle
    [-0.25, 0.25],  # left hand
    [0.25, 0.25]  # right hand
])

# Define the waving hand motion
def waving_hand(t):
    angle = np.pi / 2 * np.sin(t)
    point_lights[13, 0] = -0.25 + 0.1 * np.cos(angle)  # left hand x
    point_lights[13, 1] = 0.25 + 0.1 * np.sin(angle)  # left hand y
    return point_lights

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize the point-lights
scatter = ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)

# Animation function
def animate(t):
    global point_lights
    point_lights = waving_hand(t)
    scatter.set_offsets(point_lights)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 128),
                              interval=50, blit=True)

plt.show()

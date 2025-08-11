
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 0.5)
ax.set_facecolor('black')

# Define the initial positions of the point lights
num_lights = 15
light_positions = np.array([
    [0, 0.4],   # head
    [-0.2, 0.2], [0.2, 0.2],   # shoulders
    [-0.3, 0.1], [0.3, 0.1],   # elbows
    [-0.4, 0], [0.4, 0],       # wrists
    [-0.4, -0.2], [0.4, -0.2], # hips
    [-0.3, -0.4], [0.3, -0.4], # knees
    [-0.2, -0.6], [0.2, -0.6], # ankles
    [-0.1, -0.8], [0.1, -0.8], # feet
    [0, -0.9]   # lower body
])

# Create point light objects
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(num_lights)]

# Update function for animation
def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    # Update positions slightly to simulate a 'breathing' effect while lying down
    motion = 0.02 * np.sin(2 * np.pi * frame / 40)
    light_positions[:, 1] += motion  # Slightly alter y positions
    for point, pos in zip(points, light_positions):
        point.set_data(pos[0], pos[1])
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()

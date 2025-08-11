
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point light source
def point_light(x, y, z, intensity):
    """Create a point light source at the given position with the specified intensity."""
    return np.array([x, y, z, intensity])

# Define the sadman's movement
def sadman_movement(t):
    """Calculate the movement of the sadman at time t."""
    # Movement parameters
    v = np.array([1, 0, 0])  # velocity
    a = np.array([0, 0, -0.1])  # acceleration

    # Calculate the movement at each time step
    t_steps = int(t / 0.1)
    movement = np.zeros((t_steps, 3))
    for i in range(t_steps):
        movement[i] = v * i
        v += a * i

    return movement

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the point lights
lights = []
for i in range(15):
    light = point_light(0, 0, 0, 1)  # intensity 1
    ax.add_patch(plt.Rectangle((i, 0), 1, 1, edgecolor='black', facecolor='white', alpha=0.5))
    lights.append(light)

# Initialize the sadman's position
sadman_pos = np.array([0, 0, 0])

# Function to update the plot
def update(frame):
    global sadman_pos
    # Update the sadman's position
    sadman_pos += sadman_movement(frame)

    # Update the point lights
    for light in lights:
        light.set_data([light.x + sadman_pos[0], light.y + sadman_pos[1], light.z + sadman_pos[2]])
        light.set_alpha(frame / 10)

    # Clear the axis
    ax.clear()

    # Set the axis limits
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)

    # Draw the axis
    ax.set_aspect('equal')
    ax.set_xticks([-2, 0, 2])
    ax.set_yticks([-2, 0, 2])
    ax.set_zticks([-2, 0, 2])

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()

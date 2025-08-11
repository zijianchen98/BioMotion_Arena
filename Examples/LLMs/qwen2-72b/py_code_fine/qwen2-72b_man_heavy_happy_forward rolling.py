
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the positions of the 15 joints of the 'happyman'
joint_positions = np.zeros((num_frames, 15, 2))

# Animation parameters
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_facecolor('black')

# Create empty lists to hold the point lights
point_lights = []

def init():
    # Initialize the animation by clearing the axis
    ax.clear()
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.set_facecolor('black')
    return point_lights

def animate(i):
    # Clear the previous frame's point lights
    for light in point_lights:
        light.remove()
    point_lights.clear()

    # Update joint positions for forward rolling action
    # This is a simplified version; real motion capture data would provide better accuracy
    angle = i * 2 * np.pi / num_frames
    x_offset = np.sin(angle)
    y_offset = np.cos(angle)

    joint_positions[i, :, 0] = np.linspace(0 + x_offset, 10 + x_offset, 15)
    joint_positions[i, :, 1] = np.linspace(0 + y_offset, 10 + y_offset, 15)

    # Plot the point lights at the updated joint positions
    for pos in joint_positions[i]:
        light, = ax.plot(pos[0], pos[1], 'o', color='white')
        point_lights.append(light)

    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames,
                              init_func=init, blit=True, interval=50)

plt.show()

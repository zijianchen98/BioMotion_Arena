
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters for the animation
num_lights = 15
duration = 200  # Frames
fps = 30
dt = 1 / fps

# Define the rolling motion parameters
roll_angle = np.linspace(0, 2 * np.pi, num_lights)
roll_speed = 0.1
roll_phase = np.arange(0, duration, dt)

# Define the x and y positions of the lights
x = np.cos(roll_angle)
y = np.sin(roll_angle)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Create the point lights
lights = ax.scatter(x, y, s=50, color='white')

# Animation function
def animate(frame):
    for i in range(num_lights):
        x[i] = np.cos(roll_angle[i] + roll_phase[frame])
        y[i] = np.sin(roll_angle[i] + roll_phase[frame])
    lights.set_offsets(np.c_[x, y])
    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=False)

# Save the animation
ani.save('forward_roll_motion.gif', writer='pillow', fps=fps)

plt.show()

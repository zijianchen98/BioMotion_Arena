
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100  # Frames
frame_rate = 30
radius = 0.05
center_x = 0.5
center_y = 0.5
radius_range = 0.1
angle_speed = 0.05
z_range = 0.1

# Initialize figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.axis('off')

lights = []
for i in range(num_lights):
    light = ax.scatter(center_x, center_y, s=50, color='white', zorder=1)
    lights.append(light)

def update(frame):
    for light in lights:
        # Calculate position based on time and angle
        angle = np.linspace(0, 2 * np.pi, num_lights)[frame % num_lights]
        x = center_x + radius + radius_range * np.cos(angle)
        y = center_y + radius_range * np.sin(angle)
        z = frame / duration * z_range  # Movement along z-axis

        light.set_offsets([x, y, z])

    return lights

# Create animation
ani = animation.FuncAnimation(fig, update, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("happy_woman_turning_around.gif", writer='pillow', fps=frame_rate)

plt.show()

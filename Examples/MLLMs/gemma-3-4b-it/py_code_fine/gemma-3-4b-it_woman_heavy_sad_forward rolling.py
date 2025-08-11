
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100  # Frames
frame_rate = 30
dt = 1 / frame_rate

# Define the action parameters (forward rolling)
roll_angle_start = 0
roll_speed = 0.1
roll_amplitude = 0.3

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Initialize the lights
lights = []
for _ in range(num_lights):
    light = plt.Point2D(np.random.uniform(-0.8, 0.8), np.random.uniform(-0.8, 0.8))
    lights.append(light)

# Create the animation function
def animate(frame):
    for i in range(num_lights):
        # Update the position of each light based on the rolling motion
        light = lights[i]
        light.x = 0.5 * np.sin(frame * roll_speed + roll_angle_start)
        light.y = -0.5 * np.cos(frame * roll_speed + roll_angle_start)
        
    ax.clear()  # Clear the previous frame
    ax.set_facecolor('black')
    ax.scatter([light.x for light in lights], [light.y for light in lights], s=20, c='white')
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("forward_rolling_sadwoman.gif", writer='pillow', fps=frame_rate)

plt.show()

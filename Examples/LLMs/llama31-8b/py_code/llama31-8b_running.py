
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Define the background color
ax.set_facecolor('black')

# Define the point-lights
lights = []
for i in range(15):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    lights.append(ax.scatter(x, y, s=20, c='white'))

# Define the movement parameters
num_frames = 100
frame_duration = 100  # milliseconds
total_time = num_frames * frame_duration
dt = 16  # milliseconds (approximate frame rate: 60 FPS)
t = np.arange(0, total_time, dt)

# Define the movement equations
# These equations are based on a simplified model of human running motion
# The x and y coordinates of each light are a function of time, with the lights moving in a circular motion
theta = np.linspace(0, 2*np.pi, num_frames)
x_coords = np.cos(theta) * 0.5 + 0.5
y_coords = np.sin(theta) * 0.5 + 0.5

# Animate the lights
def animate(i):
    for j, light in enumerate(lights):
        light.set_offsets([x_coords[i % num_frames], y_coords[i % num_frames]])
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=dt, blit=True)

# Display the animation
plt.show()

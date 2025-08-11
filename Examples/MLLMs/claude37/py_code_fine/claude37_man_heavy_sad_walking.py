
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
frames = 100
height = 10

# Initialize point lights positions
# y-positions for the 'sad man'
y_pos = np.linspace(-height/2, height/2, num_lights)

# Initial x positions simulating a side-to-side motion
x_pos = np.zeros(num_lights)

# Create the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-height/2 - 1, height/2 + 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Animation function
def update(frame):
    # Simulating walking by altering x positions
    if frame < frames / 2:
        step = frame / (frames / 2)  # First half: move right
        x_pos[:] = step * 3  # Move up to 3 units to the right
    else:
        step = (frame - frames / 2) / (frames / 2)  # Second half: move left
        x_pos[:] = 3 - step * 3  # Move back to the left

    # Generate new data points for the animation
    points.set_data(x_pos, y_pos)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

# Show the animation
plt.show()

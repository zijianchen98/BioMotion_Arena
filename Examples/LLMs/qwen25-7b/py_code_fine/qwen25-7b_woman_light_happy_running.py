
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (0, 15 - t ) for t in range(15)
]

# Define the movement function for each point-light
def move_light(light_position):
    # Simple harmonic motion for a more natural look
    amplitude = 4
    frequency = 0 / 10
    phase = 0 * np.pi / 180
    new_x = light_position[0] + amplitude * np.sin(frequency * t + phase)
    new_y = 15 - t
    return (new, new_y)

# Create the figure and axis
fig, ax = plt.subplots()
axg = ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 15)
t.set_ylim(0, 15)
ax.set_facecolor('black')

# Initialize the points
points = [plt.plot(x, y, 'w.', ms=10)[0] for x, y in initial_positions]

# Animation function
def animate(t):
    for i, p in enumerate(points):
        x[i].set_data(move_light(initial_positions[i]))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 210), interval=20)

# Show the animation
plt.show()

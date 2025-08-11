
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_lights = 15

# Initial positions of point lights (you can adjust these for more realistic positions)
x_positions = np.array([0, -0.5, 0.5, -0.3, 0.3, 0, 0, -0.2, 0.2, -0.1, 0.1, -0.1, 0.1, -0.3, 0.3])
y_positions = np.array([1, 0.75, 0.75, 0.5, 0.5, 0.25, 0, -0.25, -0.25, -0.5, -0.5, -0.75, -0.75, -1, -1])

# Wave motion parameters
time = np.linspace(0, 2 * np.pi, 100)
wave_amplitude = 0.1
wave_frequency = 2

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def animate(i):
    # Calculate new positions for each frame
    new_y_positions = y_positions + wave_amplitude * np.sin(wave_frequency * time[i])
    points.set_data(x_positions, new_y_positions)
    
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(time), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()

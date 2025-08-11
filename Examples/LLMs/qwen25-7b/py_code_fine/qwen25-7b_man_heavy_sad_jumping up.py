
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the time step
num_points = 15
dt = 0 / 60  # Assuming total time 't' is 6 seconds for a smooth animation

# Define the initial positions of the points
x = np.linspace(-1, 1, num_points)
y = np.zeros(num_points)

# Define the jumping motion parameters
amplitude = 0 / 4  # Amplitude of the jump
frequency =  1 / 2  # Frequency of the jump

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-0 / 4 - 0 / 8, 0 / 4 +  3 *  1 / 8])

# Create the scatter plot for the points
scat = ax.scatter(x, y)

def update(frame):
    global x, y
    t = frame * dt
    y = amplitude * np.sin(2 * np.pi * frequency * t) - amplitude / 2
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0 / 6), interval=20, blit=True)
plt.show()

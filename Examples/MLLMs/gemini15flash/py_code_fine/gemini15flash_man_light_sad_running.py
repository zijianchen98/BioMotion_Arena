
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_facecolor('black')

# Initialize the points
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)
points, = ax.plot(x, y, 'wo', markersize=10)

# Define the animation function
def animate(i):
    # Define the motion pattern (example: running motion)
    # Adjust these parameters to fine-tune the animation
    amplitude = 2
    frequency = 0.1
    phase_shift = np.linspace(0, 2 * np.pi, num_points)
    
    x = amplitude * np.sin(2 * np.pi * frequency * i + phase_shift)
    y = -5 + amplitude * np.cos(2 * np.pi * frequency * i + phase_shift) + np.linspace(-2,2,num_points)
    points.set_data(x,y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Save the animation as a GIF (optional)
ani.save('running_sadman.gif', writer='imagemagick')

# Show the animation
plt.show()


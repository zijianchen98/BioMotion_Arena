
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-10, 10])
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point-light coordinates
num_points = 15
x = np.zeros(num_points)
y = np.zeros(num_points)

# Define the initial positions of the points (adjust as needed to match the image)

x = np.array([-1, -1, 0, 1, 1, -2, -1.5, -0.5, 0.5, 1.5, 2, -1, 1, 0, 0 ])
y = np.array([6, 4, 5, 4, 6, 2, 3, 3, 3, 3, 2, 0, 0, -2,-4])


points, = ax.plot(x, y, 'wo', markersize=10)

# Animation function
def animate(i):
    global x, y

    # Define the bowing motion (adjust parameters for realism and smoothness)
    #This part is crucial and needs to be adjusted for a realistic effect
    #Consider sinusoidal curves for smooth motion, with different frequencies and amplitudes for different points

    #Example (replace with better biomechanically plausible motion):
    #  x += 0.05 * np.sin(i * 0.1 + np.arange(num_points) * 0.2 )
    #  y += 0.1 * np.cos(i * 0.1 + np.arange(num_points) * 0.2 )
    
    # Example of more realistic bowing motion:
    amplitude = 0.5  # Adjust for bowing intensity
    frequency = 0.08  # Adjust for bowing speed
    phase_shifts = np.linspace(0, 2 * np.pi, num_points)

    x_offsets = amplitude * np.sin(frequency * i + phase_shifts)
    y_offsets = -amplitude * np.cos(frequency*i +phase_shifts)

    x += x_offsets
    y += y_offsets

    #Keep points within bounds
    x = np.clip(x, -5, 5)
    y = np.clip(y, -10, 10)


    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Save the animation (optional)
ani.save('biological_motion.gif', writer='pillow', fps=20)

# Show the animation
plt.show()

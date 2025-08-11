
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the duration of the animation
num_points = 15
duration = 10  # in seconds

# Create the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim((-1, 1)
ax.set_ylim((-1, 1))
ax.set_aspect('equal')
ax.axis('off')

# Initialize the positions of the points
points = np.random.uniform(-0.5, 0.8, size=(num_points, 2))

def update(frame):
    global points
    
    # Calculate the new positions based on the wave motion
    wave_amplitude = 0.1 * np.sin(frame / duration * 2 * np.pi)
    wave_frequency = 0.1 * np.cos(frame / duration * 2 * np.pi)
    
    for i, (point in enumerate(points):
        x, y = point
        dx = wave_amplitude * np.sin(wave_frequency + frame / duration * 2 * np.pi)
        dy = -wave_amplitude * np.cos(wave_frequency + frame / duration * 2 * np.pi)
        
        points[i] = (x + dx, y + dy
        
    # Update the scatter plot with the new positions
    scatter.set_offsets(points)
    
    return scatter,

# Create the scatter plot for the points
scatter = ax.scatter(points[:,0], points[:,1], c='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, duration * 60), blit=True, interval=30)

plt.show()


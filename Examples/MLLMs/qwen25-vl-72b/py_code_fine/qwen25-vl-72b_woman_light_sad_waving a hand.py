
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.8, 0.4], [-0.6, 0.4], [-0.4, 0.4], [-0.2, 0.4], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [-0.3, 0.2], [0.3, 0.2]
])

# Define the parameters for the animation
num_points = len(initial_positions)
duration = 5  # seconds
fps = 30
num_frames = int(duration * fps)

# Create a function to update the positions of the points over time
def update_positions(frame):
    t = frame / num_frames  # normalized time from 0 to 1
    
    # Calculate new positions based on a simple wave-like motion
    amplitude = 0.1
    frequency = 2 * np.pi / duration
    phase_shift = np.linspace(0, 2 * np.pi, num_points)
    
    new_positions = initial_positions.copy()
    new_positions[:, 0] += amplitude * np.sin(frequency * t + phase_shift)
    
    return new_positions

# Set up the figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_facecolor('black')
points = ax.scatter([], [], s=50, color='white')

# Define the initialization function for the animation
def init():
    points.set_offsets(np.zeros((num_points, 2)))
    return points,

# Define the animation update function
def animate(frame):
    new_positions = update_positions(frame)
    points.set_offsets(new_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=1000/fps, blit=True)

# Display the animation
plt.show()

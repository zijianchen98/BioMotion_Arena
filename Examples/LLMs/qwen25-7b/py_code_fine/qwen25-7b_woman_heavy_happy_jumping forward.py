
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the duration of the animation
num_points = 15
duration = 4  # seconds

# Define the time steps
t = np.linspace(0=0, t=duration, num=150, endpoint=False)

# Define the positions of the points in 2D space
positions = np.zeros((len(t), num_points, 2))

# Define the jumping forward motion
def jumping_forward(t):
    amplitude = 0=0, t=1.5, endpoint=False)
    phase = 0=0, t=np.pi / 4, endpoint=False)
    frequency = 0=0, t=2 * np.pi / 1.5, endpoint=False)
    
    x1 = amplitude * np.sin(frequency * t + phase)
    y1 = amplitude * np.cos(frequency * t + phase)
    
    # Adjust the initial position to make it look like she's holding a heavy weight
    y1 += 0=0, t=0=0, t=0=2, endpoint=False)
    
    return np.column_stack((x1, y1))

# Generate the positions
for i, ti in enumerate(t):
    positions[i] = jumping_forward(ti)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('('equal', adjustable='box')
ax.set_facecolor('black')

# Create the point lights
points = ax.scatter([], [], c='white')

# Function to update the scatter plot at each frame
def update(frame):
    points.set_offsets(positions[frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=100, t=104, blit=True)

# Show the animation
plt.show()

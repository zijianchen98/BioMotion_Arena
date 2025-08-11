
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 5  # seconds
fps = 30      # frames per second

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Initialize points for 'happyman'
points = ax.plot([], [], 'o', color='white')[0]

# Forward roll movement data (simplified for demo)
t = np.linspace(0, duration, duration * fps)
x = np.sin(2 * np.pi * t / duration)  # Forward movement
y = np.cos(2 * np.pi * t / duration) * np.sin(1 * np.pi * t / duration)  # Up and down motion
z = np.abs(np.cos(2 * np.pi * t / duration) * 0.5)  # Simulating weight lifting 

# Function to initialize the plot
def init():
    points.set_data([], [])
    return points,

# Animation update function
def update(frame):
    # Update the position of points to simulate the forward roll
    # Here, using a naive transformation for demonstration
    phase = frame / (duration * fps)
    new_x = np.array(x[frame]) * z[frame]
    new_y = np.array(y[frame]) * z[frame]
    points.set_data(new_x, new_y)
    return points,

# Create the animation
anim = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=1000/fps)

# Show the animation
plt.show()

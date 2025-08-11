
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 8)
ax.set_facecolor('black')

# Number of point-lights
num_points = 15

# Initial positions of the point-lights (Y-axis only)
y_positions = np.linspace(0, 7, num_points)

# Create scatter plot for point-lights (initially all at ground level)
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update each frame of the animation
def update(frame):
    # Calculate the jumping motion
    y_jump = np.sin(frame / 10) * 2 + 4  # Simple sine function for jumping effect
    
    # Update point-light positions
    x_positions = np.zeros(num_points)  # All point-lights at x=0
    new_y_positions = y_positions + y_jump  # Adjust y positions with jump
    
    points.set_data(x_positions, new_y_positions)
    return points,

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()

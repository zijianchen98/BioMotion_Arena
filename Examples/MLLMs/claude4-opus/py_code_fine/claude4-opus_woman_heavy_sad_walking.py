
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the animation
num_points = 15
frames = 100
fps = 30

# Function to generate walking motion for the points
def generate_walking_motion(num_points, frames):
    # Generate a basic walking path based on sine and cosine for smooth motion
    x_positions = np.linspace(-5, 5, frames)
    y_positions = np.sin(x_positions) - 1  # Adjusted to create a downwards motion
    
    points = []
    for i in range(num_points):
        # Simple distribution across the body's position
        points.append((x_positions + (i % 3) * 0.5, y_positions + (i // 3) * 0.4))
    
    return points

# Generate coordinates for the points
point_coordinates = generate_walking_motion(num_points, frames)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 1)
ax.set_facecolor('black')
ax.axis('off')  # Hide axes

# Create scatter plot for the points
scatters = [ax.scatter([], [], s=100, color='white') for _ in range(num_points)]

# Initialize the animation
def init():
    for scat in scatters:
        scat.set_offsets([])
    return scatters

# Update function for the animation
def update(frame):
    for i, scat in enumerate(scatters):
        scat.set_offsets([point_coordinates[i][0][frame], point_coordinates[i][1][frame]])
    return scatters

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

# Show the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points
num_points = 15

# Initial positions of the point-lights (Y-axis varies for lying down)
def initialize_positions():
    y_positions = np.linspace(0.8, -0.8, num_points)
    x_positions = np.zeros(num_points)  # Keeping x constant for lying down
    return x_positions, y_positions

# Update function for the animation
def update(frame):
    # Clear previous points
    ax.clear()
    
    # Move y positions to simulate a gentle, sad motion
    y_positions = np.linspace(0.8, -0.8, num_points) * (1 + 0.05 * np.sin(frame / 5.0))
    x_positions = np.zeros(num_points)
    
    # Plot the moving points
    ax.scatter(x_positions, y_positions, color='white', s=100)  # Use larger points for visibility
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_facecolor('black')  # Black background
    ax.axis('off')  # Turn off the axis

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create and run the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50)

# Display the animation
plt.show()

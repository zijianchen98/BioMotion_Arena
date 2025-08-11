
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the animation
num_lights = 15
total_frames = 200
turning_radius = 4
turning_speed = 0.05  # radians per frame

# Initialize the positions of the point-lights
def initialize_positions(num_lights):
    # Randomly distribute lights on the upper body
    angles = np.linspace(0, 2*np.pi, num_lights, endpoint=False)
    radial_distances = np.random.uniform(1, 3, num_lights)  # Distance from center
    x_positions = radial_distances * np.cos(angles)
    y_positions = radial_distances * np.sin(angles)
    return np.column_stack((x_positions, y_positions))

positions = initialize_positions(num_lights)

# Define the animation updates
def animate(i):
    global positions
    angle = i * turning_speed
    
    # Rotate the positions around the origin
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    positions = np.dot(positions, rotation_matrix.T)
    
    # Update the scatter plot
    scatter.set_offsets(positions)
    return scatter,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')  # Hide axes

# Create the scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=50, color='white', zorder=2)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=total_frames, interval=50, blit=True)

# Adjust the plot to be centered
plt.tight_layout()

# Save the animation
ani.save('biological_motion_animation.gif', writer='imagemagick', fps=20)

# Display the animation
plt.show()

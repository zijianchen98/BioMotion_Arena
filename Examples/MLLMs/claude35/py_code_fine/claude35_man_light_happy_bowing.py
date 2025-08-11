
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Initialize positions for the point lights
# These are arbitrary coordinates mimicking a simple humanoid shape
positions = np.array([[0, 1],   # Head
                      [-0.5, 0.5], [0.5, 0.5],  # Shoulders
                      [-0.5, 0], [0.5, 0],  # Elbows
                      [-0.3, -0.5], [0.3, -0.5],  # Hands
                      [-0.3, -1], [0.3, -1],  # Hips
                      [-0.5, -1.5], [0.5, -1.5],  # Knees
                      [-0.1, -2], [0.1, -2],  # Feet
                      [-1, 0.5], [1, 0.5],  # Extra points for realism
                      [0, 0]])

# Function to update the positions of point lights to simulate the bowing action
def update(frame):
    # Clear the current axes
    ax.clear()
    
    # Set the background color
    ax.set_facecolor('black')

    # Static background to keep the points constant
    ax.set_xlim(-2, 2)
    ax.set_ylim(-3, 1)

    # Apply bowing motion
    bow_angle = np.pi / 20 * frame
    new_positions = np.copy(positions)
    
    # Update y-position for bowing
    new_positions[:, 1] -= 0.1 * np.sin(bow_angle)  # Bowing effect

    # Draw the point-lights
    ax.plot(new_positions[:, 0], new_positions[:, 1], 'o', color='white', markersize=12)

# Set up the plot for animation
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axes

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

# Display the animation
plt.show()

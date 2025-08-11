
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights (joints)
num_points = 15

# Initial configuration of the points (y values)
# Positions are set to represent the bowing posture
positions = np.array([
    [0, 5],   # Head
    [-1, 4], [1, 4],  # Shoulders
    [-2, 3], [0, 3], [2, 3],  # Elbows
    [-1, 2], [1, 2],  # Wrists
    [0, 1],   # Torso
    [-1, 0], [0, 0], [1, 0],  # Hips
    [-1, -1], [1, -1],  # Knees
    [0, -2]   # Feet
])

# Animation function
def update(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-3, 3)
    plt.ylim(-3, 6)
    plt.gca().set_facecolor('black')  # Set background color to black
    
    # Update the vertical positions to simulate bowing
    # Adjust y-coordinates to create bowing effect
    bow_angle = np.sin(frame / 10)  # Make the "bowing" motion
    updated_positions = positions.copy()
    updated_positions[:, 1] += bow_angle  # Simulate lower movement for the bow
    
    # Plot the points
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white')
    
    plt.axis('off')  # Turn off the axes

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

# Show the animation
plt.show()

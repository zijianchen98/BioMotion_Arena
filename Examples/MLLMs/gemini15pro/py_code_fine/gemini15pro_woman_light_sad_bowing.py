
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
# These are approximate coordinates based on the provided image, adjust as needed
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-2, 2], [0, 2], [2, 2],  # Elbows
    [-2, 1], [0, 1], [2, 1],  # Hands/Wrists
    [-0.5, 0], [0.5, 0],  # Hips
    [-1, -1], [1, -1],  # Knees
])

# Number of frames in the animation
n_frames = 60

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Adjust limits as per your needs
ax.set_ylim(-2, 6)
ax.set_aspect('equal')  # Important for proper display of motion
ax.set_facecolor('black')
scatter = ax.scatter([], [], s=20, c='white') # Smaller point size


# Function to update the positions of the dots for each frame
def update(frame):
    # Example motion: simple bowing movement
    # You'll need to define more complex motion based on biomechanical principles
    y_offset = np.sin(frame * np.pi / n_frames)  # Simulate bowing
    new_positions = initial_positions.copy()
    
    # Apply head and upper body movement
    new_positions[:6, 1] -= y_offset * 0.5
    
    # Apply slight hand movement (e.g. towards the front during bow)
    new_positions[6:8, 0] -= y_offset * 0.2 # Left elbow goes left 
    new_positions[8, 0] += y_offset * 0.2 # Right elbow goes right

    new_positions[9:11, 0] -= y_offset * 0.4 # Left hand goes left

    new_positions[11, 0] += y_offset * 0.4 # Right hand goes right
    
    
    scatter.set_offsets(new_positions)
    return scatter,



# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=30, blit=True)


# To save the animation as a gif (requires imagemagick)
# ani.save('bowing_animation.gif', writer='imagemagick', fps=30)

# Display the animation
plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point lights
# Adjust these values to change the posture 
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4], # Head
    [-2, 3], [2, 3], # Shoulders
    [-1.5, 2], [1.5, 2], # Elbows
    [-2, 1], [2, 1], # Hands
    [-0.5, 1], [0.5, 1], # Hips
    [-1, 0], [1, 0], # Knees
    [-1.5, -1], [1.5, -1] # Feet
])

# Number of frames in the animation
n_frames = 50

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)  # Adjust limits as needed
ax.set_ylim(-2, 6)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, c='white')

# Function to initialize the animation
def init():
    scat.set_offsets(initial_positions)
    return scat,


# Function to update the animation for each frame
def animate(i):
    # Example motion: Sitting down
    # You can adjust the formulas to create different actions.

    y_offset = -i * 0.04 *  (1 - np.cos(i * np.pi / n_frames * 2))
    x_offset_knees = 0.2 *  (1 - np.cos(i * np.pi / n_frames * 2)) 
    x_offset_feet = 0.4 *  (1 - np.cos(i * np.pi / n_frames * 2)) 


    new_positions = initial_positions.copy()
    new_positions[9:, 1] += y_offset
    new_positions[10:, 0] += x_offset_knees
    new_positions[12:, 0] += x_offset_feet


    scat.set_offsets(new_positions)
    return scat,



# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, init_func=init, blit=True, interval=20, repeat=True )


# Save the animation (optional)
# writergif = animation.PillowWriter(fps=30)
# ani.save('sitting_down.gif', writer=writergif)


# Display the animation
plt.show()

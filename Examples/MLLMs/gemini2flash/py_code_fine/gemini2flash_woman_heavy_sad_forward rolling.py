
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the duration of the animation in frames
num_frames = 200

# Define the initial positions of the point-lights (example positions)
initial_positions = np.array([
    [0, 10],  # Head
    [-2, 8],  # Left Shoulder
    [2, 8],   # Right Shoulder
    [-4, 5],  # Left Elbow
    [4, 5],   # Right Elbow
    [-5, 2],  # Left Wrist
    [5, 2],   # Right Wrist
    [-1, 5],  # Torso Top Left
    [1, 5],   # Torso Top Right
    [-1, 2],  # Torso Bottom Left
    [1, 2],   # Torso Bottom Right
    [-1.5, -1], # Left Hip
    [1.5, -1],  # Right Hip
    [-1, -4], # Left Knee
    [1, -4]   # Right Knee
])

# Define the animation function that updates the positions of the point-lights
def update_points(frame_num, points):
    # Simulate forward rolling motion
    angle = (frame_num / num_frames) * 2 * np.pi
    
    # Adjust positions based on sine and cosine waves for rolling
    for i in range(num_points):
        
        # Core body rotation
        points.set_offsets(initial_positions + np.array([0, np.sin(angle)])*2)

        # Add slight horizontal sway
        points.set_offsets(points.get_offsets() + np.array([np.cos(angle)*0.5, 0]))
       
        # Make the head nod slightly with rotation
        initial_positions[0][1] += np.sin(angle)/5
        initial_positions[0][0] += np.cos(angle)/5

        # Widen arms a bit
        initial_positions[1][0] -= np.sin(angle/2)/10 #left shoudler
        initial_positions[2][0] += np.sin(angle/2)/10 #right shoulder

        # Move whole body foward as it rolls
        initial_positions += [0, np.sin(angle)]/5


    return points,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black') # Set background color to black
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes

# Create the scatter plot for the point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=20)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points,), blit=True, frames=num_frames, repeat=True)

plt.show()

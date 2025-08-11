
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Define the initial positions of point-lights (as a simple representation)
# Using 15 points for the joints and ends of limbs aligned for bowing motion
points = np.array([
    [0, 4],  # Head
    [-1, 3], [1, 3],  # Shoulders
    [-1, 2], [1, 2],  # Elbows
    [-1, 1], [1, 1],  # Hands
    [0, 0],  # Center (Waist)
    [-0.5, -1], [0.5, -1],  # Hips
    [-0.5, -2], [0.5, -2],  # Knees
    [-0.25, -3], [0.25, -3],  # Feet
    [0, -4],  # Feet or lower body
]).T  # Transpose to have points as columns

# Set number of frames for the animation
n_frames = 60

# Define the update function for the animation
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.axis('off')

    # Calculate movement for bowing
    bow_angle = np.pi / 10  # Amount of bowing (15 degrees)
    base_y = -frame / n_frames * 2  # Move down gradually
    for i in range(points.shape[1]):
        # For the head, shoulders, and torso, apply a downward bow motion
        if i == 0:  # Head
            y_offset = base_y + 4
        elif i in [1, 2]:  # Shoulders
            y_offset = base_y + 3
        elif i in [3, 4]:  # Elbows
            y_offset = base_y + 2
        elif i in [5, 6]:  # Hands
            y_offset = base_y + 1
        elif i == 7:  # Waist
            y_offset = base_y
        elif i in [8, 9]:  # Hips
            y_offset = base_y - 1
        elif i in [10, 11]:  # Knees
            y_offset = base_y - 2
        elif i in [12, 13]:  # Feet
            y_offset = base_y - 3
        else:  # Lower body
            y_offset = base_y - 4
            
        # Apply downward bowing adjustment
        y_offset -= np.sin(bow_angle * frame / n_frames) * 0.5 if (0 < frame < n_frames) else 0
            
        # Update point position based on movement
        points[1, i] = y_offset

        # Draw the point lights
        ax.plot(points[0, i], points[1, i], 'o', color='white', markersize=15)

    return ax,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=1000/24, blit=False)

# Show the animation
plt.show()

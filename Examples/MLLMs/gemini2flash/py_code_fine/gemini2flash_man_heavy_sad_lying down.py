
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the number of points
num_points = 15

# Initialize point coordinates (you'll need to adjust these)
points = np.zeros((num_points, 2))

# Head
points[0, :] = [0.5, 0.9]

# Shoulders
points[1, :] = [0.3, 0.7]
points[2, :] = [0.7, 0.7]

# Elbows
points[3, :] = [0.1, 0.5]
points[4, :] = [0.9, 0.5]

# Wrists
points[5, :] = [0.1, 0.3]
points[6, :] = [0.9, 0.3]

# Hips
points[7, :] = [0.3, 0.3]
points[8, :] = [0.7, 0.3]

# Knees
points[9, :] = [0.3, 0.1]
points[10, :] = [0.7, 0.1]

# Ankles
points[11, :] = [0.3, -0.1]
points[12, :] = [0.7, -0.1]

# Feet
points[13, :] = [0.2, -0.3]
points[14, :] = [0.8, -0.3]



# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(-0.5, 1)  # Adjust y-axis limits for laying down
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=20)


# Function to update the animation
def update(frame_number):
    # Modify point positions to simulate "laying down" motion
    # This is a simplified example; you'll likely need more complex logic
    # for realistic motion

    # Example: Slight swaying and limb movements
    for i in range(num_points):
        # Subtle horizontal movement
        points[i, 0] += 0.002 * np.sin(frame_number / 10 + i)
        # Keep points within bounds
        points[i, 0] = np.clip(points[i, 0], 0, 1)

    # Simulate heavy weight/sadness with subtle drooping
    vertical_offset = 0.001 * np.sin(frame_number / 15)
    points[0, 1] -= vertical_offset # Head sags

    
    scat.set_offsets(points)
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()

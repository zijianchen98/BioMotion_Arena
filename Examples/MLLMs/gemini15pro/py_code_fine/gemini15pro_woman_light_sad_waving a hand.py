
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point-lights
# These coordinates are placeholders and need to be adjusted 
# based on the actual motion capture data or desired animation path.
# The structure should represent the human body with head, shoulders, elbows,
# wrists, hips, knees, and ankles.

num_frames = 60  # Number of frames in the animation

# Initialize the point-light coordinates for each frame
point_lights = np.zeros((num_frames, 15, 2))

# Example: Simple waving hand animation (replace with realistic data)
for frame in range(num_frames):
    angle = frame * (2 * np.pi) / num_frames  # Angle for the waving motion
    
    # Example coordinates (adjust these to match the desired animation)
    point_lights[frame] = [
        [50, 150],  # Head
        [40, 130], [60, 130],  # Shoulders
        [30, 110], [70, 120 + 10 * np.sin(angle)],  # Elbows  # Waving motion for right elbow
        [20, 90], [75, 110 + 20 * np.sin(angle)],  # Wrists
        [45, 90], [55, 90],  # Hips
        [40, 60], [60, 60], # Knees
        [40, 30], [60, 30] # Ankles
        # ... (adjust remaining coordinates as needed)
    ]
   


# Create the figure and axes for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 100) # Adjust if your point-light motion goes beyond 100
ax.set_ylim(0, 160)
ax.set_aspect('equal') # Important for correct aspect ratio
ax.set_facecolor('black') # Set the background color to black


# Create the point-light scatter plot
scatter = ax.scatter([], [], s=20, c='white')


# Animation update function
def update(frame):
    x = point_lights[frame, :, 0]
    y = point_lights[frame, :, 1]
    scatter.set_offsets(np.c_[x, y])  # Update the point-light positions
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)


# Save the animation as a GIF (optional)
# ani.save('biological_motion.gif', writer='imagemagick')

# Display the animation
plt.show()

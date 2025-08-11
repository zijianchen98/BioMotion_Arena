
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15  # Total number of points
duration = 2000  # Duration of the animation in milliseconds
fps = 30  # Frames per second
num_frames = (duration * fps) // 1000  # Total number of frames
jump_height = 1.5  # Max height of the jump
jump_distance = 2  # Forward distance of the jump

# Initial positions of the point lights (representing body parts)
# Distributing points like a person standing
positions = np.array([
    [0, 0],  # Head
    [-0.25, -0.5], [0.25, -0.5],  # Shoulders
    [-0.5, -1], [0, -1], [0.5, -1],  # Arms
    [-0.25, -2], [0, -2], [0.25, -2],  # Torso and hips
    [-0.5, -3], [0.5, -3],  # Legs
])

# Animation function
def animate(i):
    plt.clf()  # Clear the current figure
    plt.xlim(-3, 3)
    plt.ylim(-4, 2)
    plt.axis('off')  # Turn off the axes

    # Calculate y movement based on a smooth jump curve
    t = i / num_frames * np.pi
    y_offset = jump_height * np.sin(t)  # Simple sine wave for jump
    x_offset = (i / num_frames) * jump_distance  # Linear move forward
    
    # Apply offsets to positions
    animated_positions = positions + np.array([x_offset, y_offset])

    # Create point lights
    for pos in animated_positions:
        plt.plot(pos[0], pos[1], 'o', color='white', markersize=10)

# Setup figure
fig = plt.figure(figsize=(6, 8))
fig.patch.set_facecolor('black')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000/fps)

# Display the animation
plt.show()

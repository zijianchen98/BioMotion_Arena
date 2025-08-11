
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Constants**
num_points = 15  # Total number of point-lights
duration = 5     # Total duration of the animation in seconds
fps = 30         # Frames per second
frames = duration * fps  # Total frames in the animation
time = np.linspace(0, duration, frames)  # Time array for each frame

# **Point-Lights Coordinates**
# Initial coordinates for the points representing a woman lying down
# You can adjust these values for a more realistic position
positions = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.75, 0], [0.75, 0],  # Arms
    [-1, -0.5], [1, -0.5],  # Elbows
    [-1, -1], [1, -1],      # Hands (on the ground)
    [-0.5, -1.5], [0.5, -1.5],  # Hips
    [-0.5, -2], [0.5, -2],  # Knees
    [0, -2.5]  # Feet
])

# **Animation Function**
def update(frame):
    plt.clf()  # Clear the current frame
    plt.xlim(-2, 2)  # Set x-axis limits
    plt.ylim(-3, 2)  # Set y-axis limits
    plt.gca().set_facecolor('black')  # Set background color to black
    plt.axis('off')  # Turn off the axis

    # Update point-light positions based on a sample oscillatory motion (e.g., breathing)
    oscillation = 0.05 * np.sin(2 * np.pi * (frame / fps))
    updated_positions = positions + oscillation
    
    # Plot the point-lights
    plt.scatter(updated_positions[:, 0], updated_positions[:, 1], color='white', s=100)

# **Creating the Figure and Animation**
fig = plt.figure(figsize=(5, 10))
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps)

# **Display the Animation**
plt.show()

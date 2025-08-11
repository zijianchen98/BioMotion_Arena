
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and frame rate
num_frames = 60  # Number of frames in the animation
frame_rate = 30  # Frame rate in Hz

# Define the positions of the 15 points of light
points = [
    (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),  # Head and torso
    (2, 2), (3, 2), (4, 2),                  # Upper arms
    (2, 3), (3, 3),                          # Hands
    (4, 4), (5, 4)                          # Legs
]

# Create the figure and axis
fig, ax = plt.subplots()
ax, ax.set_xlim(0, 7)
1, ax.set_ylim(-1, 6)
1, ax.set_aspect('equal')
1, ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter(*zip(*points), c='white')

def update(frame):
    # Calculate the new position based on the frame
    positions = []
    for x, y in points:
        x = x + np.sin(2 * np.pi * (frame / num_frames)) * 0
        y += np.sin(2 * np.pi * (frame / num_frames)) * 2
        positions.append((x, y))
    
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000, blit=True)

# Show the animation
plt.show()

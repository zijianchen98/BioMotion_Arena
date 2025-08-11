
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points that represent the figure
points = np.array([
    [0, 10],   # Head
    [0, 9],    # Neck
    [-1, 8],   # Right Shoulder
    [-1, 7],   # Right Elbow
    [-1, 6],   # Right Wrist
    [1, 8],    # Left Shoulder
    [1, 7],    # Left Elbow
    [1, 6],    # Left Wrist
    [0, 8],    # Waist
    [-1, 7.5],  # Right Hip
    [-1, 5],   # Right Knee
    [-1, 3],   # Right Ankle
    [1, 7.5],  # Left Hip
    [1, 5],    # Left Knee
    [1, 3]     # Left Ankle
])

# Define the jumping motion
def update_points(frame, points, scatter):
    amplitude = 3
    period = 100
    phase = 2 * np.pi * frame / period
    
    # Apply sinusoidal motion to the points
    new_positions = np.copy(points)
    new_positions[:, 1] += amplitude * np.sin(phase)
    
    # Update the scatter plot
    scatter.set_offsets(new_positions)

# Create the figure and the points to animate
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 15)
ax.set_facecolor('black')
scatter = ax.scatter(points[:, 0], points[:, 1], s=50, color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_points, fargs=(points, scatter), frames=range(200), interval=50)

# Show the animation
plt.axis('off')
plt.show()

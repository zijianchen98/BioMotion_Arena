
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define initial positions of the point-lights
# These positions represent the key points of a human body
initial_positions = np.array([
    [0.45, 0.85],  # head
    [0.55, 0.85],
    [0.40, 0.75],  # shoulders
    [0.60, 0.75],
    [0.45, 0.65],  # elbows
    [0.55, 0.65],
    [0.40, 0.55],  # wrists
    [0.60, 0.55],
    [0.45, 0.50],  # waist
    [0.55, 0.50],
    [0.40, 0.40],  # hips
    [0.60, 0.40],
    [0.45, 0.35],  # knees
    [0.55, 0.35],
    [0.45, 0.25],  # feet
    [0.55, 0.25]
])

# Define the animation function
def update(frame):
    ax.clear()
    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
    # Calculate motion based on a simple sine function to simulate jumping
    amplitude = 0.1
    frequency = 0.5
    vertical_shift = 0.1 * np.sin(frequency * frame)
    
    positions = initial_positions.copy()
    positions[:, 1] += vertical_shift
    
    # Draw the point-lights
    for pos in positions:
        circle = plt.Circle(pos, 0.02, color='white')
        ax.add_patch(circle)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions are chosen to represent the major joints of the human body
initial_positions = np.array([
    [0, 0],  # head
    [-0.2, 0.5],  # left shoulder
    [0.2, 0.5],  # right shoulder
    [-0.2, 0.2],  # left elbow
    [0.2, 0.2],  # right elbow
    [-0.2, -0.2],  # left wrist
    [0.2, -0.2],  # right wrist
    [0, -0.5],  # hips
    [-0.2, -0.8],  # left knee
    [0.2, -0.8],  # right knee
    [-0.2, -1.1],  # left ankle
    [0.2, -1.1],  # right ankle
    [0, -0.3],  # torso
    [-0.1, 0.3],  # left upper arm
    [0.1, 0.3]  # right upper arm
])

# Define the animation function
def animate(frame):
    # Calculate the new positions of the point-lights based on the frame number
    # This is a simplified representation of the jumping motion
    positions = initial_positions.copy()
    if frame < 20:
        # Start in a squatting position
        positions[:, 1] -= 0.5
    elif frame < 40:
        # Jump up
        positions[:, 1] += (frame - 20) / 10
    elif frame < 60:
        # Reach the peak of the jump
        positions[:, 1] = 1
    elif frame < 80:
        # Fall back down
        positions[:, 1] -= (frame - 60) / 10
    else:
        # Land in a squatting position
        positions[:, 1] = -0.5
    
    # Update the positions of the point-lights
    scatter.set_offsets(positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the scatter plot of point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.show()

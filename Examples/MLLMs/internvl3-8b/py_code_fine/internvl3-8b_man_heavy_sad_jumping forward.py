
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define keyframes and corresponding positions (in this context, these could be placeholders for the actual computation)
keyframes = {
    "Jump": np.array([[-0.5, 0.0], [-0.25, 0.0], [-0.1, 0.6], [0.0, 0.6],
                      [0.1, 0.4], [0.2, 0.2], [0.25, 0.0], [0.4, 0.2],
                      [0.5, 0.4], [0.6, 0.6], [0.75, 0.6], [0.9, 0.4],
                      [1.0, 0.2], [1.0, 0.0], [1.0, 0.0]])
}

# Function to get the position of each point at a given step
def get_position(t, keyframe):
    return keyframe[:int(100*t)+1]

# Create the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# Create a scatter plot
scat = ax.scatter([], [], c='white')

# Animate function
def animate(t):
    # Update the data of the scatter plot:
    scat.set_offsets(get_position(t, keyframes["Jump"]))
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 1, 400), blit=True)

# Display the animation
plt.show()

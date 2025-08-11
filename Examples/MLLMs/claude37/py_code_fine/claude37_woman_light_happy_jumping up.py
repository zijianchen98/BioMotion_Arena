
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Number of points
num_points = 15

# Initial positions of the points, representing the body's posture
# For a jumping animation, we can define two keyframes: standing and in the air
standing_position = np.array([
    [0, 0.5],  # Head
    [-0.2, 0.3], [0.2, 0.3],  # Shoulders
    [-0.2, 0.1], [0.2, 0.1],  # Elbows
    [-0.3, -0.5], [0.3, -0.5],  # Hands
    [0, 0],  # Center of body
    [-0.2, -0.7], [0.2, -0.7],  # Knees
    [-0.3, -1], [0.3, -1],  # Feet
])

# Jumping position (arms up, higher elevation)
jumping_position = np.array([
    [0, 0.7],  # Head
    [-0.2, 0.5], [0.2, 0.5],  # Shoulders
    [-0.2, 0.3], [0.2, 0.3],  # Elbows
    [-0.5, -0.4], [0.5, -0.4],  # Hands
    [0, 0.2],  # Center of body
    [-0.2, -0.2], [0.2, -0.2],  # Knees
    [-0.3, -0.5], [0.3, -0.5],  # Feet
])

# Initialize scatter points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Determine the positions based on the animation frame
    if frame < 10:
        # Transitioning to the jump position
        alpha = frame / 10
        current_position = (1 - alpha) * standing_position + alpha * jumping_position
    else:
        # Transitioning back to the standing position
        alpha = (frame - 10) / 10
        current_position = (1 - alpha) * jumping_position + alpha * standing_position

    points.set_data(current_position[:, 0], current_position[:, 1])
    return points,

# Animate the figure
anim = animation.FuncAnimation(fig, update, frames=20, init_func=init, blit=True, interval=100)

# Display the animation
plt.show()

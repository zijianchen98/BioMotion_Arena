
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject's skeletal structure and joint motion
# This is a simplified representation - a real biomechanical model would be much more complex
# These values will drive the point light movements.  Adjust for 'running'
num_joints = 10  # Number of joints to represent
joint_positions = np.array([
    [0.2, 0.1],  # Hip 1
    [0.4, 0.3],  # Hip 2
    [0.6, 0.3],  # Knee 1
    [0.8, 0.4],  # Knee 2
    [1.0, 0.4],  # Ankle 1
    [1.2, 0.5],  # Ankle 2
    [1.4, 0.5],  # Foot
    [1.6, 0.6],  # Toe 1
    [1.8, 0.7],  # Toe 2
    [2.0, 0.8]   # Toe 3
])

# Define movement parameters for running (adjust these for realism)
time_scale = 0.1  # Adjust speed
phase_offset = 0.0  # Adjust timing
amplitude = 0.3  # Adjust intensity

# Animation parameters
fig, ax = plt.subplots()
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.2, 0.9)
ax.set_aspect('equal')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

points, = ax.plot([], [], 'w.', markersize=10)

# Function to update the animation frame
def animate(frame):
    current_time = frame * time_scale + phase_offset
    for i in range(num_joints):
        x = joint_positions[i][0] + amplitude * np.cos(2 * np.pi * current_time + i * 0.2)
        y = joint_positions[i][1] + amplitude * np.sin(2 * np.pi * current_time + i * 0.2)
        points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=30, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("running_happyman.gif", writer='pillow', fps=30)

plt.show()

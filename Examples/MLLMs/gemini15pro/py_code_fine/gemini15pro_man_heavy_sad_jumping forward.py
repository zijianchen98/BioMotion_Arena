
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint positions over time (replace with your actual motion data)
# This is a simplified example and would need to be refined for realistic motion
num_frames = 60
joint_positions = np.zeros((15, 2, num_frames))

# Example: Head movement (up and down)
joint_positions[0, 1, :] = 50 + 5 * np.sin(np.linspace(0, 2 * np.pi, num_frames))

# Example: Arm movement (swinging)
joint_positions[1, 0, :] = 40 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
joint_positions[1, 1, :] = 40 + 5 * np.cos(np.linspace(0, 2 * np.pi, num_frames))
joint_positions[2, 0, :] = 30 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
joint_positions[2, 1, :] = 30 + 5 * np.cos(np.linspace(0, 2 * np.pi, num_frames))


# ... (Similarly define positions for other 12 joints)

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=5)


# Animation update function
def update(frame):
    x = joint_positions[:, 0, frame]
    y = joint_positions[:, 1, frame]
    points.set_data(x, y)
    return points,


# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, blit=True)

# Save the animation (optional)
#ani.save('jumping_forward.gif', writer='imagemagick', fps=30)

# Show animation
plt.show()

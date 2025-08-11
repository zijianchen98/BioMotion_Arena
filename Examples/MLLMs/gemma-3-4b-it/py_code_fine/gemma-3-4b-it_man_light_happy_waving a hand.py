
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the subject's skeleton and joint locations (simplified for this example)
# This is a highly simplified representation for illustration.  A real biomechanical model would be far more complex.
# This needs to be adapted to represent the waving hand motion realistically.
hand_joint_positions = np.array([
    [0.0, 0.5],  # Wrist
    [0.7, 0.5],  # Palm
    [1.0, 0.2],  # Thumb
    [0.5, -0.3]   # Fingers
])

# Animation parameters
num_frames = 150
frame_rate = 30  # Frames per second
duration = num_frames / frame_rate

# Create a figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
lights = ax.scatter(np.array([0.0]) * np.ones(num_frames),
                    np.array([0.0]) * np.ones(num_frames),
                    s=10, c='white')

# Define a function to update the positions of the point-lights
def update(frame):
    # Simulate waving motion - a very basic example
    # Replace this with a more sophisticated biomechanical model
    for i in range(len(hand_joint_positions)):
        # Simple sinusoidal wave
        angle = (frame / (duration * 5)) * 2 * np.pi
        x = hand_joint_positions[i][0] + 0.5 * np.cos(angle)
        y = hand_joint_positions[i][1] + 0.5 * np.sin(angle)
        lights.set_offsets(np.array([[x, y]]))
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("waving_hand_animation.gif", writer='pillow', fps=frame_rate)

plt.show()

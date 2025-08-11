
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate sadman with heavy weight motion
def generate_motion(num_frames=100):
    motion = []
    for t in range(num_frames):
        angle = 2 * np.pi * t / num_frames
        positions = [
            (0, 0),  # Head
            (-0.1, -0.1),  # Left shoulder
            (0.1, -0.1),  # Right shoulder
            (-0.2, -0.5),  # Left arm
            (0.2, -0.5),  # Right arm
            (0, -1),  # Left hip
            (0, -1.2),  # Right hip
            (-0.3, -1.5),  # Left leg
            (0.3, -1.5),  # Right leg
            (-0.4 + 0.2 * np.sin(angle), -2),  # Left foot
            (0.4 + 0.2 * np.sin(angle), -2),  # Right foot
            (0, -0.7),  # Back
            (-0.1, -0.8),  # Left side
            (0.1, -0.8),  # Right side
            (0, -1.8)  # Weight
        ]
        motion.append(positions)
    return motion

# Animation update function
def update(frame, scatter):
    scatter.set_offsets(motion[frame])
    return scatter,

# Generate motion data
motion = generate_motion()

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 1)
ax.axis('off')
scatter = ax.scatter([], [], c='white', s=50)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(motion), fargs=(scatter,), interval=50, blit=True)

# Display the animation
plt.show()

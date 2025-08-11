
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define key body parts as point-light sources
# Initial positions (x, y)
body_parts = {
    'head': np.array([0, 0]),
    'neck': np.array([0, -5]),
    'shoulders': np.array([[-5, -10], [5, -10]]),  # left and right shoulders
    'elbows': np.array([[-8, -15], [8, -15]]),  # left and right elbows
    'wrists': np.array([[-10, -20], [10, -20]]),  # left and right wrists
    'hips': np.array([[-5, -5], [5, -5]]),  # left and right hips
    'knees': np.array([[-7, 0], [7, 0]]),  # left and right knees
    'ankles': np.array([[-9, -10], [9, -10]]),  # left and right ankles
}

# Number of frames in the animation
num_frames = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-20, 20)
ax.set_ylim(-30, 5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Plot initial points
points, = ax.plot([], [], 'wo', markersize=5)

# Animation update function
def update(frame):
    t = frame / num_frames * 2 * np.pi
    
    # Define the motion for each body part
    def motion(part, base, amplitude, frequency):
        return base + np.array([amplitude * np.sin(frequency * t), amplitude * np.cos(frequency * t)])
    
    # Update positions
    positions = {}
    for part, base_pos in body_parts.items():
        if isinstance(base_pos, list):
            positions[part] = [motion(part, pos, 2, 1) for pos in base_pos]
        else:
            positions[part] = motion(part, base_pos, 2, 1)
    
    # Extract x and y coordinates
    x = []
    y = []
    for part_pos in positions.values():
        x.extend(part_pos[:, 0])
        y.extend(part_pos[:, 1])
    
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

plt.show()

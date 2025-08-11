
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define keyframes for jumping forward motion
def generate_motion_frames():
    frames = []
    for t in np.linspace(0, 1, 30):
        # Define body joints' positions (simplified model)
        head = [0, 1.5]
        shoulders = [-0.5, 1], [0.5, 1]
        elbows = [-0.75, 0.5], [0.75, 0.5]
        wrists = [-0.75, 0], [0.75, 0]
        hips = [-0.5, 0.5], [0.5, 0.5]
        knees = [-0.5, 0], [0.5, 0]
        ankles = [-0.25, -0.5], [0.25, -0.5]

        # Apply motion to joints for the "jumping forward" action
        body_part_offsets = [head, shoulders[0], shoulders[1], elbows[0], elbows[1],
                                wrists[0], wrists[1], hips[0], hips[1], knees[0],
                                knees[1], ankles[0], ankles[1]]

        # Adjust positions based on motion frame
        y_offset = 0.5 * np.sin(2 * np.pi * t)
        x_offset = 0.2 * t
        frame = [(x + x_offset, y + y_offset) for x, y in body_part_offsets]
        frames.append(frame)
    return frames

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
scat = ax.scatter([], [], color='white')

# Animation update function
def update(frame):
    scat.set_offsets(frame)
    return scat,

# Generate motion frames
frames = generate_motion_frames()

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=100, blit=True)

plt.axis('off')
plt.show()

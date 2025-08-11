
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and the frame interval
num_frames = 60
interval = 50

# Define the points (x, y coordinates) for the happywoman turning around animation
# The coordinates are designed to represent a turning motion
def generate_motion_frames(num_frames):
    motion_frames = []
    for i in range(num_frames):
        angle = (i / num_frames) * 2 * np.pi
        points = [
            (4, 0),            # Head
            (3, 1), (5, 1),  # Shoulders
            (2, 2), (6, 2),  # Elbows
            (3, 3), (5, 3),  # Hands
            (4, 2),            # Waist
            (3, 4), (5, 4),  # Hips
            (2, 5), (6, 5),  # Knees
            (3, 6), (5, 6),  # Feet
            (4, 8)             # Tail
        ]
        # Apply rotation to each point
        rotated_points = []
        for (x, y) in points:
            new_x = x * np.cos(angle) - y * np.sin(angle)
            new_y = x * np.sin(angle) + y * np.cos(angle)
            rotated_points.append((new_x, new_y))
        motion_frames.append(rotated_points)
    return motion_frames

# Generate motion frames
frames = generate_motion_frames(num_frames)

# Create the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

# Initialize points
points, = ax.plot([], [], 'wo')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    x, y = zip(*frames[frame])
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=num_frames, interval=interval, blit=True)

plt.axis('off')
plt.show()

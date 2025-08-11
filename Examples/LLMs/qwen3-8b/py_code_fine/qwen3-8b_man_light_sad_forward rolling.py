
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Parameters
num_points = 15
frame_rate = 30
duration = 5  # seconds
total_frames = frame_rate * duration

# Define a biomechanically plausible motion for a sad man in forward rolling
def sad_man_forward_rolling(t):
    # Simulate a rolling motion with some periodicity and variation
    # Each point follows a sine wave with phase shift and amplitude
    # To make it more realistic, we can add some randomness in phase and amplitude
    points = []
    for i in range(num_points):
        # Simulate a joint-like movement
        phase = np.random.uniform(0, 2 * np.pi)
        amplitude = np.random.uniform(0.2, 0.5)
        freq = np.random.uniform(0.1, 0.3)
        x = 100 + i * 6 + amplitude * np.sin(2 * np.pi * freq * t + phase)
        y = 50 + amplitude * np.sin(2 * np.pi * freq * t + phase + np.pi / 2)
        points.append((x, y))
    return points

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 200)
ax.set_ylim(0, 100)
ax.axis('off')

# Initialize the points
points = [Circle((0, 0), 3, color='white') for _ in range(num_points)]
for p in points:
    ax.add_patch(p)

# Animation function
def animate(t):
    for i, p in enumerate(points):
        x, y = sad_man_forward_rolling(t)[i]
        p.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=total_frames, interval=1000 / frame_rate, blit=False)

# Show the animation
plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the joint connection order to mimic biomechanical structure
connections = [
    (0, 1), (1, 2), (2, 3),  # Head, neck and spine
    (3, 4), (3, 5),         # Shoulders
    (4, 6), (5, 7),         # Upper arms
    (6, 8), (7, 9),         # Forearms
    (2, 10), (10, 11), (11, 12),  # Hips and torso
    (10, 13), (10, 14),     # Upper legs
    (13, 15), (14, 16),     # Lower legs
    (15, 17), (16, 18)      # Feet
]

# Define the point-light coordinates for a single "rolling forward" motion frame
# This is a simplification for demonstration
# Each row corresponds to (x, y) positions of one joint
keyframes = [
    [
        (0.0, 2.0), (0.0, 1.7), (0.0, 1.2), (0.0, 0.7),  # Head to spine
        (-0.2, 0.8), (0.2, 0.8),                        # Shoulders
        (-0.3, 0.5), (0.3, 0.5),                        # Upper arms
        (-0.4, 0.2), (0.4, 0.2),                        # Forearms
        (0.0, 0.7),                                     # Hips
        (-0.1, 0.5), (0.1, 0.5),                        # Torso to thighs
        (-0.2, 0.2), (0.2, 0.2),                        # Upper legs
        (-0.3, 0.0), (0.3, 0.0),                        # Lower legs
        (-0.3, -0.2), (0.3, -0.2)                       # Feet
    ],
    [
        (0.0, 1.9), (0.0, 1.6), (0.0, 1.1), (0.0, 0.6),  # Head to spine
        (-0.2, 0.7), (0.2, 0.7),                        # Shoulders
        (-0.3, 0.4), (0.3, 0.4),                        # Upper arms
        (-0.4, 0.1), (0.4, 0.1),                        # Forearms
        (0.0, 0.6),                                     # Hips
        (-0.1, 0.4), (0.1, 0.4),                        # Torso to thighs
        (-0.2, 0.1), (0.2, 0.1),                        # Upper legs
        (-0.3, -0.1), (0.3, -0.1),                      # Lower legs
        (-0.3, -0.3), (0.3, -0.3)                       # Feet
    ],
    # Add more keyframes here if desired for smoother motion
]

# Repeat the keyframes into a loop
keyframes = keyframes + list(reversed(keyframes))

# Interpolation for smooth animations
num_frames = 50
frames = []
for i in range(len(keyframes) - 1):
    start = keyframes[i]
    end = keyframes[i + 1]
    for t in np.linspace(0, 1, num_frames // len(keyframes)):
        interpolated = [(s[0] + t * (e[0] - s[0]), s[1] + t * (e[1] - s[1])) for s, e in zip(start, end)]
        frames.append(interpolated)

# Setup the animation plot
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 2.5)
ax.set_facecolor('black')
plt.axis('off')

points, = plt.plot([], [], 'wo', markersize=8)  # Plot for joints
lines = [plt.plot([], [], 'w-', lw=2)[0] for _ in connections]  # Plots for bone connections

# Update function for animation
def update(frame):
    x = [pt[0] for pt in frame]
    y = [pt[1] for pt in frame]
    points.set_data(x, y)
    for line, (i, j) in zip(lines, connections):
        line.set_data([frame[i][0], frame[j][0]], [frame[i][1], frame[j][1]])
    return [points] + lines

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=frames, blit=True, interval=50, repeat=True
)

plt.show()

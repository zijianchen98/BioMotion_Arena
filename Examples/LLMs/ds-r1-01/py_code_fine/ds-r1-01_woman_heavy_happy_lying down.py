
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points' data: start and end positions, start_time (0-1), duration (0-1)
points = [
    # Head
    {'start': (0.0, 0.8), 'end': (0.0, 0.2), 'start_time': 0.2, 'duration': 0.6},
    # Neck
    {'start': (0.0, 0.7), 'end': (0.0, 0.2), 'start_time': 0.2, 'duration': 0.6},
    # Left Shoulder
    {'start': (-0.2, 0.6), 'end': (-0.2, 0.2), 'start_time': 0.3, 'duration': 0.5},
    # Right Shoulder
    {'start': (0.2, 0.6), 'end': (0.2, 0.2), 'start_time': 0.3, 'duration': 0.5},
    # Left Elbow
    {'start': (-0.3, 0.5), 'end': (-0.3, 0.2), 'start_time': 0.4, 'duration': 0.4},
    # Right Elbow
    {'start': (0.3, 0.5), 'end': (0.3, 0.2), 'start_time': 0.4, 'duration': 0.4},
    # Left Wrist
    {'start': (-0.4, 0.4), 'end': (-0.4, 0.2), 'start_time': 0.5, 'duration': 0.3},
    # Right Wrist
    {'start': (0.4, 0.4), 'end': (0.4, 0.2), 'start_time': 0.5, 'duration': 0.3},
    # Torso
    {'start': (0.0, 0.55), 'end': (0.0, 0.2), 'start_time': 0.1, 'duration': 0.7},
    # Left Hip
    {'start': (-0.1, 0.3), 'end': (-0.1, 0.2), 'start_time': 0.0, 'duration': 0.8},
    # Right Hip
    {'start': (0.1, 0.3), 'end': (0.1, 0.2), 'start_time': 0.0, 'duration': 0.8},
    # Left Knee
    {'start': (-0.15, 0.15), 'end': (-0.15, 0.2), 'start_time': 0.0, 'duration': 0.8},
    # Right Knee
    {'start': (0.15, 0.15), 'end': (0.15, 0.2), 'start_time': 0.0, 'duration': 0.8},
    # Left Ankle
    {'start': (-0.2, 0.0), 'end': (-0.2, 0.2), 'start_time': 0.0, 'duration': 0.8},
    # Right Ankle
    {'start': (0.2, 0.0), 'end': (0.2, 0.2), 'start_time': 0.0, 'duration': 0.8},
]

# Smoothstep function for smooth animation
def smoothstep(t):
    return t * t * (3 - 2 * t)

# Initialize the plot
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter(
    [p['start'][0] for p in points],
    [p['start'][1] for p in points],
    color='white', s=50, edgecolors='none'
)

# Animation update function
def update(frame):
    t = frame / 100  # Normalize time between 0 and 1
    new_positions = []
    for point in points:
        start_x, start_y = point['start']
        end_x, end_y = point['end']
        st, dur = point['start_time'], point['duration']
        
        progress = (t - st) / dur
        if progress < 0:
            new_x, new_y = start_x, start_y
        elif progress > 1:
            new_x, new_y = end_x, end_y
        else:
            s = smoothstep(progress)
            new_x = start_x + (end_x - start_x) * s
            new_y = start_y + (end_y - start_y) * s
        new_positions.append([new_x, new_y])
    
    scat.set_offsets(new_positions)
    return scat,

# Create and display the animation
ani = animation.FuncAnimation(
    fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True
)

plt.show()

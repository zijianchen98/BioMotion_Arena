
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
num_frames = 100

# Function to generate running motion data
def generate_running_motion(frame):
    # Create a basic sine-wave-like path for the arms and legs
    times = np.linspace(0, 2 * np.pi, num_frames)
    
    # Body parts positions (x,y) - represented as 2D coordinates
    positions = {
        'head': (0, 2 + 0.3 * np.sin(times[frame])),
        'left_shoulder': (-0.5, 1 + 0.2 * np.sin(times[frame])),
        'right_shoulder': (0.5, 1 + 0.2 * np.sin(times[frame])),
        'left_elbow': (-0.5, 0.5 + 0.2 * np.sin(times[frame])),
        'right_elbow': (0.5, 0.5 + 0.2 * np.sin(times[frame])),
        'left_hand': (-0.5, 0 + 0.2 * np.sin(times[frame])),
        'right_hand': (0.5, 0 + 0.2 * np.sin(times[frame])),
        'torso': (0, 1.5),
        'left_hip': (-0.2, 1 - 0.2 * np.sin(times[frame])),
        'right_hip': (0.2, 1 - 0.2 * np.sin(times[frame])),
        'left_knee': (-0.2, 0 - 0.3 * np.sin(times[frame])),
        'right_knee': (0.2, 0 - 0.3 * np.sin(times[frame])),
        'left_foot': (-0.2, -0.5 - 0.2 * np.sin(times[frame])),
        'right_foot': (0.2, -0.5 - 0.2 * np.sin(times[frame])),
    }
    
    return np.array(list(positions.values()))

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create the points
points, = ax.plot([], [], 'wo', markersize=10)  # 'wo' for white points

# Animation function
def init():
    points.set_data([], [])
    return points,

def animate(frame):
    data = generate_running_motion(frame)
    points.set_data(data[:, 0], data[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init, blit=True, interval=1000/30)

# Show the animation
plt.show()

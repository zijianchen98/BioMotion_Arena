
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants for the animation
NUM_POINTS = 15
FIG_SIZE = (6, 10)
DURATION = 100  # duration in frames
FPS = 20  # frames per second

# Biomechanical data for "sad woman sitting down"
# These are x, y coordinates for 15 key points of the body.
# Each body part's motion is represented by a trajectory (list of coordinates over time)
# For this simple example, these trajectories are generated programmatically.
def generate_sitting_down_motion():
    # Initialize key points for "standing" position
    key_points = {
        "head": [0, 5],
        "shoulders": [[-1, 4], [1, 4]],
        "elbows": [[-2, 3], [2, 3]],
        "hands": [[-3, 2], [3, 2]],
        "hips": [[-1, 2], [1, 2]],
        "knees": [[-1, 1], [1, 1]],
        "feet": [[-1, 0], [1, 0]],
    }

    frames = DURATION
    trajectories = {}

    # Generate smooth downward movement for "sitting down" action
    for key, point in key_points.items():
        if isinstance(point[0], list):  # Handle body parts with two points (e.g., shoulders, hands)
            trajectories[key] = []
            for sub_point in point:
                trajectory = [
                    [sub_point[0], np.interp(t, [0, frames], [sub_point[1], sub_point[1] - 1])]
                    for t in range(frames)
                ]
                trajectories[key].append(trajectory)
        else:
            trajectory = [
                [point[0], np.interp(t, [0, frames], [point[1], point[1] - 1])]
                for t in range(frames)
            ]
            trajectories[key] = trajectory

    # Combine all data into a flat list of 15 points for each frame
    final_trajectories = []
    for t in range(frames):
        frame_points = []
        for key, traj in trajectories.items():
            if isinstance(traj[0], list):
                frame_points.extend([[p[0], p[1]] for p in (traj[0][t], traj[1][t])])
            else:
                frame_points.append([traj[t][0], traj[t][1]])
        final_trajectories.append(frame_points)

    return np.array(final_trajectories)

# Generate motion data
motion_data = generate_sitting_down_motion()

# Create the animation
fig, ax = plt.subplots(figsize=FIG_SIZE, facecolor="black")
ax.axis("off")
ax.set_xlim(-4, 4)
ax.set_ylim(-2, 6)

points, = ax.plot([], [], "wo", ms=8)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    x = motion_data[frame, :, 0]
    y = motion_data[frame, :, 1]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(
    fig, update, frames=DURATION, init_func=init, blit=True, interval=1000/FPS
)

plt.show()

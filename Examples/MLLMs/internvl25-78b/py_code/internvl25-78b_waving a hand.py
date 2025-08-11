
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'w.', markersize=10)

# Define the motion of the waving hand
def init():
    points.set_data([], [])
    return points,

def update(frame):
    t = frame / 10.0
    # Positions of the points (simplified kinematic model)
    x0, y0 = 0.5, 0.8
    arm_length = 0.3
    angle = np.sin(t) * 0.7
    shoulder = np.array([x0, y0])
    elbow = shoulder + np.array([-arm_length * 0.5 * np.cos(angle), -arm_length * 0.5 * np.sin(angle)])
    wrist = elbow + np.array([-arm_length * 0.5 * np.cos(angle), -arm_length * 0.5 * np.sin(angle)])
    
    # Calculate finger positions
    finger_vectors = [
        np.array([0.05 * np.cos(np.pi * i / 7), 0.05 * np.sin(np.pi * i / 7)]) for i in range(7)
    ]
    finger_positions = [wrist + vec for vec in finger_vectors]

    # All points
    all_points = [shoulder, elbow, wrist] + finger_positions

    # Create the data for the points
    x = [p[0] for p in all_points]
    y = [p[1] for p in all_points]

    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

plt.show()

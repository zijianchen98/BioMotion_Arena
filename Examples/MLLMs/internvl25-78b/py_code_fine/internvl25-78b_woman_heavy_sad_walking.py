
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light structure
def generate_biological_motion():
    motion = np.zeros((15, 2, 50))  # 15 points, 2D coordinates, 50 frames
    
    # Setup initial positions (simplified model)
    y_pos = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7])
    x_pos = np.array([0, -1, 1, -1, 0, 1, -2, -1, 0, 1, -1, 0, 1, 0, 0])
    
    motion[:, 0, 0] = x_pos
    motion[:, 1, 0] = y_pos
    
    for frame in range(1, 50):
        motion[:, 1, frame] = y_pos + np.sin(frame / 5.0)  # vertical motion simulating walking
        motion[:, 0, frame] = x_pos + 0.1 * np.sin(frame / 3.0)  # side-to-side motion

    return motion

# Animation function
def animate_motion(motion):
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 8)
    points, = ax.plot([], [], 'wo', markersize=10)

    def init():
        points.set_data([], [])
        return points,

    def update(frame):
        x = motion[:, 0, frame]
        y = motion[:, 1, frame]
        points.set_data(x, y)
        return points,

    anim = animation.FuncAnimation(fig, update, frames=50, init_func=init, blit=True, repeat=True)
    plt.axis('off')
    plt.show()

# Generate and animate
motion_data = generate_biological_motion()
animate_motion(motion_data)

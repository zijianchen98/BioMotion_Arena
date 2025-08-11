
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def load_point_light_positions():
    # Here we simulate the positions of point lights (for simplicity)
    # In reality, these would be calculated based on a biomechanical model or motion capture data.

    # Let's create a simplified version where 15 points represent a hand waving
    # Assume these points move from bottom left to top right, simulating a wave

    path = np.linspace([0, 0], [1, 1], 100)  # Sample path from bottom left to top right
    points = np.random.rand(15, 2) * 0.2 + [0.4, 0.4]  # Random points relative to a base position

    frames = []
    for frame, (x, y) in enumerate(path):
        new_positions = points + [x, y]
        frames.append(new_positions)

    return frames

def animate_points(frames):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')
    
    scat = ax.scatter([], [], color='white')

    def update(frame):
        scat.set_offsets(frame)
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, repeat=True, interval=50)
    plt.show()

point_positions = load_point_light_positions()
animate_points(point_positions)

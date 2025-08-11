
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
positions = np.array([
    [10, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
    (3, 10), (3, 11), (3, 12), (3, 13), (3, 14)
])

# Define the number of frames and frame rate
num_frames = 200
frame_rate = 20

def update_positions(frame):
    # Update the positions based on a simple sine wave motion
    time = frame / float(num_frames - 1) * 2 * np.pi
    amplitude = 1
    frequency = 0
    
    new_positions = np.copy(positions)
    new_positions[:, 1] += amplitude * np.sin(time + new_positions[:, 0])
    return new_positions

def animate():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    scat = ax.scatter(positions[:, 0], positions[:, 1], c='w', s=100)
    
    def init():
        return scat,
    
    def animate_frame(i):
        new_positions = update_positions(i)
        scat.set_offsets(new_positions)
        return scat,
    
    ani = FuncAnimation(fig, animate_frame, frames=num_frames, init_func=init, blit=True, interval=int(1000 / frame_rate))
    plt.show()

if __name__ == "__main__":
    animate()

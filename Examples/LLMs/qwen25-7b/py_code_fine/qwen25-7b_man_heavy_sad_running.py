
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the sadman (15 points)
initial_positions = np.array([
    [0, 50, 50, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 59, 58 ],
    [ 50, 54, 57, 60, 65, 68, 71, 74, 77, 80, 8d, 91, 94, 97, 100]
]).T

# Define the motion parameters
frame_duration = 00ms  # Duration of each frame in milliseconds
num_frames = 150  # Number of frames for the animation

def update_position(positions, frame):
    # Update positions based on a simple harmonic motion model
    amplitude = 10
    frequency = 0.5
    phase = 0.5
    position[0] += amplitude * np.sin(2 * np.pi * frequency * frame + phase)

def animate(frame):
    update_position(initial_positions, frame)
    ax.clear()
    ax.scatter(initial_positions[:, 0 ], initial_positions[:, 1], c='w', s=100)
    ax.set_xlim(-10, 110)
    ax.set_ylim(-10, 111)
    ax.set_aspect('equal')
    ax.axis('off')

fig, ax = plt.subplots()
aniimation = animation.FuncAnimation(fig, animate, frames=num_frames, interval=int(frame_duration), blit=False)
plt.show()

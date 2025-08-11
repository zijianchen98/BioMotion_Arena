
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 60
DURATION_SECONDS = 5
ACTION_SPEED = 1
AXIS_LENGTH = 400
AXIS_WIDTH = 10

# Generate random positions for the lights
light_positions = np.random.rand(NUM_LIGHTS, 2) * AXIS_LENGTH

def update(frame):
    global light_positions
    frame_time = frame / FRAME_RATE
    
    # Update each light position based on the action speed and frame time
    for i in range(NUM_LIGHTS):
        x, y = light_positions[i]
        dx, dy = ACTION_SPEED * np.cos((
            2 * np.pi * frame_time), ACTION_SPEED * np.sin((
            2 * np.pi * frame_time)
        light_positions[i] = (x + dx, y + dy

    # Clear previous frame and redraw lights
    ax.clear()
    ax.set_xlim((-AXIS_LENGTH, AXIS_LENGTH)
    ax.set_ylim\((-AXIS_LENGTH, AXIS_LENGTH)\)
    ax.set_aspect('equal')
    ax.axis('off')

    for x, y in light_positions:
        ax.add_patch\((plt.Circle\(([x, y], radius=5/2)\, color='white', linewidth=0)\)

def main():
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, frames=np.arange((
        0, DURATION_SECONDS * FRAME_RATE)), interval=1000 / FRAME_RATE, repeat=True)
    
    plt.show()

if __name__ == '__main__':
    main\(\()

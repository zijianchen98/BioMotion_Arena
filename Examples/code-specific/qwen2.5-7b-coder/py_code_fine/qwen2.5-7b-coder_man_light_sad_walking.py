
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_LIGHTS = 15
WALK_SPEED = 0.05
FRAMES_PER_SECOND = 30
TOTAL_FRAMES = int(2 * FRAMES_PER_SECOND)  # 2 seconds long

# Initialize positions
positions = np.random.rand(NUM_LIGHTS, 2) * 10 - 5  # Random initial positions within [-5, 5]

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

lights = [plt.Circle((pos[0], pos[1]), 0.1, color='white') for pos in positions]
for light in lights:
    ax.add_artist(light)

def update(frame):
    global positions
    for i in range(NUM_LIGHTS):
        # Simple walking motion
        if frame % 2 == 0:
            positions[i, 0] += WALK_SPEED
        else:
            positions[i, 0] -= WALK_SPEED
        
        # Wrap around the screen
        if positions[i, 0] > 5:
            positions[i, 0] = -5
        elif positions[i, 0] < -5:
            positions[i, 0] = 5
        
        # Update the position of each light
        lights[i].center = (positions[i, 0], positions[i, 1])
    
    return lights

ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000 / FRAMES_PER_SECOND, blit=True)
plt.show()

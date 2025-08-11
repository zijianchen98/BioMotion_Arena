
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FRAME_RATE = 30
DURATION = 2  # seconds
FPS = 60

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights
lights = [plt.Circle((0, 0), radius=0.01, color='white') for _ in range(NUM_LIGHTS)]
for light in lights:
    ax.add_patch(light)

# Happy man waving hand parameters
def get_hand_position(t):
    # Simple sine wave for hand movement
    x = 0.3 * np.sin(2 * np.pi * t)
    y = 0.4 + 0.1 * np.cos(4 * np.pi * t)
    return x, y

def animate(frame):
    t = frame / FPS
    hand_x, hand_y = get_hand_position(t)
    
    # Distribute lights around the hand
    angles = np.linspace(0, 2 * np.pi, NUM_LIGHTS, endpoint=False)
    for i, angle in enumerate(angles):
        r = 0.1 + 0.05 * np.sin(4 * np.pi * t + i * 0.5)
        x = hand_x + r * np.cos(angle)
        y = hand_y + r * np.sin(angle)
        lights[i].center = (x, y)
    
    return lights

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=int(DURATION * FPS), interval=1000 / FPS, blit=True)

# Show animation
plt.show()

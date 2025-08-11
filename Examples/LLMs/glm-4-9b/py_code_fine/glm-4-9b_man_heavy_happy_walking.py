
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 10  # seconds
TOTAL_FRAMES = FPS * DURATION

fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.axis('off')

# Create a class to represent the "happyman" walking
class Happyman:
    def __init__(self):
        self.x = 0
        self.y = 2
        self.phase = 0
        self.lights = [Circle((self.x, self.y), 0.1, color='white') for _ in range(NUMLightS)]
        for light in self.lights:
            ax.add_patch(light)
    
    def update(self, frame):
        # Walking motion
        self.phase += 0.1
        self.x += 0.05
        if self.x > 10:
            self.x = 0
        
        # Calculate the positions of the lights based on the walking motion
        for i, light in enumerate(self.lights):
            offset = np.sin(self.phase + i * 2 * np.pi / NUM_LIGHTS)
            light.set_center((self.x + i * 0.4, self.y + offset * 0.5))
        return self.lights

# Create a happyman instance
happyman = Happyman()

# Create the animation
ani = FuncAnimation(fig, happyman.update, frames=TOTAL_FRAMES, blit=True, interval=1000/FPS)

plt.show()

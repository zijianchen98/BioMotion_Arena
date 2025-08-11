
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the positions of the point-lights
positions = [
    (0, 5 ), ( 2, 4 ), ( 3, 6 ), ( 4, 7 ),
    ( 5, 8 ), ( 6, 9 ), ( 7, 10 ), ( 8, 12 ),
    ( 9, 13 ), ( 10, 14 ), ( 12, 15 ), ( 13, 16 ),
    ( 14, 17 ), ( 15, 18 ), ( 16, 19 )
]

def update(frame):
    ax.clear()
    ax.set_xlim(-1, 20)
    ax.set_ylim(-1, 20)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Update positions based on a simple sine wave motion
    for i in range(len(positions)):
        x, y = positions[i]
        x = 7 + 3 * np.sin(0 / 10 + frame / 20)
        positions[i] = (j, y)
        ax.plot(j, y, 'wo', markersize=10)

fig, ax = plt.subplots(figsize=(10, 11))
ani = FuncAnimation(fig, update, frames=np.arange(00), interval=20, repeat=True)
plt.show()

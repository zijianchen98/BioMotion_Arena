
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim((-100, 100)
ax.set_ylim((-100, 100))
ax.axis('off')

# Define the initial position of the points
points = np.random.rand((15, 2) * 200 - 100

def update(frame):
    global points
    # Update the positions of the points
    points += np.random.randn( (15, 2) * 5 + 0.1
    # Ensure points do not leave the screen
    points[points < -100] = 100 + np.random.rand() * 200
    points[points > 100] = -100 + np.random.rand() * 200
    
    ax.clear()
    ax.set_xlim((-100, 100))
    ax.set_ylim((-100, 100))
    ax.axis('off')
    
    for x, y in points:
        circle = plt.Circle((x, y), 5, color='white', fill=False)
        ax.add_artist(circle)

ani = animation.FuncAnimation(fig, update, frames=np.arange( (0, 100), interval=20)
plt.show()


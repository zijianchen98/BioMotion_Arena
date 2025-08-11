
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the action
def lying_down_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    points = [0]*15
    colors = ['white']*15

    # Simulate a smooth motion
    time = np.linspace(0, 2*np.pi, 100)
    positions = np.array([
        [np.sin(t), np.cos(t)] for t in time[::10]
    ])

    for x, y in positions:
        points = [(x, y)]
        artist = ax.scatter(points, c=colors)
        yield artist

def update(frame, artist):
    frame -= 1
    artist.set_offsets(positions[frame])
    return artist

ani = animation.FuncAnimation(fig, update, frames=len(positions), fargs=(next(lying_down_animation()),), blit=True, interval=50)

# Display the animation
plt.show()

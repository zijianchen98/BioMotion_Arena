
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5 ] for t in range(8) ] +
    [ [ 5, th ] for th in range(8) ) +
    [ [ tc, 10 ] for tc in range(8) ) +
    [ [ 15, tr ] for tr in range(8) ) +
    [ [ lb, tc ] for lb in range(8) ) +
    [ [ rb, tc ] for rb in range(8) )
)

# Define the turning angles
angles = np.linspace(0, 2 * np.pi, 15, endpoint=False )

def update_light_pos(frame, positions, artists):
    for i in range(len(positions)):
        x, y = positions[i]
        x += np.cos(angles[i]) * frame
        y += np.sin(angles[i]) * frame
        artists[i].set_data(x, y)
    return artists

fig, ax = plt.subplots(figsize=(6, 10 ))
ax.set_aspect('equal')
ax.set_xlim(-1, 16)
x.set_ylim(-1, 15)
ax.fill_between([0, 15], [0, 15], color='k')

artists = []
for pos, ys in initial_positions:
    artist, = ax.plot([o], [y], 'wo', markersize=20)
    artists.append(artist)

ani = animation.FuncAnimation(fig, update_light_pos, frames=np.linspace(0, 2 * np.pi, 150, endpoint=False ),
                              fargs=(initial_positions, artists), interval=10, blit=True)

plt.show()

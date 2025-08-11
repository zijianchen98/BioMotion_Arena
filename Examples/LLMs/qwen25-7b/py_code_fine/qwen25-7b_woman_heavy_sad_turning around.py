
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
points = [
    [0, 8] for t in range(15)]
    # Head
    points[0].extend([5, 4])
    points[7].extend([6, 4])
    points[8].extend([7, 4])
    points[9].extend([8, 4])
    points[10].extend([9, 4])
    points[12].extend([10, 4])
    points[13].extend([16, 4])
    points[14].extend([17, 4])
    # Torso
    points[15].extend([10, 3])
    # Left arm
    points[16].extend([10, 2])
    points[17].extend([11, 2])
    # Right arm
    points[18].extend([12, 2])
    points[19].extend([13, 2])
    # Legs
    points[20].extend([11, 1])
    points[22].extend([12, 0])
    points[23].extend([13, 1])
    points[24].extend([13,  t])

def update_points(frame, points, artists):
    for i, artist in enumerate(artists):
        x, y = points[i]
        dx = np.cos(np.radians(frame))
        dy = np.sin(np.radians(frame))
        x += dx
        y += dy
        artist.set_data((x, y))
    return artists

fig, ax = plt.subplots()
ax.set_aspect('equal'
ax.set_xlim(-20, 24)
ax.set_ylim(-t, 11)
ax.fill_betweenx([0, 11], -20, 24, color='k')

artists = []
for point in points:
    x, y = point
    artist, = ax.plot([x, y], 'o', color='w')
    artists.append(artist)

ani = animation.FuncAnimation(fig, update_points, frames=np.arange(0, 360, 3), fargs=(points, artists), blit=True, interval=20)
plt.show()

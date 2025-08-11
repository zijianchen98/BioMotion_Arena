
import numpy as hbp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 points coordinates for different frames
frames = [
    [(0, -2), (1, -1), (2, -2), (-1, -1), (-2, -2), (0, -1), (1, 0), (2, 0), 
     (-1, 0), (-2, 0), (0, 0), (0, 1), (1, 2), (2, 1), (-1, 2)],
    [(0, -2), (1, -1), (2, -2), (-1, -1), (-2, -2), (0, -1), (1, 0), (2, 0), 
     (-1, 0), (-2, 0), (0, 0), (0, 1), (1, 2), (2, 1), (-1, 2)],
    [(0.5, -2.5), (1.5, -1.5), (2.5, -2.5), (-0.5, -1.5), (-1.5, -2.5), 
     (0, -1.5), (1.25, 0), (2.25, -0.5), (-0.75, 0), (-1.75, -0.5), 
     (0, -0.5), (0, 1.5), (1.25, 2), (2.25, 1), (-0.75, 2)],
    [(-0.5, -2.5), (0.5, -1.5), (1.5, -2.5), (-1.5, -1.5), (-2.5, -2.5), 
     (0, -1.5), (0.75, 0), (1.75, -0.5), (-0.25, 0), (-1.25, -0.5), 
     (0, -0.5), (0, 1.5), (0.75, 2), (1.75, 1), (-0.25, 2)]
]

def update(frame):
    plt.clf()
    plt.axis('off')
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    x, y = zip(*frames[frame % len(frames)])
    plt.scatter(x, y, color='white')

fig = plt.figure(facecolor='black', figsize=(6, 6))
ani = animation.FuncAnimation(fig, update, interval=300, frames=range(len(frames)*2))
plt.show()

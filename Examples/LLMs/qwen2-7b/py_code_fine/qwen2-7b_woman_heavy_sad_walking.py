
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_walking(num_frames=100):
    fig = plt.figure(figsize=(6, 6))
    ax = plt.axes(xlim=(0, 8), ylim=(-4, 4), aspect='equal')
    ax.set_facecolor('black')
    points = np.zeros((num_frames, 15, 2))
    
    def update(frame):
        points[frame] = np.random.rand(15 * 6 - 3, np.random.rand() * 8 - 4
        if frame > 0:
            for i in range(14:
                points[frame, i] += points[frame - 1, i]
        ax.clear()
        ax.plot(points[frame][:, 0], points[frame][:, 1], 'w.', markersize=1)
        ax.add_patch((
            plt.Circle((points[frame][-1, 0], points[frame][-1, 1]), radius=0.2, color='w', alpha=0.5),
        )
        
    anim = animation.FuncAnimation(fig, update, frames=num_frames, interval=20, repeat=False)
    plt.show()

if __name__ == "__main__":
    sad_woman_walking()
